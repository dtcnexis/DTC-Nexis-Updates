# DTC NEXIS — الدفعة 94: تدقيق مستقل لاتساق نظام الدفع عبر 31,520 سجل محرك

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=REVIEW_ONLY / SOURCE-SEMANTIC CANDIDATES / NO_OEM_APPROVAL / NOT_PUBLISHED
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/VEHICLE_CONFLICT_OEM_CHECKPOINT_BATCH93_AR.md

## سبب التدقيق
أداة التعارض الأصلية رصدت 1,166 صفًا بسبب ثلاثة مؤشرات: اختلاف نوع/عدد سرعات ناقل الحركة، اختلاف cc >500، اختلاف القدرة >=20hp. لم تختبر تناقض AWD/FWD/RWD. هذه الدفعة تضيف قاعدة فحص **نظام الدفع** من النص الخام، دون تغيير التهجئة أو حذف السجلات.

## إدخال ومنهج
- قرئت جميع ملفات data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_001.csv إلى engines_part_017.csv من الفرع الحالي، وعدد صفوف المحركات **31,520**.
- استُخرج من engine_label ما يظهر بوضوح من: FWD, RWD, AWD, 4WD, 4x4، وإشارات AWD التجارية E-Four, 4MOTION, xDrive, quattro, 4MATIC.
- قورن مع الحقل structured drive (column 15, 0-based 14)، بعد تطبيع النص الصريح Front/Rear/All/Four Wheel Drive. لم يُعامل UNKNOWN كأنه فئة دفع معروفة.
- إذا احتوى النص على فئتين متعارضتين سجّل LABEL_SELF_CONTRADICTION. وإلا، إذا اختلف عن حقل الدفع الصريح سجّل LABEL_VS_STRUCTURED_DRIVE.
- **هذه قاعدة مؤشرات نصية عالية الاسترجاع وليست إثبات OEM.** قد يخطئ النص الخام، أو الحقل، أو كلاهما، ويجب تحديد النسخة والسوق والجيل والـVIN قبل التصحيح.
- استُخدمت مفاتيح source_file+source_line وفحصت فريدة لكل نتائج الدفعة، ولا توجد مفاتيح مكررة ضمنها.

## النتائج بعد تحقق CSV
- records_scanned=31520
- distinct_drive_candidate_rows=582
- LABEL_SELF_CONTRADICTION=40
- LABEL_VS_STRUCTURED_DRIVE=542
- overlap_with_original_1166_conflict_keys=30
- **NEW keys outside the prior 1166 = 552**
- combined_unique_candidate_keys=1718
- original_conflict_queue_keys=1166
- **هذه ليست 552 سيارة تم تصحيحها، ولا 1718 خللًا فنيًا مؤكدًا**. هي قائمة تحقيق موسعة.
- من حالات الدفعة 93 التي سبق فحصها فنيًا، رُصد صفان هنا أيضًا: Toyota Aqua engines_part_015.csv:714 وToyota C-HR engines_part_015.csv:937. لا يُعاد احتسابهما مراجعتين OEM جديدتين.
- الأكثر ورودًا في قائمة الدفعة 94 بحسب المصدر: BMW 106, Audi 59, Mercedes-Benz 42, Volkswagen 41, Smart 28؛ لا يثبت هذا ترتيب أخطاء الشركات أو الجودة.

## أثر جديد على سلامة البيانات
- Acura TLX engines_part_001.csv:111 و112: RAW FWD، structured Rear Wheel Drive. OEM source required to decide correct application and year.
- Alfa Romeo 75 engines_part_001.csv:365 و367: RAW RWD، structured Front Wheel Drive. Manufacturer's heritage documents cover the Alfa 75 rear-drive architecture.
- Toyota Corolla 2019–2022 engines_part_015.csv:1010 و1011: raw FWD، structured RWD; verify manufacturer-specific engine and model-year.
- Audi 100 quattro engines_part_001.csv:917: same label says quattro (AWD) and FWD simultaneously; field AWD. Variant/year needs OEM proof.
- These examples have not been automatically corrected.

## ملفات المخرجات والتحقق
- data/master/audits/vehicle_foundation_20261121/DRIVETRAIN_LITERAL_MISMATCH_REVIEW_BATCH94.csv
- Git commit=9071002e3f6fe6f33468fb6a104d8e30863fbbaa
- verified blob_sha=8452a2bf42438df710493c97e6ea439c89eaa8fd
- file holds **582 candidate records** with full provenance, source blob SHA per engine file, review status SOURCE_ONLY_NEEDS_OEM_APPLICABILITY, approval NOT_APPROVED.
- All original 17 CSV and 4 review-queue files remain unmodified.

## Next batch
last_completed_batch=94
next_batch=95
next_workstream=CHECK_ACURA_TLX_ALFA_75_TOYOTA_COROLLA_AND_AUDI_QUATTRO_SOURCE_CONTRADICTIONS_WITH_MANUFACTURER_EVIDENCE_AND_EXPLICIT_YEAR
new_approved_gearbox_assignments=0
new_approved_ECU_DTC_links=0
new_approved_vehicle_corrections=0
raw_rows_modified=0
main_merged=false
stable_updated=false

## حماية
No original data modifications, no master/Windows RC3.8.0/RC3.8.2 or site releases, no image gathering, no stable channel changes, and no auto-import of non-OEM source indicators.
