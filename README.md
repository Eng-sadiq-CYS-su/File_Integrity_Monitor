# 🛡️ File Integrity Monitor: منصة التحقيق الجنائي الرقمي المتقدمة

![Project Banner](assets/banner.png)

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

## 📸 استكشف المنصة

````carousel
![الواجهة الرئيسية](assets/main_window.png)
<!-- slide -->
![تحليل البيانات](assets/scan_results.png)
<!-- slide -->
![إدارة التنبيهات](assets/alerts_management.png)
<!-- slide -->
![التقارير الاحترافية](assets/pdf_report.png)
````

---

## 🚀 الميزات المتقدمة

### 🧠 كشف المتسبب (Forensic Actor Discovery)
بخلاف أنظمة المراقبة التقليدية، تقوم هذه المنصة بتحديد **مصدر** التغيير. عبر تتبع مسارات النظام في لحظة التعديل، يتم ربط الحدث بالبرنامج المسؤول (مثل: `explorer.exe` أو أي سكريبت مشبوه).

### ⏪ محرك الاستعادة "العودة بالزمن"
كل فحص للنظام ينشئ "نقطة استعادة" آمنة. في حال تعرض ملف للتلف أو التشفير بواسطة برمجيات الرانسوموير (Ransomware)، يمكن لبروتوكول **Undo Change** استعادته فوراً من مخزن النسخ الاحتياطية المشفر.

### 📊 لوحات تحكم PDF ذكية
توليد تقارير جاهزة للتدقيق الأمني تشمل:
- **رسوم بيانية تفاعلية**: ملخص بصري لحالة النظام الأمنية.
- **دعم اللغة العربية**: تنسيق مثالي للمسارات والنصوص العربية داخل التقارير.
- **تحليلات إحصائية**: تحديد المجلدات الأكثر استهدفاً أو عُرضة للتغيير.

---

## 🏗️ البنية التقنية (Architecture)

```mermaid
graph TD
    A[نظام الملفات] -->|أحداث المراقبة| B(المراقب الفوري)
    B -->|التقاط الحدث| C{محرك التحقيق}
    C -->|تحديد العملية| D[متتبع العمليات Actor]
    C -->|حساب البصمة| E[مُشفر SHA-256]
    D --> F[خدمة قاعدة البيانات]
    E --> F
    F -->|الحفظ الاستمراري| G[(تخزين SQLite)]
    H[واجهة المستخدم] -->|أوامر التحكم| I[المتحكم الرئيسي]
    I -->|استعلام| F
    I -->|توليد| J[مُصدر تقارير PDF]
    K[مدير النسخ الاحتياطي] -->|لقطات أمان| A
```

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

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat-square&logo=linkedin)](https://github.com/Eng-sadiq-CYS-su) 
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=flat-square&logo=github)](https://github.com/Eng-sadiq-CYS-su)

---

## 📄 الرخصة
هذا المشروع مرخص بموجب رخصة MIT - راجع ملف [LICENSE](LICENSE) لمزيد من التفاصيل.

---
<p align="center">
  تم التطوير بكل ❤️ لتعزيز الأمن الرقمي العالمي.
</p>
