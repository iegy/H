# حصن — موقع المتصفح

الموقع الرسمي لمتصفح **حصن** (Hisn) لأندرويد: شرح الخصائص وتحميل أحدث نسخة.

- `index.html` — الصفحة العربية
- `en/index.html` — الصفحة الإنجليزية
- `assets/` — التنسيق والشعار

ملف التطبيق موجود في `download/Hisn.apk`. النشر يتم تلقائياً من ريبو Hisn (workflow «Build Hisn APK» مع خيار «نشر على الموقع») عن طريق `tools/publish.py`، اللي بيحدّث الملف و`version.json` (اللي التطبيق بيقرأه للتحديث) والإصدار والحجم وبصمة SHA-256 في الصفحتين.
تصميم وتطوير Mohammed Hussein | [iegy.net](https://iegy.net/) — © 2026 All rights reserved.
