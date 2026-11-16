# Infiniti — Batch04 — Q50 2016 V37 ECU Index (2026-11-16)

## تنفيذ فعلي
أُنشئ ملف `data/master/brands/infiniti_batch04_q50_2016_ecu_indexes_20261116.json` على فرع `data/infiniti-dtc-20261116-batch03`.

| النظام | عدد رموز DTC الأصلية الجديدة |
|---|---:|
| BCM / Body | 44 |
| ANC / Multimedia and CAN | 12 |
| SRS / Airbag failure-type variants | 44 |
| Chassis Control / Active suspension & ADAS | 54 |
| **الإجمالي** | **154** |

كل السجلات تتضمن وحدة ECU، الرمز الكامل والرمز الأساسي، الترجمة العربية والعنوان الإنجليزي القصير كما يعرضه الفهرس، سنة الموديل 2016، حالة تجهيزات السيارة غير المحققة، رابط القسم والتوثيق، ووضع اعتماد تشخيصي مقيَّد.

## مقارنة الدفعات
- Batch02 المحلي: 65 كوداً.
- Batch03: 5 أكواد OEM موثقة بنشرات خاصة = 70 رمزاً بعد الدفعتين.
- Batch04: 154 رمزاً نصياً/لاحقة جديدة، **غير متكررة مع الدفعتين** بعد مقارنة قائمة الأكواد.
- الإجمالي المرحلي **224 رمزاً** بين Batch02 وBatch03 وBatch04؛ العدد لا يعني 224 عطل سيارة مؤكداً ولا ضمان التغطية الشاملة.
- حالة مراجعة سابقة Batch03: 14 حالة. حالات Batch04: 154 معلومة تشخيصية ناقصة، المجموع الحالي = 168 حالة مؤجلة (قد تتضمن رموزاً سبق وجودها في Draft منفصل لم تتوفر بايتاته).

## جودة البيانات
- التحقق الفني يثبت ظهور الرمز والنص المختصر في DTC Index، **وليس** اكتمال طريقة اكتشافه أو تشخيصه.
- قيم مطابقة دقيقة فقط حيث قرئت تفاصيلها: B2562 جهد BCM أدنى من 8.8 V لمدة 120 ثانية، B259A فيوز 20 بقيمة 10A وجهد M17/131 = 9–16 V؛ تستعمل فقط على Q50 2016 بشرط تطابق النسخة.
- وحدات SRS: منع اختبار الدوائر بمقياس مقاومة عام؛ يلزم CONSULT واتباع تعليمات العزل المعتمدة.
- لم تُفترض مواقع القطع ولا أرقام ECU أو المحركات أو أسلاك المركبات الأخرى.
- لا صور جديدة ولا نسخ للمخططات المحمية.

## المراجع
- BCS: https://www.nicoclub.com/service-manual?fsm_download=Q50%2F2016+Q50%2Fbcs-body_control_system.pdf
- AV: https://www.nicoclub.com/service-manual?fsm_download=Q50%2F2016+Q50%2Fav-audio_visual_navigation_system.pdf
- SRC: https://www.nicoclub.com/service-manual?fsm_download=Q50%2F2016+Q50%2Fsrc-srs_airbag_control_system.pdf
- SCS: https://www.nicoclub.com/service-manual?fsm_download=Q50%2F2016+Q50%2Fscs-suspension_control_system.pdf
- FWD: https://www.nicoclub.com/service-manual?fsm_download=Q50%2F2016+Q50%2Ffwd-quick_reference_index.pdf

لا دمج إلى main ولا تعديل RC3.8.0 / RC3.8.2 ولا قناة التحديث. مراجعة المالك مطلوبة.
