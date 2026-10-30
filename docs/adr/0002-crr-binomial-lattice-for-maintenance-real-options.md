# ADR 0002: Cox-Ross-Rubinstein Binomial Lattices for Maintenance Real Options

- **Status:** Accepted
- **Date:** 2026-10-28
- **Context:** Quantitative Capital Allocation & Asset Maintenance Timing
- **Deciders:** Igor Grybek (Systems Architect, Arxa Group)

## Context & Problem Statement
Traditional industrial asset management relies on static Discounted Cash Flow (DCF) or Net Present Value (NPV) calculations. When a condition monitoring system detects early mechanical wear, standard tools compare the static cost of immediate replacement against expected failure costs. This ignores the value of managerial flexibility: the option to wait one more operational cycle, gather additional vibration telemetry, and defer irreversible capital expenditure.

## Decision Drivers
1. **Managerial Flexibility Valuation:** Valuing the real option to defer maintenance under asset degradation uncertainty.
2. **Computational Tractability:** Providing deterministic, transparent valuation trees understandable by plant controllers and CFOs.
3. **Adherence to Columbia Financial Engineering Standards:** Methodological alignment with Cox-Ross-Rubinstein (CRR) discrete-time lattice formulation.

## Decision Outcome
Chosen Option: **American-Style Binomial Real-Options Lattice**.
The model formulates maintenance timing as an optimal stopping problem on a recombining binomial tree:
- Underlying asset value $S_t$: PV of manufacturing capacity delivered by the asset.
- Strike price $K$: Irreversible CapEx required for equipment overhaul.
- Backward induction determines at each node whether:
  $$V(S, t) = \max\left( S - K, \, e^{-r \Delta t} [p V_u + (1-p) V_d] \right)$$
Where $S - K$ represents immediate exercise ($\text{Act}$) and the continuation value represents deferral ($\text{Defer}$).

### Positive Consequences
- Formally bridges engineering reliability metrics with executive capital budgeting.
- Demonstrates that optimal timing under uncertainty reduces total lifecycle costs from €540,000 (unmanaged baseline) to €484,000 (real-options optimum), delivering €56,000 in net savings.
