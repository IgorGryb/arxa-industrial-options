# ARXA — karta systemu decyzyjnego

ID: `PXP-PRJ-ARXA`  
Status: prywatne studium decyzji przemysłowej z ograniczonymi scenariuszami; nie wdrożona platforma ani rekomendacja operacyjna.

## Znaczenie dla decyzji

ARXA bada, czy sygnał danych poprawia wykonalną decyzję o interwencji i
etapowaniu inwestycji po uwzględnieniu capacity, downtime, jakości danych,
kosztu, finansowania i błędów. Główny wektor: aktywa/infrastruktura/technologia;
wzmacniające: kapitał/ryzyko, dane/dowód oraz operacje/produkt.

## Mapa systemu

`data signal → confidence/quality → feasible action → capacity and downtime →
operating cost → staged capital decision → governance review`.

## Dowód i wkład

Pakiet dokumentuje model danych, scenariusze, metryki, model ekonomiczny,
ograniczenia i dossier. Wkład polega na połączeniu predykcji z konkretną akcją
oraz jej warunkami wykonania, a nie na deklarowaniu samej predykcji jako wartości.

## Model i hipoteza integracji

Mechanizm porównuje fixed rule, forecast-only rule oraz action constrained by
cost/capacity. Hipoteza: lepsza metryka predykcji może nie poprawić decyzji,
jeżeli ograniczenia działania, false positives albo distribution shift odwracają
wynik. Koszt integracji i data quality są częścią rekomendacji.

## Test i następna opcja

Najtańszy test uruchamia te trzy reguły na identycznych przypadkach z
degradacją danych. Następna opcja to lokalny brief aktywa dopiero po ujawnieniu
ownerów, capacity, danych i granicy decyzji.

## Rdzeń biznesowy i standard architektury

**Wizja ze źródła (koncepcja historyczna):** An industrial-intelligence and supply-chain coordination venture linking operational data to production, sourcing and capital decisions.

**Pierwsze ograniczone zastosowanie:** One asset and failure mode: compare scheduled maintenance, a forecast-only rule and a cost/capacity-constrained intervention before staging capital.

**Model komercyjny (hipoteza):** A business-to-business subscription for industrial decision support, with onboarding and data-integration cost modeled separately; buyer, price and demand are unvalidated.

**Jednostki i czynniki ekonomiczne:** expected downtime and failure loss; intervention and false-alarm cost; capacity and inventory; data and integration cost; staged capex and financing.

**Wykonany zakres:** A small Python reference model on synthetic industrial scenarios; it does not ingest live plant telemetry.

**Architektura referencyjna (projekt, bez wdrożenia):** Operational data ingestion, schema and quality controls, analytics, scenario models, enterprise-system interfaces, access control and monitoring.

**Opcje odroczone:** Live ERP/MES/IoT integration, multi-party orchestration, autonomous agents, blockchain contracts and production rollout.

| Model | Zastosowanie w tym przypadku |
|---|---|
| Techniczny | Controlled operational-data pipeline and scenario model with declared data-quality limits. |
| Biznesowy i produktowy | Industrial decision-support subscription hypothesis anchored in a single asset use case. |
| Operacyjny | Maintenance owner controls action capacity, handoffs, intervention and exception escalation. |
| Finansowy | Compare avoided loss with intervention, integration, operating and staged-capital costs. |
| Ryzyko i governance | Stress missing or degraded data, false alarms, funding and human override. |

**Źródła rozwoju:** IBM — IBM Data Architecture (`recorded_completed`); Microsoft — Microsoft Data Architecture for Modern Data Stacks (`recorded_completed`); Johns Hopkins University — Advanced Statistics for Data Science (`recorded_completed`); Corporate Finance Institute (CFI) — Valuation Modeling (`recorded_completed`); Columbia University — Financial Engineering and Risk Management (`recorded_completed`). Są to odnotowane ukończenia programów i kandydackie połączenia zastosowań; nie stanowią samodzielnego dowodu wdrożenia lub biegłości. **Metody z zapisanym zakresem odczytu:** `M-SIPOC`, `M-RACI`, `M-FEASIBILITY`, `M-SCENARIO`, `M-MEASURE`.

## Granice i źródła

Nie deklarować industrial deployment, predictive maintenance outcome,
engineering authority ani zrealizowanej ekonomiki. Źródła: [dossier zarządcze](MANAGEMENT-DOSSIER.md),
[validation memo](MODEL-VALIDATION-MEMO.md), [data card](DATA-CARD.md) i
[rejestr pozycji](../../../00.%20ARCHIVE%20SYSTEM/portfolio/CONVEX-POSITION-REGISTER.yaml).
