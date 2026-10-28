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

## Granice i źródła

Nie deklarować industrial deployment, predictive maintenance outcome,
engineering authority ani zrealizowanej ekonomiki. Źródła: [dossier zarządcze](MANAGEMENT-DOSSIER.md),
[validation memo](MODEL-VALIDATION-MEMO.md), [data card](DATA-CARD.md) i
[rejestr pozycji](../../../00.%20ARCHIVE%20SYSTEM/portfolio/CONVEX-POSITION-REGISTER.yaml).
