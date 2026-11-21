# DTC NEXIS — الدفعة 39: Ligier / Lucid / Maserati / Maxus / McLaren / Mercedes-AMG / Mercedes-Benz (30 حالة)

date=2026-11-21 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/MISSING_TRANSMISSION_LIGIER_BATCH38_AR.md
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
raw_sources=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_008.csv;data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_009.csv

## النطاق
- part_008: Ligier 1626–1631 (6)، Lucid 1839–1843 (5)، Maserati 1896 و1930–1931 (3)، Maxus 1961 و1966 (2) = 16.
- part_009: McLaren 502 (1)، Mercedes-AMG 566–570 (5)، Mercedes-Benz 676–681 (6) و823–824 (2) = 14.
- فُحصت هوية جميع الحالات الثلاثين وحقول المحرك والسعة والوقود من CSV الخام، مع تأكيد أنها في قائمة OTHER ولا تملك رمز ناقل مثبتًا.

## فروق وتحذيرات
- Ligier XTOO R DCI/RS/RS DCI/S 2008–2009 (1626–1631): 440/500/505cc؛ لا دمج لتقارب السعات، ولا تحويل DCI إلى مواصفة ناقل.
- Lucid Motors Air (1839–1842): Dream Edition Performance/Range وGrand Touring/Touring، 1111/933/800/620HP، وكلها Electric AWD بحسب النص؛ لا تخمين نسبة الاختزال أو كود وحدة الدفع. Lucid Motors Gravity (1843) 800HP Electric، تسمية «Motors Gravity» تحتاج مطابقة الهوية.
- Maserati GranCabrio (1896) 2024 V6 RWD 542HP، MCPura وMCPura Cielo 2025 (1930–1931) V6 3000cc 630HP؛ لا تفرض ناقل أي نسخة على الأخرى.
- Maxus DELIVER 9 (1961) Diesel 1996cc مقابل EDELIVER 9 (1966) 1996cc وحقل وقود فارغ رغم حرف E؛ احتمال خلط نوع منظومة الدفع/السعة، ولا يتم تصحيحه آليًا.
- McLaren Senna (502) 2018، 3999cc V8/800HP؛ لا يعتمد رقم ناقل دون OEM.
- Mercedes-AMG EQE (566–568): Electric بقيم 350/505/460 kW، وإصدارات EQE SUV (569–570) 43/53 بقيم 476/626HP وحقل fuel يصرّح Plug-in Hybrid؛ تناقض ظاهري يستلزم تحققًا مصنعيًا قبل قبول تصنيف منظومة الدفع.
- Mercedes-Benz A-Klasse (676–681): محركات 180/200 بنزين 1332cc، 220 4MATIC بنزين 1991cc، 180d/200d/220d ديزل 1950cc؛ الصياغة الخام «220 d ((190 HP)» خطأ نصي محتمل يستلزم مراجعة دون تعديل.
- Mercedes-Benz A-Klasse Saloon (823–824): 180 و200 بنزين 1332cc، ومختلفة عن جسم hatchback؛ لا افتراض تماثل ناقل بين الهيكلين.

## النتائج
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_39=739
last_examined=engines_part_009.csv:824
next_record=engines_part_009.csv:825 (confirmed queue)
remaining_OTHER_unreviewed_based_on_initial_1162=423

## الحماية
- البيانات وصف مصدر، وليست إثبات OEM لأي وحدة ناقل أو ECU أو DTC.
- لا تغيير للأصول الخام أو main أو stable أو المكتبة المعتمدة أو الوسائط أو الموقع أو برنامج Windows.
