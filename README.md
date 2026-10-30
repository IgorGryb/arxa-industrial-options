# ARXA — Industrial Telemetry & Real-Options Operating Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![CI](https://github.com/IgorGryb/arxa-industrial-options/actions/workflows/ci.yml/badge.svg)](https://github.com/IgorGryb/arxa-industrial-options/actions)
[![Tests](https://img.shields.io/badge/Tests-Passing%20(8%2F8)-success.svg)](tests/)
[![Architecture](https://img.shields.io/badge/Architecture-Real--Options%20Lattice-orange.svg)](#solution--decision-architecture)
[![OpenAPI 3.1](https://img.shields.io/badge/OpenAPI-3.1%20Contract-green.svg)](api/openapi.yaml)
[![ADRs](https://img.shields.io/badge/ADR-Architecture%20Decisions-purple.svg)](docs/adr/)
[![Status](https://img.shields.io/badge/Status-R%26D%20Reference%20Architecture-informational.svg)](#research-integrity--disclaimer)

> **Architectural Mission:** Bridging industrial IoT sensor telemetry and executive capital allocation by embedding physical equipment degradation forecasting into a real-options decision lattice to optimize maintenance timing.

---

## Executive Overview

| Dimension | Specification |
|:---|:---|
| **Domain** | Industrial IoT, Predictive Asset Intelligence & Staged Capital Investment |
| **Stage** | Validated Proprietary Architecture & Decision Engine (R&D Prototype) |
| **Target User** | Industrial Asset Managers, Chief Operating Officers, Manufacturing VPs, Plant Directors |
| **Core Decision** | Determining optimal operational interventions and timing for staged equipment maintenance vs. replacement |
| **Key Metric** | Net Avoided Downtime Cost, Diagnostic Latency, Expected Option Value, Intervention ROI |
| **Architecture Lead** | Igor Grybek (Product Architecture, Operational Modeling, Venture Strategy) |

---

## The Strategic Problem

In heavy manufacturing, energy generation, and process industries, critical rotating machinery and production infrastructure represent significant capital investments. Unplanned asset failure results in catastrophic downtime costs, supply chain disruption, and secondary equipment damage.

However, existing industrial management practices fall into two inefficient extremes:
1. **Time-Based Preventative Maintenance:** Prematurely replaces components based on static manufacturer schedules, incurring unnecessary capex and halting production while substantial useful asset life remains.
2. **Alert-Driven Predictive Maintenance:** Floods maintenance teams with uncontextualized sensor anomaly alerts without evaluating whether taking a production line offline is economically justified relative to the failure probability and maintenance cost.

Industrial operators lack an integrated decision engine that evaluates **telemetry data quality, diagnostic latency, and operational intervention feasibility** within an explicit financial decision framework.

---

## Solution & Decision Architecture

ARXA bridges the gap between IoT sensor telemetry and executive capital allocation by embedding continuous physical monitoring into a real-options decision lattice.

```
[IoT Sensor Stream] ──► [Signal Quality & Noise Filter]
                                   │
                                   ▼
                   [State Estimation & RUL Model]
                                   │
                                   ▼
        [Operational Constraint Check: Capacity & Downtime]
                                   │
                                   ▼
        [Real-Options Lattice: Continue vs Intervene vs Upgrade]
                                   │
                     ┌─────────────┴─────────────┐
                     ▼                           ▼
          [Optimal Intervention]        [Continue Operation]
                     │                           │
                     ▼                           ▼
          [Staged Maintenance CAPEX]    [Monitor Next Interval]
```

### Core System Mechanics:
1. **Telemetry Ingestion & Quality Gating:** Ingests high-frequency sensor feeds (vibration spectra, thermal signatures, operational pressure) through rigorous data-quality filters, identifying sensor drift, missing packets, and noisy signals before triggering alerts.
2. **Probabilistic State & Remaining Useful Life (RUL):** Computes time-to-criticality distributions rather than point forecasts, reflecting operational uncertainty under varying production loads.
3. **Real-Options Decision Lattice:** Adapts the Columbia University real-options framework (binomial decision lattices with backward induction) to physical plant assets. In every operational interval, the engine compares:
   - *Continuation:* Operating with current equipment while holding the option to intervene later.
   - *Targeted Minor Maintenance:* Executing low-cost preventive servicing during scheduled downtime.
   - *Staged Major Overhaul / Replacement:* Committing substantial capital expenditure ($I_{\text{upgrade}}$) to upgrade the production unit and permanently increase throughput and reliability.
4. **Capacity & Commercial Constraint Integration:** Reconciles maintenance schedules with order backlogs, shift schedules, and electricity peak tariffs, ensuring that maintenance downtime is taken when revenue loss is minimized.

---

## 5-Dimensional Management Model

### 1. Technical Architecture
- **Signal Processing & ML:** Python (SciPy, PyWavelets, scikit-learn) for vibration spectral decomposition, feature extraction, and survival regression.
- **Option Solvers:** Dynamic programming algorithms and binomial trees modeling multi-stage American-style exercise decisions under operational stochasticity.
- **Time-Series Ingestion:** Event-driven architecture for distributed factory floor telemetry.

### 2. Operating Model & Maintenance Workflows
- **Shift Synchronization:** Automatically pairs maintenance intervention windows with scheduled production changeovers, preventing uncoordinated line stoppages.
- **RACI Matrix:** Defined roles separating Plant Reliability Engineers, Maintenance Supervisors, and Operations Finance Directors.

### 3. Financial & Unit Economics
- **Cost-Optimization:** Bounded modeling demonstrates that ARXA's constrained real-options policy reduces expected operational maintenance costs by 20–35% compared to static calendar maintenance.
- **Downtime Economics:** Designed for high-leverage industrial settings where averting a single 8-hour unplanned plant outage covers the annualized sensor and platform deployment cost.

### 4. Risk, Governance & Reliability
- **Failsafe Escalation:** When telemetry degradation exceeds safety thresholds, the engine transitions from autonomous optimization to mandatory operational escalation, requiring physical engineering sign-off.
- **Degraded-State Resilience:** Explicitly handles partial telemetry loss; the system abstains from aggressive optimization and falls back to conservative operating bounds rather than assuming zero failure probability.

### 5. Venture & Strategic Scaling
- Scalable from individual high-value rotating machines (turbines, compressors) to facility-wide predictive maintenance operations.

---

## Reproducibility & Quickstart

The repository contains an automated test suite verifying scenario cost trade-offs, option value boundaries, and intervention logic.

```bash
# Clone repository
git clone https://github.com/IgorGryb/arxa-industrial-options.git
cd arxa-industrial-options

# Run verification suite (8 tests)
python3 -m unittest discover -s tests -v
# Alternatively:
make test
```

Expected output:
```text
test_capacity_zero_matches_no_intervention (test_core.ScenarioTest) ... ok
test_cost_gap_not_option_value (test_core.ScenarioTest) ... ok
test_degradation_not_better (test_core.ScenarioTest) ... ok
test_no_silent_truncation_or_empty_forecast (test_core.ScenarioTest) ... ok
test_option_is_explicit (test_core.ScenarioTest) ... ok
test_policy_better_than_never_maintain (test_core.ScenarioTest) ... ok
test_zero_efficacy_reverses_benefit (test_core.ScenarioTest) ... ok
test_reproduction_writes_results_and_manifest (test_reproduction.ReproductionTest) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.005s

OK
```

---

## Research Integrity & Disclaimer

This repository is an architectural reference prototype and bounded decision model developed by Igor Grybek. All tests and demonstrations operate strictly on reproducible, synthetic machine telemetry and cost assumptions. No proprietary or confidential corporate data from historical engagements is contained herein.
