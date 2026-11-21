# DTC NEXIS — الدفعة 44: Morris / NIO / Nissan / Noble / Oldsmobile / Opel / Peugeot / Plymouth / Polaris (30 حالة)

date=2026-11-21 | REVIEW_ONLY / NOT_OEM_VERIFIED / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/MISSING_TRANSMISSION_MORRIS_BATCH43_AR.md
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
raw_sources=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_011.csv;data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_012.csv

## نطاق مفصل
- part_011: Morris 788–800 (13)، NIO 805 (1)، Nissan 978/1301/1346/1379 (4)، Noble 1529–1530 (2)، Oldsmobile 1544 (1)، Opel 1599 (1) = 22.
- part_012: Opel Corsa 58 وGrandland 216 (2)، Peugeot 3008 1190–1191 (2)، Plymouth Voyager 1912 و1917–1918 (3)، Polaris General 1919 (1) = 8.
- 30 حالة في قائمة OTHER تمت مطابقتها مباشرة مع صفوف CSV الخام. لا اعتماد ناقل OEM ولا استيراد بيانات إلى المكتبة المعتمدة.

## الملاحظات المعلقة
- Morris Minor Tourer (788) 847cc، Traveller (789–790) 1089/1098cc، Van 791 1098cc؛ Oxford (792–794) 1477/1489/1939cc، Oxford Series VI (795) 1622cc مع سنة بداية خام 1953 تحتاج مطابقة الجيل؛ Saloon/Ten/Traveller (796–800) 918/1098/1292/1140cc. تبقى فروق السنة والسعة قائمة دون حذف أو تطبيع قسري.
- NIO EP9 (805) 2016 Electric 4WD/1360HP؛ وحدة اختزال/قيادة غير موثقة.
- Nissan Elgrand (978) 2025 Hybrid Gasoline 1498cc AWD؛ Qashqai (1301) 2021 e-Power مع fuel Electric لكن 1461cc، يجب التحقق من وصف الطاقة والوقود والمولّد؛ Rogue (1346) 2020 1.5 V-Turbo FWD، وSerena (1379) e-Power مع fuel Mild Hybrid و1198cc، جميعها تحتاج مصدر تطبيق مصنع.
- Noble M600 (1529–1530) 2014 بسعتين 4144/4414cc؛ لا يثبت تشابه الاسم نفس منظومة النقل.
- Oldsmobile Toronado (1544) 1985 3785cc؛ لا تعيين ناقل من محرك فقط.
- Opel Astra (1599) 2021 وصف 165kW/225HP لكن fuel Diesel، دون سعة؛ تناقض محتمل هوية نسخة ووقود. Corsa (58) 2019 Electric 100kW، Grandland GSe (216) 2021 PHEV 1.6L AWD/300HP؛ تختلف المنظومات ولا يُستنتج ناقل منهما.
- Peugeot 3008 2020 (1190–1191) Hybrid Gasoline 1598cc، 225/300 e-EAT8 في نص المحرك؛ لفظ e-EAT8 وحده لا يثبت الكود المصنعي والتطبيق والبرمجية الدقيقة.
- Plymouth Voyager 1912 (1990) AWD 2.5L مقابل Voyager 1917–1918 (1984) FWD 2.5/3.0 V6؛ لا قياس ناقل عبر الجيل أو الدفع.
- Polaris GENERAL (1919) 2019، 999cc؛ يحتاج مرجعًا مؤهلًا لناقل الدفع وطراز المركبة.

## نتيجة الدفعة
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_44=889
last_examined=engines_part_012.csv:1919
next_record=engines_part_012.csv:1920 (confirmed queue)
remaining_OTHER_unreviewed_based_on_initial_1162=273

## الحدود
- المراجعة للبيانات الخام وقائمة النواقص فقط، وليست شهادة OEM. دون مساس بـmain أو stable أو CSV المصدر أو الموقع أو البرنامج أو الصور أو مكتبة DTC المعتمدة.
