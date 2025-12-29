import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class IntegrityHandler(FileSystemEventHandler):
    def __init__(self, callback, db, ignore_dirs):
        self.callback = callback
        self.db = db
        self.ignore_dirs = ignore_dirs

    def on_modified(self, event):
        if not event.is_directory:
            self._process_event(event, "🔴 Modified")

    def on_created(self, event):
        if not event.is_directory:
            self._process_event(event, "🟡 Created")

    def on_deleted(self, event):
        if not event.is_directory:
            self._process_event(event, "❌ Deleted")

    def _process_event(self, event, status):
        path_parts = os.path.normpath(event.src_path).split(os.sep)
        if any(ignored in path_parts for ignored in self.ignore_dirs):
            return
            
        filename = os.path.basename(event.src_path)
        
        # Save to DB
        self.db.add_alert(filename, status)
        
        # UI Callback (will trigger protected notification in UI thread)
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
