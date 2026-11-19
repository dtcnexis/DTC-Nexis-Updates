# DTC NEXIS — الدفعة 18: ختام سجلات Alpina غير المصنفة

التاريخ: 2026-11-19 | REVIEW_ONLY | NOT_APPROVED | NOT_PUBLISHED
الفرع: review/vehicle-foundation-audit-20261118
base_commit: 27bd0da249a80b23b12a48daf3a036bb111ee57c
source_queue: data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
source_raw: data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_001.csv
stable_ids: engines_part_001.csv:691–716 (26 records); only already-existing records reviewed; do not rewrite raw files.

## نتائج التحقق من المصدر
- 691: D5 S ALLRAD، 2019، 2993cc، 300kW، يختلف في القدرة عن الصف 690 (285kW) المدقق سابقاً.
- 692–694: D5 S TOU.ALLR / TOU.ALLR. / TOUR، 2021–2022، 2993cc، 300kW؛ الاختصارات والنقطة النهائية لا تثبت وحدة الهيكل أو نسخة الناقل؛ alias_candidates_only.
- 695–697: D5 S TOURING / TOURING ALLRAD، 2018، 2993cc، 285kW أو 300kW؛ اختلاف نسخ الدفع والقدرة محفوظ.
- 698/699: ROADSTER S / ROADSTER V8 هي طرازات مختلفة، 3346/4837cc؛ لا توحيد.
- 700–705: ستة سجلات Alpina model=unknown؛ ليست موديلات معتمدة، ويجب منع ترقية ملاءمة ناقل/ECU لها حتى يُثبت الموديل. 701/702 يشتركان في 2.0L Diesel ولكن displacement_cc=1994/1995؛ ليسا تكراراً حرفياً.
- 706: XB7، 2020، 4395cc و457kW؛ يحتاج سوق وناقل OEM.
- 707–711: XD3، سنة بدء جيل 2014، 2993cc وقدرات 245/261/285/290/257kW؛ لا تعميم السنة على كل نسخة.
- 712: XD3 BITURBO 2013، 2993cc 257kW Diesel؛ متسق مبدئياً مع وثيقة صانع Alpine الرسمية عن XD3 Bi-Turbo 2013 (مصدر أولي للسعة/القدرة فقط، يحتاج تحقق ناقل السوق):
  https://www.alpina-automobiles.com/fileadmin/user_upload/PDF_TechnicalData/TechDa_PerformanceDiagram/Leistungsdiagramm_BMW_ALPINA_XD3_BITURBO_2013_DE.pdf
  وهو lead وليس اعتماداً فنياً كاملاً.
- 713: XD3 BITURBO 2013، 2993cc 257kW **Petrol**، مع اختلاف نوع الوقود عن 712؛ POWERTRAIN_FUEL_CONFLICT_REVIEW.
- 714: XD3 BITURBO 2013، 4395cc 447kW Petrol؛ POWERTRAIN_IDENTITY_ANOMALY_HIGH. لا تنقله إلى نموذج آخر تلقائياً.
- 715/716: XD4 2019، 2993cc Diesel، 285/290kW، اختلاف محفوظ.

## نتيجة الدفعة ونقطة الاستئناف
prior_records_examined=26
deferred_for_OEM=26
new_approved_gearbox=0
new_imports=0
removed_duplicates=0
original_rows_changed=0
new_ECU_DTC_links=0
تراكم المراجعة في مجموعة OTHER من الدفعات 11–18 = 205 صفوف تمت قراءتها؛ ليس عدد السجلات المكتملة فنياً.
last_verified_row=engines_part_001.csv:716
next_queue_record=engines_part_001.csv:763 Aro M Series
تالي العمل: مراجعة Aro 763/764 وAston Martin Vanquish 854، ثم بقية السجلات غير المصنفة مع فحص OEM. مصادر PDF تحتاج فحصاً بصرياً مستقلاً عند الحكم على التفاصيل. يبقى ناقل 1,469 حالة ناقصاً في الجرد المرجعي ما لم يحدث اعتماد مستقل.
no_main_merge=true; no_site_or_windows_changes=true; no_release=true; no_source_deletion=true
