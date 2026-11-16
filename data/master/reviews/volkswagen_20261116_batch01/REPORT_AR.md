# Volkswagen 2026-11-16 — OEM bulletin evidence (unreleased)

Source baseline: VW022 1699 mixed records, including 644 legacy VAG candidate records. Existing VW002 and all four master enrichment parts remain unchanged.

New source-context records: 45, distributed {"P":16,"U":14,"B":11,"C":4}. Individual full code+ECU+bulletin+symptom combinations unique: 45. None added by rewriting the 644 candidate rows.

Sources: 2073355/2 (2024-04-25) https://static.nhtsa.gov/odi/tsbs/2024/MC-10253931-0001.pdf; 2071701/2 (2024-02-07) https://static.nhtsa.gov/odi/tsbs/2024/MC-10250289-0001.pdf; 2061220/7 (2023-01-09) https://static.nhtsa.gov/odi/tsbs/2023/MC-10230571-0001.pdf; 2035369/2 (2023-08-03) https://static.nhtsa.gov/odi/tsbs/2023/MC-10241183-0001.pdf.

Scope: ID.4 2024 Chattanooga J533 SW0411 (benign-only combinations); ID.4 2022 campaign-gated JX4; Atlas / Cross Sport SRS VIN-scoped; Jetta GLI / Passat 2012–2014 SRS. US scopes do not prove Swedish or European applicability.

Deferred review: 45 context entries because diagnostic thresholds, EU fitment, parts, wiring or reuse rights are not verified. Exact source-context matches not merged across different ECU/symptom codes.

This changes **only the independent data library on a separate branch**, NOT the installer, signed feeds or stable application. Main unchanged until owner review.
