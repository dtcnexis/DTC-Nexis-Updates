# DTC NEXIS — الدفعة 37: Honda / Hyundai / Jaecoo / Jeep / Karma / Kia / Lancia / Land Rover / Lexus / Ligier

date=2026-11-21 | REVIEW_ONLY / NO_OEM_APPROVAL / NOT_PUBLISHED
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/MISSING_TRANSMISSION_GEO_HONDA_BATCH36_AR.md
source_queue=data/master/reviews/vehicle_catalog_full_20261118/review_queue/missing_transmission_no_hint_other_batch01.csv
raw_sources=data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_007.csv;data/master/reviews/vehicle_catalog_full_20261118/gor3a/engines_part_008.csv

## نطاق الفحص (30 إدخالًا مطابقًا للقائمة)
- part_007: Honda Jazz/Fit 425 (1)، Hyundai Mistra 1167 (1)، Jaecoo 1624–1630 (7)، المجموع 9.
- part_008: Jeep Wrangler 98–99 (2)، Karma 146–147 (2)، Kia Soul 645 وXCeed 789–790 (3)، Lancia 944 و1015 (2)، Land Rover 1336 (1)، Lexus 1430 و1584 (2)، Ligier 1587–1595 (9)، المجموع 21.
- تحقق تطابق الصفوف مع CSV الخام والتسلسل الفعلي لقائمة OTHER. الصفوف 1585–1586 (Lightyear) ليست من هذه القائمة ولم تُحسب.

## الحالات الفنية المؤجلة
- Honda Jazz / Fit 2020 (425): 1496cc، 98HP Hybrid مع FWD؛ صف AWD 424 السابق مختلف، ولم يتحقق رمز ناقل أي منهما.
- Hyundai Mistra 2014–2017 (1167): 2.0L بنزين، 2000cc؛ الناقل غير محدد.
- Jaecoo (1624–1630): أسماء 7 PHEV/J7 PHEV/J8 PHEV/JAECOO5 HYBRID/JAECOO7/JAECOO7 PHEV/JAECOO8 PHEV وسنوات 2025–2026، كلها 1499cc بحسب المصدر؛ حقل الوقود الخام فارغ رغم لفظ HYBRID/PHEV في الاسم. لا تُثبت الأسماء نظام الدفع أو ناقله أو تطابق الهوية؛ أشكال الهيكل MPV/hatchback تحتاج مراجعة.
- Jeep Wrangler 2023 (98–99): محرك 2.0L أربع أسطوانات مقابل 3.6L V6، ونص AWD، ولا رموز ناقل مصنعية.
- Karma Revero GT 2019 (146): Hybrid 1998cc/403HP؛ Revero GTS 2019 (147): Electric في خانة الوقود مع 1499cc و3 أسطوانات وقدرة 536HP. تعارض كون GTS كهربائية مع حقول محرك الاحتراق يستدعي مرجعًا فنيًا مستقلًا.
- Kia Soul 2022 (645): 2.0L/145HP Gasoline، وKia XCeed 2022–2026 (789–790) 1.0 T-GDi/118HP مقابل 1.5 T-GDi/158HP؛ لا تأكيد لناقل كل خيار.
- Lancia Beta (944): سنة البداية والنهاية في المصدر 1909، 3119cc؛ لا يُصحح التاريخ تلقائيًا، والتحقق من الهوية والجيل أولوية. Lancia Flavia Convertible (1015): 1960–1967، 1488cc؛ الناقل غير معروف.
- Land Rover Range Rover Sport 2019–2022 (1336): 2995cc/V6/400HP، AWD؛ رقم الناقل غير مثبت.
- Lexus GX 2019–2023 (1430): وصف 4.6L V8 لكن حقل الأسطوانات الخام 6؛ تعارض مصدر يتطلب OEM. Lexus UX 300e 2018–2023 (1584): Electric مع حقل الأسطوانات 4 وdrivetrain AWD؛ احتمال خلط وحدات محرك كهربائي/حراري يستلزم تحققًا.
- Ligier 162 Ambra/BE UP/IXO/IXO DCI/JS162/JS20 (1587–1595): 1995–2010، سعات 440/480/505cc رغم تسميات 0.4L/0.5L، ولا وصف ناقل؛ لا دمج لاختلافات السعة أو الأجيال، و«Niet geregistreerd» ليس هيكلًا موثقًا.

## النتائج
existing_records_examined=30
records_deferred=30
new_imports=0
full_OEM_approvals=0
confirmed_exact_duplicate_deletions=0
raw_rows_modified=0
cumulative_OTHER_records_reviewed_batches_11_to_37=679
last_examined=engines_part_008.csv:1595
next_record=engines_part_008.csv:1596 (confirmed queue)
remaining_OTHER_unreviewed_based_on_initial_1162=483

## الضوابط
- تدقيق المصدر وقائمة النواقص فقط؛ لا يعتبر اعتمادًا فنيًا OEM أو روابط جديدة ECU/DTC.
- لم تُعدل الملفات الخام أو main أو stable أو الموقع أو Windows أو الصور أو الأكواد المعتمدة.
