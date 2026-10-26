# ARXA — validation and decision memo

Private synthetic study. Eight repository tests; twelve efficacy/capacity scenarios.

| Efficacy | Capacity | Cost | Actions | Residual failures |
|---:|---:|---:|---:|---:|
| 0 | 0 | 540000 | 0 | 6 |
| 0 | 2 | 584000 | 2 | 6 |
| 0 | 10 | 760000 | 10 | 6 |
| 0 | unlimited | 1024000 | 22 | 6 |
| 0.5 | 0 | 540000 | 0 | 6 |
| 0.5 | 2 | 584000 | 2 | 6.0 |
| 0.5 | 10 | 670000 | 10 | 5.0 |
| 0.5 | unlimited | 754000 | 22 | 3.0 |
| 1 | 0 | 540000 | 0 | 6 |
| 1 | 2 | 584000 | 2 | 6 |
| 1 | 10 | 580000 | 10 | 4 |
| 1 | unlimited | 484000 | 22 | 0 |

No-intervention baseline cost: 540000. Synthetic technical cost units; not the EUR/period management case.
Rolling index MAE: 0.039256; degraded-input MAE: 0.039728. This predicts an engineered index, not calibrated failure probability.

## Decision and forecast interpretation

The original favorable-policy forecast holds only under its selected perfect-efficacy assumptions. Zero efficacy reverses the advantage; zero capacity reproduces no intervention. Preserve the negative result instead of presenting only the favorable scenario.
The separate pre-recorded management-cost example is 180 versus 380 EUR/period at residual failure probabilities 0.10 and 0.30. This arithmetic does not identify treatment benefit.
Continue a narrowly scoped decision study. Pause an operating recommendation until data quality, failure labels, efficacy and available intervention resources are established. A staged capital commitment requires a separate cash-flow and financing model.

## Post-mortem

Removed the misleading option_value field: an absolute cost difference is not a real-option price. Added efficacy/capacity scenarios and rejected prediction-length mismatch instead of silently truncating observations. Costs, scores and probabilities retain distinct meanings.
Handoff: DELIVERY-SPECIFICATION.md, tests and artifacts/management-review.json. No real asset, customer, industrial saving or production integration is claimed.
