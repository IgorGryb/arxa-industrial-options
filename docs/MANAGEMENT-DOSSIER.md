# ARXA — management and operating dossier

Project: `PRJ-ARXA-PROTOTYPE`. Authored 2026-10-26. Status: internally specified design; not a deployed service. Source concept: `SRC-PRJ-ARXA-DOC`. Methods: M-SIPOC, M-RACI, M-FEASIBILITY, M-SCENARIO, M-MEASURE.

## Decision and business model

A model for managing data-enabled operational transformation and investment choices.

**Problem:** An industrial analytics initiative can optimize a prediction metric without improving the operational decision or economics.
**Customer / decision user:** Operations manager, asset owner and finance sponsor
**Payer:** Industrial business unit; no actual client assumed
**Value proposition (hypothesis):** A measurable connection between data quality, operating action and incremental economics.

**Alternatives:**

- Calendar maintenance: transparent operational baseline
- Buy vendor analytics: compare access, integration and exit costs
- Build full industrial platform: defer

**Selected design decision:** Use one maintenance case and a transparent baseline; reuse Arctervix financing concepts by reference rather than claim a second independent invention.

Market size, paid demand, channel conversion and real service delivery are not established. First access channel is a controlled review with the target decision user. Scale only after the problem and acceptance criteria survive that review.

## Product scope and acceptance

| ID | Must requirement | Acceptance evidence |
|---|---|---|
| ARXA-REQ-01 | Model output maps to a named operational action | Reviewer checks the corresponding model/process step; records source, exception and outcome. |
| ARXA-REQ-02 | Baseline remains available on data failure | Reviewer checks the corresponding model/process step; records source, exception and outcome. |
| ARXA-REQ-03 | Economic benefit is not double-counted | Reviewer checks the corresponding model/process step; records source, exception and outcome. |

Should: export a decision memo and traceability view. Could: automate repetitive updates after correctness is established.
**Will not do:** Live machine control, guaranteed downtime reduction, production safety certification.

## Operating model — SIPOC

- Supplier: Asset/process owner and approved public or synthetic data
- Inputs: Failure assumptions, intervention costs, downtime and data-quality indicators
- Process: Choose one operational bottleneck → Map baseline process and decision owner → Define data and intervention policy → Compare costs and degraded-data scenarios → Set rollout controls and stop criteria
- Outputs: Maintenance/investment policy, scenario economics and rollout decision
- Customer: Operations manager, asset owner and finance sponsor

### Control and exception handoffs

| Step | Responsible | Accountable | Control / handoff |
|---|---|---|
| 1. Choose one operational bottleneck | Analyst / process owner | Decision owner | Record input version, output ID and reviewer; exceptions escalate before the next release. |
| 2. Map baseline process and decision owner | Analyst / process owner | Decision owner | Record input version, output ID and reviewer; exceptions escalate before the next release. |
| 3. Define data and intervention policy | Analyst / process owner | Decision owner | Record input version, output ID and reviewer; exceptions escalate before the next release. |
| 4. Compare costs and degraded-data scenarios | Analyst / process owner | Decision owner | Record input version, output ID and reviewer; exceptions escalate before the next release. |
| 5. Set rollout controls and stop criteria | Analyst / process owner | Decision owner | Record input version, output ID and reviewer; exceptions escalate before the next release. |

Roles are proposed functions, not claims of an existing staffed organization. Reviewer is consulted; downstream owner is informed. A single person may hold several roles, but cannot claim independent review of their own work.

**Exception policy:** Missing or degraded inputs trigger baseline policy or manual review; no automatic physical actuation.

## End-to-end operationalization

| Stage | Input | Owner | Method | Tool | Artifact | Gate | Next owner |
|---|---|---|---|---|---|---|---|
| Initiation | Mandate and source record | Decision owner | M-RACI | Obsidian | Problem/mandate brief | Alternative of no action stated | Analyst |
| Analysis | Brief and approved sources | Analyst | M-SIPOC | Obsidian | Source and assumption map | Facts separated from hypotheses | Model owner |
| Modeling | Assumptions and baseline | Model owner | M-SCENARIO | Excel | Economic and operational model | Units, population and perspective explicit | Product owner |
| Design | Model and user needs | Product owner | M-FEASIBILITY | FigJam / local flow | Requirements and data flow | Every Must links to acceptance test | Delivery owner |
| Planning | Requirements and dependencies | Delivery owner | M-MOSCOW | Linear / local backlog | Prioritized handoff plan | Single accountable owner and next action | Implementer or analyst |
| Execution | Approved scope | Analyst / implementer | M-FEASIBILITY | Local documents/model | Controlled artifact version | No undocumented scope expansion | Reviewer |
| Testing | Artifact, baseline and forecast | Reviewer | M-SCENARIO | Excel / targeted tests | Test report | Normal and negative cases documented | Decision owner |
| Evaluation | Results and limitations | Decision owner | M-MEASURE | Dashboard + PowerPoint storyboard | Decision memo | Recommendation conditional on evidence | Change owner |
| Change management | New source, exception or decision | Change owner | M-RACI | Git + local change log | Impact and revised baseline | Dependent outputs marked stale/rechecked | Next stage owner |

Tool configuration is proposed, not connected. Local Markdown/YAML is authoritative. Cloud tools require a separate data-sharing decision. See [toolchain](../../../00.%20ARCHIVE%20SYSTEM/portfolio/TOOLCHAIN-AND-HANDOFF.md).

## Financial and operating economics

Incremental value = avoided expected downtime/loss - intervention cost - data/platform/change cost. Separate estimated economic impact from measured savings. Do not count the same failure avoidance in multiple benefit categories.

Estimates must disclose cost population, currency, horizon and baseline. Sensitivity changes one driver or a declared scenario while other external assumptions remain equal. Missing required input makes the result unavailable. No forecast is reported as a realized business result.

## Technology management and build/buy/partner

Keep a source/assumption register, a model layer, a review layer and derived communication outputs. Stable IDs connect them. Access labels travel with the data. Maintain exportable local records and a documented exit path before selecting a hosted service.

Buy or reuse commodity task management, presentation and modeling tools. Build only a narrow calculation or validator when it resolves a decision-critical uncertainty. Partner for specialist legal, domain or security validation when the scope requires it. Proposed interfaces exchange artifact ID, version, owner, status and source IDs; no integration is claimed as implemented.

NFR design: outputs must be traceable and reproducible; invalid inputs must be visible; sensitive data must not leave the approved boundary. Response-time, uptime and capacity targets remain uncalibrated until a real user/process requires them.

## Metrics and dashboard specification

| Metric | Unit | Calculation | Source | Decision |
|---|---|---|---|---|
| Expected total cost | EUR/period | failure loss + interventions + platform/change cost | scenario assumptions | Compare policy to baseline |
| Data completeness | fraction | valid required observations / required observations | data-quality log | Fallback or revalidate |
| Incremental value | EUR/period | baseline cost - proposed-policy cost | paired scenario models | Continue only if robust under downside |

Metric owner: process/model owner. Review event: new result, changed assumption or operating incident, not an imposed calendar. For fractions, zero/missing denominator means unavailable. Actual metrics need a defined reporting period and event population; none are invented here.

Dashboard layout: decision/status at top, scenario comparison in the center, assumptions and exceptions below. Use a line chart for time, bars for comparable alternatives, and a table for exact constraints. Do not combine projected and realized values without explicit labeling.

## Validation and risk

**Hypothesis:** A simple decision policy with controlled data quality can outperform complexity that ignores operating costs.

**Negative scenario:** Degrade data and raise intervention cost; favorable economic claims must be recalculated, not retained.

**Material limitation:** Distribution shift, sensor quality and intervention effectiveness may invalidate estimated savings.

Validation layers: structural document review; arithmetic/model tests; scenario/exception walkthrough; external validation only when an appropriate recipient participates. Existing technical-baseline tests remain bounded evidence. User practice is optional and not a release gate for documentation.

## Delivery and stop conditions

Sequence: source and mandate → explicit model and handoffs → targeted validation → decision memo → review-ready case study. Continue if the model answers the decision with traceable assumptions. Pivot if the decision or economics changes. Pause if a necessary source is unavailable. Stop if the best supported option is no action or a simpler existing solution.

**Next event-triggered action:** Validate intervention effectiveness and adoption costs before broadening to a platform.

## Presentation storyboard

1. Decision and user problem. 2. Alternatives and source basis. 3. Product and operating model. 4. Economics and scenarios. 5. Architecture and ownership. 6. Validation result and limitations. 7. Recommendation and next decision.

Each slide and dashboard number must point back to this dossier and its model/run. Storyboard is not a delivered slide deck. No public publishing or external application is performed.

## Provenance and authoring boundary

This management model was authored with an AI agent from existing project sources, course materials and the approved user direction. It demonstrates the documented design and review process, not independent proof that the user performed every implementation step. All economic sample cases are synthetic.
