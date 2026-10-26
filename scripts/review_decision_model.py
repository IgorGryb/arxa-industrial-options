import hashlib,json
from pathlib import Path
from arxa.core import telemetry,forecast,policy_cost,real_option
ROOT=Path(__file__).resolve().parents[1]
def main():
    rows=telemetry(); preds,error=forecast(rows); _,degraded=forecast(rows,True)
    baseline=sum(r['failure'] for r in rows)*90000
    cases=[dict(efficacy=e,capacity=c,**policy_cost(rows,preds,efficacy=e,max_actions=c)) for e in (0,.5,1) for c in (0,2,10,None)]
    assert all(r['cost']==baseline for r in cases if r['capacity']==0)
    assert next(r['cost'] for r in cases if r['efficacy']==0 and r['capacity'] is None)>baseline
    r=dict(id='ARXA-MANAGEMENT-REVIEW-001',scope='synthetic index forecast and assumed intervention scenarios',
           forecast_mae=error,degraded_data_mae=degraded,baseline_cost=baseline,scenarios=cases,
           act_defer=real_option(.8),management_costs=dict(base=180,negative=380,unit='synthetic EUR/period'),
           model_sha256=hashlib.sha256((ROOT/'src/arxa/core.py').read_bytes()).hexdigest(),
           limitations=['Uncalibrated synthetic score','Efficacy assumed, not causal estimate','No real-option price','No observed operating benefit'])
    (ROOT/'artifacts/management-review.json').write_text(json.dumps(r,indent=2)+'\n')
    lines=['# ARXA — validation and decision memo','','Private synthetic study. Eight repository tests; twelve efficacy/capacity scenarios.','',
           '| Efficacy | Capacity | Cost | Actions | Residual failures |','|---:|---:|---:|---:|---:|']
    lines += [f"| {x['efficacy']} | {x['capacity'] if x['capacity'] is not None else 'unlimited'} | {x['cost']:.0f} | {x['preventive_actions']} | {x['unmitigated_failures']} |" for x in cases]
    lines += ['',f'No-intervention baseline cost: {baseline}. Synthetic technical cost units; not the EUR/period management case.',
              f'Rolling index MAE: {error:.6f}; degraded-input MAE: {degraded:.6f}. This predicts an engineered index, not calibrated failure probability.',
              '', '## Decision and forecast interpretation','',
              'The original favorable-policy forecast holds only under its selected perfect-efficacy assumptions. Zero efficacy reverses the advantage; zero capacity reproduces no intervention. Preserve the negative result instead of presenting only the favorable scenario.',
              'The separate pre-recorded management-cost example is 180 versus 380 EUR/period at residual failure probabilities 0.10 and 0.30. This arithmetic does not identify treatment benefit.',
              'Continue a narrowly scoped decision study. Pause an operating recommendation until data quality, failure labels, efficacy and available intervention resources are established. A staged capital commitment requires a separate cash-flow and financing model.',
              '', '## Post-mortem','',
              'Removed the misleading option_value field: an absolute cost difference is not a real-option price. Added efficacy/capacity scenarios and rejected prediction-length mismatch instead of silently truncating observations. Costs, scores and probabilities retain distinct meanings.',
              'Handoff: DELIVERY-SPECIFICATION.md, tests and artifacts/management-review.json. No real asset, customer, industrial saving or production integration is claimed.']
    (ROOT/'docs/MODEL-VALIDATION-MEMO.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps(dict(scenarios=len(cases),baseline=baseline,status='bounded-review-passed')))
if __name__=='__main__': main()
