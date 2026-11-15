# BMW DTC review queue — 2026-11-16

Status: draft / not published. This branch is isolated from main and release channels.

Source inventory: BMW_DTC_NEXIS_batch01.json (98 records, 97 distinct codes), BMW_DTC_NEXIS_expansion_batch02_review.json, and previous BMW draft exports.

Prior status labels: 88 "قيد التوثيق", 10 "مكتمل". All 98 require independent source and applicability revalidation before insertion into data/master.

Blocked: data/master is a directory; its full inventory and deduplication schema were not retrieved. No validated new BMW codes were added to the master library.

Review priorities: BMW manufacturer code variants, engine/ECU-specific meanings, N20/N26 VANOS bulletin applicability, DME/DDE, EGS, FEM/BDC/CAS, DSC/ABS, ACSM and CAN network codes.

Do not merge or publish without technical review. Original local batch files must be preserved separately.
