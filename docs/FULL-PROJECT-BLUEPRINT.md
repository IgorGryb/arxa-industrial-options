# Full project blueprint — ARXA — Industrial Scenario and Real Options Platform

> Controlling management update (2026-10-26): [Management dossier](MANAGEMENT-DOSSIER.md) defines business, product, operating, financial and technology-management scope. User practice and production implementation are not documentary gates. Earlier technical content below remains bounded supporting material, not the full portfolio mandate.


Stable project ID: `PRJ-ARXA-PROTOTYPE`  
Status: source-grounded target architecture; implementation and validation backlog  
Evidence boundary: this document specifies what should be built and tested. Only linked test artifacts may support implementation claims.

## 1. Project thesis and decision boundary

A credible industrial decision system should start with one asset, failure mode and maintenance/capital decision, quantify uncertainty and human override, and treat the broader distributed, agentic and real-options platform as a staged roadmap.

**Decision owner:** maintenance/reliability and capital decision owner  
**Decision supported:** Whether to inspect, maintain, defer, stage, expand or abandon an intervention under uncertain failure risk, downtime cost and capital constraints.

### Users and reviewers

- reliability engineer
- maintenance planner
- operations manager
- finance/investment reviewer
- data/model owner

### In scope for the validated portfolio case

- one public industrial or energy dataset
- one asset/failure proxy
- temporal forecast comparison
- maintenance policy and work-order states
- NPV and real-option scenarios

### Explicitly outside the validated claim

- autonomous safety-critical execution
- enterprise-scale agent network
- blockchain requirement
- quantum advantage
- claimed client ROI or production integration

## 2. Layer architecture and operationalization

`Current` is evidence-based maturity now; `target` is the program gate. It is not a claim that the target has been achieved.

### 2.1 problem-user

**Objective:** Narrow the platform vision to one asset, failure mode and decision owner.

**Operationalization:** Define physical process, intervention choices, decision lead time, data availability, safety boundary and stop criterion.

**Required artifact:** industrial decision charter  
**Acceptance test:** An operations/reliability reviewer confirms the decision and proxy limitations.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling, `C419-055`  
**Maturity:** current L2 → target L5  
**Open gap:** No selected real asset owner; archive lacks a dedicated supply-chain course.

### 2.2 market-business

**Objective:** Establish a defensible beachhead and alternative solutions.

**Operationalization:** Compare OEM tools, CMMS/EAM, analytics platforms, manual inspection and no-action; define buyer, integration friction and value hypothesis.

**Required artifact:** industry strategy and adoption memo  
**Acceptance test:** A practitioner validates priority, buying constraints and rejects unsupported platform-scale claims.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling, `C419-055`  
**Maturity:** current L2 → target L5  
**Open gap:** Broad market/ROI claims in the concept corpus are unsupported for publication.

### 2.3 product-service

**Objective:** Deliver a human-controlled risk-to-action journey.

**Operationalization:** Specify asset view, data-quality signal, risk forecast, explanation, scenario comparison, inspection/work-order, approval, override and learning feedback.

**Required artifact:** product and service blueprint  
**Acceptance test:** Role scenarios correctly handle alert, abstention, override, completed work and observed outcome.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling, `C419-161`  
**Maturity:** current L3 → target L5  
**Open gap:** Current prototype calculates a policy but lacks complete operational journeys.

### 2.4 operating-model

**Objective:** Integrate forecast with inspection, planning, spares, windows and incidents.

**Operationalization:** Assign RACI, SLA, evidence and escalation across monitoring, engineer review, work-order, approval, execution, incident and feedback.

**Required artifact:** maintenance decision runbook  
**Acceptance test:** Tabletop exercise handles bad sensor, missed failure, unavailable part and disputed recommendation.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling, `C419-154`  
**Maturity:** current L2 → target L5  
**Open gap:** No observed maintenance workflow or dedicated supply-chain source.

### 2.5 data-technology

**Objective:** Build governed telemetry-to-policy components with monitoring.

**Operationalization:** Separate ingest, quality, feature store, training, scoring, calibration, policy, scenario/options, explanation, monitoring and audit interfaces.

**Required artifact:** reference architecture and executable pipeline  
**Acceptance test:** Temporal reproduction, schema drift, missingness, load and access tests meet declared thresholds.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling, `C419-138`, `C419-140`, `C419-143`, `C419-154`, `C419-161`  
**Maturity:** current L4 → target L5  
**Open gap:** Synthetic prototype needs public time-series data and realistic operational scale tests.

### 2.6 analytical-model

**Objective:** Evaluate forecast calibration and decision policy under asymmetric costs.

**Operationalization:** Pre-register targets, leakage controls, temporal splits, naive/statistical/ML baselines, calibration, cost matrix and abstention threshold.

**Required artifact:** forecast and policy benchmark  
**Acceptance test:** Model beats baseline on decision metric, survives degraded-data tests and exposes inconclusive cases.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling, `C419-121`, `C419-143`, `C419-201`  
**Maturity:** current L4 → target L5  
**Open gap:** Existing corrected metric is narrow and based on synthetic data.

### 2.7 finance-economics

**Objective:** Link operational uncertainty to NPV and real options without claiming realized ROI.

**Operationalization:** Model downtime, failure severity, maintenance, inventory, capex, discount rate and options to defer/stage/expand/abandon.

**Required artifact:** investment and real-options model  
**Acceptance test:** Sensitivity identifies decision reversals and an independent finance reviewer checks cash-flow logic.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling, `C419-197`, `C419-201`  
**Maturity:** current L3 → target L5  
**Open gap:** Synthetic costs are illustrative and not calibrated to an asset.

### 2.8 risk-security-compliance

**Objective:** Prevent unsafe automation and ungoverned industrial data use.

**Operationalization:** Define safety boundary, human override, provenance, access, audit, cybersecurity questions, drift, model change and abstention.

**Required artifact:** industrial AI risk/control matrix  
**Acceptance test:** Failure injection produces safe abstention/escalation; every critical control has owner and residual risk.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling, `C419-190`  
**Maturity:** current L2 → target L5  
**Open gap:** No safety/cyber domain review or implemented access control.

### 2.9 delivery-governance

**Objective:** Stage platform ambition and control model/policy changes.

**Operationalization:** Use capability status, ADRs, data/model releases, approval gates, incident post-mortem and explicit roadmap boundaries for agentic/blockchain/quantum ideas.

**Required artifact:** delivery roadmap and model governance  
**Acceptance test:** A model/policy update is traced through data, tests, operations, finance and dependent claims.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling, `C419-161`, `C419-190`  
**Maturity:** current L3 → target L5  
**Open gap:** Far-future capabilities must be demoted to hypotheses/interfaces until implemented.

### 2.10 evidence-validation-publication

**Objective:** Publish one validated industrial decision case with transparent proxy and estimate boundaries.

**Operationalization:** Bind claims to public dataset, temporal split, model run, policy result, option assumptions, reviewer notes and limitations.

**Required artifact:** industrial evidence dossier and case study  
**Acceptance test:** No client, compliance, autonomous-agent or realized-ROI claim survives without evidence; user approves publication.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling, `C419-190`, `C419-197`  
**Maturity:** current L2 → target L6  
**Open gap:** Current PDF/web are based on the synthetic baseline and require replacement.

## 3. Operating state model

### Normal states

`telemetry received → quality checked → risk scored → abstained or alert → engineer review → inspection requested → work order planned → approved/deferred → maintenance executed → outcome observed → model/policy updated`

Every transition must record actor, timestamp, input state, output state, decision/evidence reference and exception reason when applicable.

### Required exception paths

- sensor drift
- missing maintenance history
- distribution shift
- false alarm
- missed failure
- spares unavailable
- maintenance-window conflict
- human override
- cost estimate uncertainty
- unsafe action request

## 4. Technical and quality envelope

### Non-functional requirements

- temporal data isolation
- training/scoring separation
- uncertainty exposed
- human override mandatory
- no autonomous safety action
- data-quality abstention
- policy and finance assumptions versioned

### Metrics tree

- forecast MAE/Brier/calibration
- false negative and false positive cost
- lead time
- downtime avoided as modeled range
- maintenance and inventory cost
- work-order completion
- override rate
- NPV and option value sensitivity
- drift/data-quality alerts

Metrics must be tagged as observed, modeled or estimated. Modeled economic impact cannot be presented as realized impact.

## 5. Falsifiable hypotheses

1. A temporal forecast will outperform a naive baseline sufficiently to change a preregistered maintenance decision under asymmetric cost.
2. A policy that exposes calibration and permits abstention will outperform a fixed threshold when data quality degrades.
3. Real-option framing changes capital timing under at least one plausible uncertainty scenario, without implying realized savings.

A test that cannot refute a hypothesis is practice or demonstration, not validation.

## 6. Experiment sequence

1. Select a public dataset and document why it is only a proxy for the chosen operational process.
2. Compare naive, statistical and one ML baseline using temporal splits and calibrated probabilities.
3. Inject missingness, drift and label delay; test abstention, override and policy cost.
4. Run maintenance and real-option scenarios with operations and finance reviewers; record disagreements and corrections.

The prediction, threshold and interpretation owner must be recorded before each result. Failed or inconclusive tests remain in the evidence bundle.

## 7. Source-to-practice coverage

| Mapping | Layer | Course | Archive state | Practice/test | Evidence target |
|---|---|---|---|---|---|
| MOD-SPEC | operations | Electric Industry Operations and Markets | manifest-complete | use energy asset case or operational analogy | sector operations memo |
| MOD-SPEC | business | Oil & Gas Industry Operations and Markets | manifest-complete | map upstream-to-downstream decision economics | industry case map |
| MOD-SPEC | technology | Advanced Business Analytics: Excel Optimization & Simulation | manifest-complete | optimize maintenance policy under constraints | sensitivity report |
| MOD-SPEC | technology | Advanced Analytics & AI Optimization with Microsoft Fabric | manifest-complete | design experiment and monitoring surface | technical architecture |
| MOD-SPEC | technology | Big Data Management and Optimization | manifest-complete | define scale and partition assumptions | data architecture test |
| MOD-SPEC | technology | Data Analytics and Machine Learning for Big Data | manifest-complete | compare forecasting baselines | model benchmark |
| MOD-SPEC | operations | Indexing, Performance Optimization & Functions in SQL Server | manifest-complete | design operational query workload | performance report |
| MOD-SPEC | technology | Microsoft Azure Machine Learning for Data Scientists | manifest-complete | add training/scoring separation and monitoring | model-operations card |
| MOD-SPEC | finance-risk | Introduction to Financial Engineering and Risk Management | manifest-complete | formalize uncertainty and policy objective | model specification |
| MOD-SPEC | governance | Risk Management and Financial Theory | manifest-complete | define override/escalation logic | risk-control memo |
| MOD-SPEC | finance-risk | Modeling Risk and Realities | manifest-complete | pre-register distributions and scenario priors | forecast log |
| MOD-SPEC | business | Corporate & Business Strategy | manifest-complete | choose beachhead and alternatives | strategy memo |
| MOD-SPEC | governance | AI Strategy and Governance | manifest-complete | define human ownership and model-change gates | governance policy |
| MOD-SPEC | finance-risk | Introduction to Corporate Finance | manifest-complete | connect options to NPV and financing | investment memo |

All rows above currently mean source routing. They become competence evidence only after the stated practice/test is executed and recorded.

## 8. Artifact backlog and gates

| Artifact ID | Layer | Deliverable | Current → target | Definition of Done |
|---|---|---|---:|---|
| ART-ARXA-01 | problem-user | industrial decision charter | L2 → L5 | An operations/reliability reviewer confirms the decision and proxy limitations. |
| ART-ARXA-02 | market-business | industry strategy and adoption memo | L2 → L5 | A practitioner validates priority, buying constraints and rejects unsupported platform-scale claims. |
| ART-ARXA-03 | product-service | product and service blueprint | L3 → L5 | Role scenarios correctly handle alert, abstention, override, completed work and observed outcome. |
| ART-ARXA-04 | operating-model | maintenance decision runbook | L2 → L5 | Tabletop exercise handles bad sensor, missed failure, unavailable part and disputed recommendation. |
| ART-ARXA-05 | data-technology | reference architecture and executable pipeline | L4 → L5 | Temporal reproduction, schema drift, missingness, load and access tests meet declared thresholds. |
| ART-ARXA-06 | analytical-model | forecast and policy benchmark | L4 → L5 | Model beats baseline on decision metric, survives degraded-data tests and exposes inconclusive cases. |
| ART-ARXA-07 | finance-economics | investment and real-options model | L3 → L5 | Sensitivity identifies decision reversals and an independent finance reviewer checks cash-flow logic. |
| ART-ARXA-08 | risk-security-compliance | industrial AI risk/control matrix | L2 → L5 | Failure injection produces safe abstention/escalation; every critical control has owner and residual risk. |
| ART-ARXA-09 | delivery-governance | delivery roadmap and model governance | L3 → L5 | A model/policy update is traced through data, tests, operations, finance and dependent claims. |
| ART-ARXA-10 | evidence-validation-publication | industrial evidence dossier and case study | L2 → L6 | No client, compliance, autonomous-agent or realized-ROI claim survives without evidence; user approves publication. |

### External validation required

- reliability/maintenance practitioner review
- industrial data/security review
- corporate-finance/real-options assumptions review

## 9. Integrated delivery sequence

1. Confirm problem, decision owner, user and anti-scope; record the user's own explanation.
2. Freeze approved sources/data and record hashes, permissions and proxy limitations.
3. Pre-register hypotheses, predictions, thresholds, alternatives and falsification conditions.
4. Complete guided practice from the selected courses and save its independent output.
5. Implement the vertical slice with explicit normal and exception states.
6. Compare against baseline; run negative, security, data-quality and sensitivity tests.
7. Review business, operations, finance and governance artifacts with the appropriate role.
8. Correct model, assumptions, dependent documents and evidence manifests.
9. Ask the user to interpret the result and choose continue, pause, pivot, stop or complete.
10. Only after acceptance, regenerate case study, PDF and private web version and run a claim audit.

## 10. Publication claim boundary

Allowed now: the narrow technical baseline exists and its local tests passed.  
Not allowed now: production readiness, market adoption, realized economic impact, legal compliance, client result or broad platform implementation.  
Allowed later: only statements backed by a versioned artifact, test result, reviewer record and evidence-manifest entry.

## 11. User gates

The user participates before irreversible narrowing, before a material test, when interpreting the result and before publication. The minimum prompts are:

- explain the problem and expected mechanism in your own words;
- predict the result and name a falsifying observation;
- interpret differences between baseline, model and judgment;
- choose `continue`, `pause`, `pivot`, `stop` or `complete`;
- state what changed in your understanding.
