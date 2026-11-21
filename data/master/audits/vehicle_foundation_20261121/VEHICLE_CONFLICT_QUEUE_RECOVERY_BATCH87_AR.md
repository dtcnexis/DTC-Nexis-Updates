# DTC NEXIS — الدفعة 87: استعادة وفحص 1,166 حالة تعارض أصلية

date=2026-11-21
branch=review/vehicle-foundation-audit-20261118
status=CONFLICT_INDEX_RECOVERED / REVIEW_ONLY / NO_OEM_CORRECTION / NO_RELEASE
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_VALIDATION_CHECKPOINT_BATCH86_AR.md

## مسار الاستعادة
- استُخدم GitHub REST content listing ثم Git tree recursive لقمة الفرع review/vehicle-foundation-audit-20261118. فهرس GitHub code search يُفتِّش الفرع الافتراضي فقط، لذا لم يَعُد فشله السابق دليلًا على عدم وجود ملف.
- Git tree: https://api.github.com/repos/dtcnexis/DTC-Nexis-Updates/git/trees/review/vehicle-foundation-audit-20261118?recursive=1
- أصل الجرد:
  data/master/reviews/vehicle_catalog_full_20261118/ENGINE_TRANSMISSION_CONFLICT_AUDIT_AR.md
- أصل السجلات:
  data/master/reviews/vehicle_catalog_full_20261118/review_queue/engine_transmission_internal_conflicts_batch01.csv
  data/master/reviews/vehicle_catalog_full_20261118/review_queue/engine_transmission_internal_conflicts_batch02.csv
  data/master/reviews/vehicle_catalog_full_20261118/review_queue/engine_transmission_internal_conflicts_batch03.csv
  data/master/reviews/vehicle_catalog_full_20261118/review_queue/engine_transmission_internal_conflicts_batch04.csv

## تحقق ملفات الفرع
| file | physical data rows | Git blob |
|---|---:|---|
| batch01 | 1 | 5026a727fa2cafe6ceedf499f24a5196e4b9ca7a |
| batch02 | 247 | d3daa579d404db03654de989a338626088a30395 |
| batch03 | 510 | afb158467b7535010a8983b62f0121db2de480a4 |
| batch04 | 408 | 8b0947731e4811f2a89380df9f5ebd63a50601a4 |
| **Total** | **1166** | |

- تمت قراءة كل CSV وتحليل الاقتباس والفواصل والسطر/الجزء؛ جميع مفاتيح source_file + source_line عددها **1166 فريدًا**، ولم يُلاحظ تكرار بين الدفعات.
- batch01 يستخدم اسم مصدر يبدأ gor3a/، وحقول issue_type/reason بدل detected_conflict؛ يجب تطبيع هذا الاختلاف قبل أي تجميع آلي جديد.
- تقرير المنشأ وثّق 1,194 إشارة اشتباه موزعة: **371** تعارض نوع/سرعات ناقل، **81** تعارض سعة، **742** فرق قدرة >=20HP. هذه مؤشرات متداخلة وليست تقسيمًا حصريًا للصفوف، ولذلك لا تُساوى أعدادها بصفوف 1166.
- تصنيف أولي غير نهائي حسب **النص الرئيسي لوصف التعارض الواحد** (exclusive heuristic على حقل reason/detected_conflict): gear=360, power=741, displacement=65، مجموعها 1166. هذه ليست أعدادًا بديلة عن 371/742/81، لأنها لا تحسب اختلافات إضافية في الصف الواحد.

## تمركز حالات المراجعة (بعد قراءة جميع الملفات)
أكثر عشر شركات حسب مفاتيح صفوف الـ1166:
Toyota 89; Mercedes-Benz 83; Audi 69; BMW 69; Volkswagen 56; Ford 48; Peugeot 46; Lexus 41; Hyundai 40; Opel 32.
هذا ترتيب **مؤشرات مصدرية** فقط وليس ترتيب جودة سيارات أو شركات.

## عينات تحقق مباشرة من صفوف الخام
1. engines_part_005.csv:11 Dacia Duster 1.6 FHEV, label 140HP vs structured 94HP; fuel Hybrid Gasoline; **احتمال اختلاف قدرة النظام الهجين عن قدرة محرك البنزين** ولا يجوز تسميته خطأ مثبتًا.
2. engines_part_004.csv:1844 Dacia Bigster 1.8 hybrid label 156HP vs structured 109HP، بحاجة لفصل system/ICE output.
3. engines_part_012.csv:51 Opel Corsa 1.2 MHEV 6AT in label versus structured 8-speed automatic plus power 110/100; gearbox variant/market and power units require OEM validation.
4. engines_part_001.csv:489 Alfa Romeo MiTo 1.4 Turbo MultiAir 6AT vs structured 6-speed manual; same gear count but different gearbox architecture.
5. engines_part_005.csv:163 Dacia Sandero Stepway dCi label 5MT vs structured 5-speed automatic.
6. engines_part_001.csv:55 Acura MDX Hybrid label 321HP vs engine structured 260HP, possible hybrid system-vs-engine confusion.
These six examples were checked against corresponding original engine rows, without applying technical corrections.

## حفظ البيانات وأولوية الاستكمال
previous_conflict_queue=1166
recovered_and_unique_key_verified=1166
newly_OEM_verified_conflict_corrections=0
duplicates_removed=0
master_vehicle_rows_modified=0
approved_ECU_DTC_links=0
next_batch=88
next_workstream=OEM_CHECK_POWER_AGGREGATION_AND_TRANSMISSION_TYPE_FOR_DACIA_AND_OPEL_ALFA_CASES; CLASSIFY_HYBRID_POWER_CONFUSION_WITHOUT_AUTOMATIC_CORRECTION

## حماية
لم تُغيّر قوائم التعارضات الأصلية أو أي gor3a CSV، ولم تُمس main أو stable أو ملفات DTC المعتمدة أو الموقع أو Windows RC3.8.0/RC3.8.2 أو الصور.
