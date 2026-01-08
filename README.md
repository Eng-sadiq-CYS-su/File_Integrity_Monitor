# 🛡️ File Integrity Monitor: منصة التحقيق الجنائي الرقمي المتقدمة

<p align="center">
  <img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=1000" alt="File Integrity Monitor Banner" width="100%">
</p>

> **نظام متطور لمراقبة سلامة الملفات والاستجابة الفورية للتهديدات برؤية أمنية عميقة.**

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![UI Framework](https://img.shields.io/badge/Framework-PyQt5-orange?style=for-the-badge&logo=qt)](https://www.riverbankcomputing.com/software/pyqt/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Stability](https://img.shields.io/badge/Stability-Production--Ready-brightgreen?style=for-the-badge)]()

---

## 🌟 الرؤية الأمنية

في عصر التهديدات الرقمية المعقدة، لم تعد مراقبة النظام مجرد خيار، بل ضرورة قصوى. **File Integrity Monitor** هو أداة جنائية احترافية مصممة لاكتشاف وتتبع وعكس التغييرات غير المصرح بها في نظام الملفات بدقة تصل إلى أجزاء من الثانية.

### 🛡️ الركائز الأساسية
- **النزاهة المطلقة**: مدعومة بخوارزميات SHA-256 عالية الأداء ومتعددة المسارات.
- **التحقيق الجنائي (Forensics)**: ميزة اكتشاف "المتسبب" (Actor) لتحديد البرنامج المسؤول عن كل تعديل بدقة.
- **المرونة والاستعادة**: محرك "العودة بالزمن" المتكامل لاستعادة البيانات فوراً وضمان عدم فقدانها.
- **التقارير التنفيذية**: تقارير PDF ثنائية اللغة (عربي/إنجليزي) مع رسوم بيانية تفاعلية لتحليل البيانات.

---

## 🏗️ التصميم المنطقي للنظام (System Logic Drawing)

يوضح الرسم التالي تدفق البيانات الاستخباراتي داخل النظام من لحظة وقوع الحدث وحتى اتخاذ الإجراء الأمني:

```mermaid
graph TD
    %% Define Styles
    classDef security fill:#001f3f,stroke:#0074D9,stroke-width:2px,color:#fff;
    classDef storage fill:#2ECC40,stroke:#3D9970,stroke-width:2px,color:#fff;
    classDef forensic fill:#FF4136,stroke:#85144b,stroke-width:4px,color:#fff;
    classDef ui fill:#7FDBFF,stroke:#0074D9,stroke-width:1px,color:#000;

    Folder["📁 المجلد المراقب"] -- "تغيير في الملف" --> Watchdog["⚖️ محرك Watchdog"]
    Watchdog -- "حدث (تعديل/حذف)" --> Intelligence["🧠 محرك الذكاء الجنائي"]
    
    subgraph "Forensic Analysis Cell"
        Intelligence --> Actor["🕵️ كاشف المتسبب (Actor)"]
        Intelligence --> Hasher["🔢 مدقق البصمة (SHA-256)"]
        Actor -- "من البرنامج؟" --> Process["psutil: explorer.exe..."]
    end

    Process --> DB[("🗄️ قاعدة البيانات (SQLite)")]
    Hasher --> DB
    
    DB --> UI["🖥️ واجهة المستخدم (PyQt5)"]
    UI -- "طلب استعادة" --> Backup["⏪ مدير النسخ الاحتياطي"]
    Backup -- "استبدال الملف التالف" --> Folder

    class Intelligence,Actor forensic;
    class DB storage;
    class Watchdog security;
    class UI,Folder ui;
```

---

## 🎨 رسم تخطيطي للواجهة (UI Mockup Drawing)

توضيح مرئي لهيكل الواجهة الاحترافية التي تم تطويرها باستخدام PyQt5:

```mermaid
graph TD
    subgraph "نافذة البرنامج الرئيسية (Main Dashboard)"
        Header["🛡️ File Integrity Monitor (Header)"]
        
        subgraph "شريط الأدوات الأمني (Security Control Panel)"
            Btn1["▶️ Start Protection / بدء الحماية"]
            Btn2["🔔 View Alerts / التنبيهات"]
            Btn3["📄 Export PDF / تصدير تقرير"]
        end

        subgraph "مؤشرات الحالة (Status Indicators)"
            Folder["📂 Directory: C:/Users/Sadiq/Project"]
            Progress["▓▓▓▓▓▓▓▓░░ 80% (Scan Progress)"]
        end

        subgraph "سجل الأحداث الجنائي (Forensic Log Table)"
            Row1["📄 critical_file.dll | 🔴 Modified | Actor: notepad.exe"]
            Row2["📄 system_log.txt   | ❌ Deleted  | Actor: Unknown"]
            Row3["📄 malware_scan.py | 🟡 Created  | Actor: python.exe"]
        end
        
        Header --> Btn1
        Btn1 --> Folder
        Folder --> Progress
        Progress --> Row1
    end
```

---

## 🚀 الميزاث المتقدمة بالتفصيل

### 🧠 كشف المتسبب (Forensic Actor Discovery)
بخلاف أنظمة المراقبة التقليدية، تقوم هذه المنصة بتحديد **مصدر** التغيير. عبر تتبع مسارات النظام في لحظة التعديل، يتم ربط الحدث بالبرنامج المسؤول (مثل: `explorer.exe` أو أي سكريبت مشبوه).

### ⏪ محرك الاستعادة "العودة بالزمن"
كل فحص للنظام ينشئ "نقطة استعادة" آمنة. في حال تعرض ملف للتلف أو التشفير بواسطة برمجيات الرانسوموير (Ransomware)، يمكن لبروتوكول **Undo Change** استعادته فوراً من مخزن النسخ الاحتياطية المشفر.

### 📊 لوحات تحكم PDF ذكية
توليد تقارير جاهزة للتدقيق الأمني تشمل:
- **رسوم بيانية تفاعلية**: ملخص بصري لحالة النظام الأمنية.
- **دعم اللغة العربية**: تنسيق مثالي للمسارات والنصوص العربية داخل التقارير.

---

## 🛠️ التثبيت والتشغيل الاحترافي

### 1. إعداد البيئة
```bash
git clone https://github.com/Eng-sadiq-CYS-su/File_Integrity_Monitor.git
cd File_Integrity_Monitor
python -m venv .venv
source .venv/bin/activate  # لنظام ويندوز: .venv\Scripts\activate
```

### 2. تثبيت الملحقات
```bash
pip install -r requirements.txt
```

### 3. بناء الملف التنفيذي (Production Build)
لبناء نسخة مستقلة تعمل كبرنامج احترافي على ويندوز:
```bash
pyinstaller --noconsole --onefile --name "FileIntegrityMonitor" --icon "assets/icon.ico" --add-data "assets;assets" app.py
```

---

## 👤 المطور والرؤية التقنية

**صادق الموبدي (Sadiq Al-Mubdi)**
> *مهندس أمن سيبراني ومطور أنظمة متقدمة*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/sadiq-al-mubdi-3b8389387/) 
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=flat-square&logo=github)](https://github.com/Eng-sadiq-CYS-su)

---

## 📄 الرخصة
هذا المشروع مرخص بموجب رخصة MIT - راجع ملف [LICENSE](LICENSE) لمزيد من التفاصيل.

---
<p align="center">
  تم التطوير بكل ❤️ لتعزيز الأمن الرقمي العالمي.
</p>
