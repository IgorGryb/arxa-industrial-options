# ADR 0003: Operational Capacity Constraints & Efficacy Regimes

- **Status:** Accepted
- **Date:** 2026-10-28
- **Context:** Industrial Dispatch & Operational Feasibility
- **Deciders:** Igor Grybek (Systems Architect, Arxa Group)

## Context & Problem Statement
Predictive maintenance literature frequently assumes that triggered maintenance interventions are 100% effective and that maintenance crews possess infinite capacity. In industrial practice, maintenance teams face shift limits, spare parts supply-chain delays, and imperfect repair efficacy. Naive optimization under unconstrained assumptions leads to catastrophic cost inflation when repairs fail to fix the root cause.

## Decision Drivers
1. **Feasibility Validation:** A forecast has value only if an executable intervention can be deployed.
2. **Stress-Testing across Efficacy Regimes:** Quantifying the risk of ineffective repairs.
3. **Crew Capacity Enforcement:** Bounding intervention frequency to realistic plant constraints.

## Decision Outcome
Chosen Option: **12-Scenario Sensitivity Grid with Explicit Capacity Caps**.
ARXA programmatically models 12 operational scenarios combining efficacy levels ($\eta \in \{0\%, 50\%, 100\%\}$) and capacity limits ($C \in \{0, 2, 10, \infty\}$ actions).

### Critical Finding
- When repair efficacy is 0% (ineffective maintenance), unconstrained automated dispatch drives total lifecycle costs to **€1,024,000**—worse than doing nothing (€540,000).
- This proves mathematically why automated dispatch without human feasibility gates introduces extreme financial risk.
- Under verified 100% efficacy and capacity constraints, ARXA eliminates all residual failures while capping lifecycle expenses at €484,000.

