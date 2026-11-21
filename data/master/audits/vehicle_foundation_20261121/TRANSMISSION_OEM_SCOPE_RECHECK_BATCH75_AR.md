# DTC NEXIS — الدفعة 75: Subaru Ascent / Ford Transit Connect / Toyota Corolla identity

date=2026-11-21
status=REVIEW_ONLY / OEM_FAMILY_EVIDENCE / NO_MASTER_IMPORT / NO_RELEASE
branch=review/vehicle-foundation-audit-20261118
previous_checkpoint=data/master/audits/vehicle_foundation_20261121/TRANSMISSION_OEM_VALIDATION_CHECKPOINT_BATCH74_AR.md

## مطابقة المصدر
- Subaru engines_part_015.csv:43, Ascent (2022), 2.4L CVT AWD (260 HP), source Git blob 6ec436f6414f8d5557c6171555ed402fb0a11f36.
- Ford engines_part_006.csv:1276, Transit Connect Wagon (2018), raw combined years 2018–2023, 2.0L GDI 8AT (150 HP), source Git blob 2622eaa2d8a10316d2e7a9561d3182061f51ffce.
- Toyota engines_part_015.csv:1004 and :1005, Corolla Sedan (2022), Hybrid Gasoline 1.8L CVT FWD (140 HP) / 2.0L CVT FWD (196 HP), source Git blob 6ec436f6414f8d5557c6171555ed402fb0a11f36.

## Subaru Ascent 2022 — وثيقة رسمية وتم التحقق بصريًا
- Subaru USA 2022 Ascent brochure, physical PDF page index 10 (printed p.19): lists Subaru Boxer 2.4L turbo 260 hp and **High Torque Lineartronic CVT** with eight-step manual-mode emulation and Symmetrical AWD.
- OEM_PDF_URL=https://www.subaru.com/content/dam/subaru/downloads/pdf/brochures/2022/ascent/2022_Ascent_Brochure_Final.pdf
- VERIFICATION=WEB_PDF_SCREENSHOT_PAGE_10_VERIFIED.
- Finding: strong same-model/year/engine-power/drive transmission family proof. The simulated eight steps are NOT a fixed 8AT. Transmission assembly ID, service gearbox model code, ECU/TCM identity and VIN applicability remain pending.
- decision=REVIEW_ONLY_OEM_FAMILY_CONFIRMED_NOT_FINAL_PART_CODE.

## Ford Transit Connect — 2018 vs 2019/2020
- Ford's 2018 US owner's manual mentions six-speed **6F35**. 2019 US manual pdf and 2020 US owner's manual mention eight-speed **8F35**. Some 2019 documentation describes both types, depending on configuration.
- OEM_2018=https://www.fordservicecontent.com/Ford_Content/vdirsnet/OwnerManual/Home/Content?ProcUid=G1708465&Uid=G1608812&buildtype=web&countryCode=USA&div=f&languageCode=en&userMarket=usa&vFilteringEnabled=False&variantid=6040
- OEM_2019_PDF=https://www.fordservicecontent.com/Ford_Content/Catalog/owner_information/2019-Ford-Transit-Connect-Owners-Manual-version-1_om_EN-US_05_2018.pdf
- OEM_2020=https://www.fordservicecontent.com/Ford_Content/vdirsnet/OwnerManual/Home/Content?ProcUid=G1965212&Uid=G1965211&buildtype=web&countryCode=USA&div=f&languageCode=en&moidRef=G1405423&userMarket=USA&vFilteringEnabled=False&variantid=7408
- Finding: raw combined 2018–2023 row cannot be granted one Ford gearbox ID globally; first subdivide by actual MY, trim, engine, VIN production date and market. Owner manual identifies transmission families but not exact vehicle match.
- decision=REVIEW_ONLY_MODEL_YEAR_SEGMENTATION_REQUIRED.

## Toyota Corolla hybrid family — same numerical fingerprint, body and MY gate
- Toyota Europe 2023 press release explicitly reports **140 DIN hp** for 1.8L and **196 DIN hp** for 2.0L fifth-generation hybrid Corolla, acceleration **9.2/7.5 seconds** respectively. The numeric pair exactly matches raw entries and acceleration, but 2023 Europe family is not proof of 2022 Sedan.
- OEM_MY2023=https://newsroom.toyota.eu/toyota-announces-the-new-2023-corolla/
- Toyota regional Spanish official information indicates **Corolla Sedan Hybrid 140H** is offered with one hybrid engine; the 2.0L 196CV is represented for other Corolla family bodies in contemporary releases.
- OEM_REGIONAL=https://newsroom.toyota.eu/novedades-en-la-familia-toyota-corolla/
- Finding: likely MY2023 hybrid engine data combined with MY2022 and incorrect Sedan body for 2.0L; this is a **plausible provenance hypothesis**, not a confirmed correction. Also do not confuse CVT vs e-CVT architecture.
- decision=REVIEW_ONLY_YEAR_BODY_AND_TRANSAXLE_ID_PENDING.

## نتائج الدفعة
existing_hint_cases_reexamined=4
new_approved_exact_gearbox_assignments=0
new_ECU_DTC_links=0
new_imports=0
source_rows_modified=0
remaining_hint_cases_without_exact_approved_gearbox=32
new_OEM_visual_PDF_validation=1
next_batch=76
next_workstream=REVIEW_UNRESOLVED_FULL_MARKET_FITMENT_AND_OEM_GEARBOX_IDENTIFIERS

## الحماية
No modifications to original gor3a CSV, prior review queues, main, stable, Windows RC3.8.0/RC3.8.2, website, images or approved DTC library.
