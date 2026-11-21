# DTC NEXIS — الدفعة 67: تدقيق Hyundai i20 وi20 Active (2018)

date=2026-11-21 | REVIEW_ONLY / OEM_SOURCE_SCOPE_CHECK / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_SCOPE_RECHECK_BATCH66_AR.md
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_32_prioritized_batch02.csv

## الحالات
- engines_part_007.csv:834 Hyundai i20 (2018–2020) 1.2L 5MT FWD (75 HP)
- engines_part_007.csv:865 Hyundai i20 Active (2018–2020) 1.2L 5MT FWD (75 HP)
- engines_part_007.csv:866 Hyundai i20 Active (2018–2020) 1.2L 5MT FWD (84 HP)

## المراجع الأصلية والنتائج
1. Hyundai France، ملف إطلاق New i20 2018: تؤكد الشركة محرك 1.2L بقوتي 75 و84 ch مع ناقل يدوي 5 سرعات في **i20 5-door** صراحة. هذا دليل عائلة للموديل i20 وليس إثباتًا لكل الأسواق أو الأرقام المصنعية للناقل.
   https://www.hyundai.news/fr/archives-du-dossier-de-presse/i20-2018/dossier-de-presse-nouvelle-i20.html
2. Hyundai Poland، ملف i20 2018: يذكر محرك 1.2 بقوتي 75 و84 KM مع ناقل 5 سرعات، لكن يخص i20. ويرد **i20 Active 1.4 / 100 KM مع يدوي 6 سرعات** في عرضه الإقليمي. لا يثبت ذلك استحالة توافر 1.2 Active في كل سوق؛ لكنه قرينة على خطر نقل وصف i20 العادية إلى Active.
   https://www.hyundai.news/pl/archiwum-materialow-prasowych/i20-2018/nowy-hyundai-i20-atrakcyjna-stylistyka-i-bezpieczenstwo.html
3. Hyundai UK، إعلان 2018 عن i20 5-door 1.2 / 84PS و5MT؛ هذا سند مستقل للهيكل 5 أبواب، لا i20 Active:
   https://www.hyundai.news/uk/articles/press-releases/hyundai-motor-uk-announces-new-i20-5-door-pricing-and-specifications.html

## الحكم لكل صف
- 834: OEM_5MT_MODEL_VARIANT_LEAD / MARKET_AND_OEM_GEARBOX_CODE_NOT_ESTABLISHED / NOT_APPROVED.
- 865: BODY_VARIANT_APPLICABILITY_CONFLICT / NO_DIRECT_1_2_ACTIVE_OEM_MATCH / NOT_APPROVED.
- 866: BODY_VARIANT_APPLICABILITY_CONFLICT / NO_DIRECT_1_2_ACTIVE_OEM_MATCH / NOT_APPROVED.
- لا تستبدل i20 Active بمحرك 1.4 أو 6MT تلقائيًا، ولا تحذف صفوف 1.2؛ المطلوب توثيق سوق/رمز المحرك/صندوق ناقل i20 Active حسب سنة الصنع.

## حصيلة الدفعة
existing_hint_cases_reexamined=3
new_confirmed_OEM_gearbox_code_assignments=0
new_ECU_DTC_links=0
new_raw_vehicle_imports=0
records_remaining_not_OEM_approved=32
raw_records_modified=0
next_workstream=OTHER_UNVERIFIED_HINT_OEM_MARKET_YEAR_DIAGNOSTICS

## حماية
لا تغيير لـmain أو stable أو المصدر الخام أو بيانات الموقع/Windows أو الصور أو المكتبة المعتمدة. هذا ملحق مراجعة للمراجع السابقة، وليس تحديثًا مثبتًا لمواصفات السيارة.
