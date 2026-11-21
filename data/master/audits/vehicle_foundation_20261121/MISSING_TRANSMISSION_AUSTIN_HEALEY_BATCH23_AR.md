# DTC NEXIS — الدفعة 23: Austin Healey 923–952، فحص اختلافات السعة والتسمية

date=2026-11-21 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
base_commit=64bbb6570642494a0b51550bf8f76ed553f826ee
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
raw_source=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_002.csv

## مطابقة المصدر
- فُحصت 30 حالة متتالية من قائمة OTHER (صفوف المصدر 923–952). تمت مقارنة هوية الماركة/الموديل/السنة/وصف المحرك مع القائمة، وقرئت السعة الدقيقة وbody_type من CSV الخام.
- كل الصفوف لا تحمل وصف ناقل الحركة، وتبقى NOT_OEM_VERIFIED. لا يكفي تشابه الاسم أو السعة لاستخلاص رمز OEM.
- حالات مصدرية ذات اختلافات أو احتمال التباس، وليست أحكامًا فنية على السيارة.

## نقاط التدقيق
- 923–924: HEALEY 100-6 / 1956 / 2.6L: 2600 مقابل 2639cc، اختلاف سعة؛ لا يُدمجان حرفيًا.
- 925–927: HEALEY 100/6 / 1956: 3500 و2639 و2912cc. «100/6» مقابل «100-6» قد يكون اختلاف كتابة لكن لا يُدمج دون سند عن الموديل والمحرك والسوق. 3500cc شذوذ ذو أولوية.
- 928–930: HEALEY 3000 / 1957: 2908 و3000 و2912cc. احتفظ بفرق السعة مع ضرورة مراجعة سنة الجيل.
- 931–936: «HEALEY 3000 MK 11» مقابل «MK 111»: أسماء يحتمل فيها استبدال الأرقام الرومانية بالحرفي 11/111؛ هناك 2912/2910/3000cc لكل مجموعة. لا توحيد تلقائي.
- 937–944: تنويعات «MK I», «MK II», «MK III», «MK3», «MKII», «MKIII». سعات 2912/2922/3000cc وسنوات مسجلة مختلفة (1959/1962/1964). يُحفظ اختلاف السنة والنص كاملًا إلى حين توثيق اسم الجيل والسوق. body_type «Niet geregistreerd» في الصف 938 ليس تأكيدًا لشكل الهيكل.
- 945–952: HEALEY SPRITE / 1958 سعات 1098,1298,984,950,948,3523,803cc بالإضافة إلى «SPRITE MK 1» 948cc. **صف 950 (3.5L/3523cc)** شذوذ عالي الأولوية، والصف 951 (803cc) يستلزم إثبات انطباقه؛ لا حذف ولا تصحيح آلي.

## حالة الدفعة
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_23=302
last_examined=engines_part_002.csv:952
next_record=first queue entry following engines_part_002.csv:952 (read queue)

## قيود القبول
- يلزم دليل مصنعي أو كتالوج قطع مؤهل لكل تطابق (الموديل، الجيل، السنة، السوق، المحرك، رمز ناقل الحركة). لا يُعتبر هذا التقرير مرجعًا لإضافة ECU/DTC إلى المكتبة المعتمدة.
- لا تغييرات على main أو الموقع أو Windows أو قنوات تحديث stable أو ملفات المصدر الأصلية أو الوسائط.
