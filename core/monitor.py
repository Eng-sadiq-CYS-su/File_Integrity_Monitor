import os
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class IntegrityHandler(FileSystemEventHandler):
    def __init__(self, callback, db, ignore_dirs):
        self.callback = callback
        self.db = db
        self.ignore_dirs = ignore_dirs
        self._last_processed = {} # Cache to prevent rapid-fire duplicate alerts

    def on_modified(self, event):
        if not event.is_directory:
            self._process_event(event, "🔴 Modified")

    def on_created(self, event):
        if not event.is_directory:
            self._process_event(event, "🟡 Created")

    def on_deleted(self, event):
        if not event.is_directory:
            self._process_event(event, "❌ Deleted")

    def _get_process_locking_file(self, target_path):
        """Attempts to identify which process is currently accessing the file."""
        try:
            target_path = os.path.normpath(target_path).lower()
            for proc in psutil.process_iter(['name', 'open_files']):
                try:
                    # Check open file handles (this is the most accurate way)
                    files = proc.info.get('open_files')
                    if files:
                        for f in files:
                            if os.path.normpath(f.path).lower() == target_path:
                                return proc.info['name']
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        except Exception:
            pass
        return "Unknown / System"

    def _process_event(self, event, status):
        # 1. Basic filtering (temp files, hidden files)
        filename = os.path.basename(event.src_path)
        if filename.startswith('~') or filename.startswith('.') or filename.endswith('.tmp'):
            return

        # 2. Directory exclusion check
        path_parts = os.path.normpath(event.src_path).split(os.sep)
        if any(ignored in path_parts for ignored in self.ignore_dirs):
            return

        # 3. Hash-based deduplication (Critical for 'Modified' noise)
        from core.hasher import calculate_hash
        try:
            if os.path.exists(event.src_path):
                current_hash = calculate_hash(event.src_path)
                last_hash = self._last_processed.get(event.src_path)
                
                if current_hash == last_hash:
                    return # No real change, just a metadata write
                
                self._last_processed[event.src_path] = current_hash
            else:
                # File deleted, clear from cache
                if event.src_path in self._last_processed:
                    del self._last_processed[event.src_path]
        except:
            return # Busy/Locked file

        # 4. Forensic: Identify the Actor (Process)
        actor = self._get_process_locking_file(event.src_path)

        # Save to DB and Notify
        self.db.add_alert(filename, status, actor)
        self.callback(filename, status)

class RealTimeMonitor:
    def __init__(self, directory, callback, db, ignore_dirs=None):
        self.directory = directory
        self.callback = callback
        self.db = db
        self.ignore_dirs = ignore_dirs or []
        self.observer = Observer()

    def start(self):
        handler = IntegrityHandler(self.callback, self.db, self.ignore_dirs)
        self.observer.schedule(handler, self.directory, recursive=True)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()
