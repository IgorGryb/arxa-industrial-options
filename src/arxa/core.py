from __future__ import annotations
import csv, hashlib, json, math
from pathlib import Path

PROJECT_ID="PRJ-ARXA-PROTOTYPE"
def telemetry(n=80):
    rows=[]
    for i in range(n):
        degradation=i/n
        vibration=2.0+2.5*degradation+0.2*math.sin(i*.7)
        temperature=55+19*degradation+1.5*math.sin(i*.31)
        risk=max(0,min(1,.55*(vibration-2)/3+.45*(temperature-55)/22))
        failure=1 if risk>.65 and i%7 in (0,1) else 0
        rows.append({"period":i+1,"vibration":vibration,"temperature":temperature,"risk":risk,"failure":failure})
    return rows
def forecast(rows, degraded=False):
    if not rows: raise ValueError('Nonempty time-ordered observations required')
    if any(not isinstance(r.get('risk'),(int,float)) or not math.isfinite(r['risk']) or not 0<=r['risk']<=1 for r in rows): raise ValueError('Invalid synthetic risk score')
    errors=[]; preds=[]
    for i,row in enumerate(rows):
        if i<5: pred=.1
        else:
            hist=rows[max(0,i-5):i]
            values=[x["risk"] for j,x in enumerate(hist) if not degraded or (j+i)%3]
            pred=sum(values)/len(values) if values else .1
        preds.append(pred); errors.append(abs(pred-row["risk"]))
    return preds,sum(errors)/len(errors)
def policy_cost(rows,preds,threshold=.55,preventive=22000,failure_cost=90000,efficacy=1.,max_actions=None):
    if len(rows)!=len(preds): raise ValueError('Prediction length mismatch')
    if any(not isinstance(v,(int,float)) or not math.isfinite(v) for v in (threshold,preventive,failure_cost,efficacy)): raise ValueError('Finite assumptions required')
    if not 0<=threshold<=1 or not 0<=efficacy<=1 or min(preventive,failure_cost)<0: raise ValueError('Invalid policy assumptions')
    if max_actions is not None and (type(max_actions) is not int or max_actions<0): raise ValueError('Invalid capacity')
    if any(not math.isfinite(p) or not 0<=p<=1 for p in preds): raise ValueError('Invalid prediction')
    cost=0; actions=0; failures=0
    for row,p in zip(rows,preds):
        if p>=threshold and (max_actions is None or actions<max_actions):
            cost+=preventive+row['failure']*(1-efficacy)*failure_cost; actions+=1
            failures+=row['failure']*(1-efficacy)
        elif row["failure"]: cost+=failure_cost; failures+=1
    return {"cost":cost,"preventive_actions":actions,"unmitigated_failures":failures}
def real_option(current_risk,preventive=22000,failure_cost=90000,learning_value=5000):
    if any(not isinstance(v,(int,float)) or not math.isfinite(v) for v in (current_risk,preventive,failure_cost,learning_value)) or not 0<=current_risk<=1 or min(preventive,failure_cost,learning_value)<0: raise ValueError('Invalid act/defer assumptions')
    act=preventive; defer=current_risk*failure_cost-learning_value
    return {"act_cost":act,"defer_expected_cost":defer,"decision":"act" if act<defer else "defer","cost_gap":abs(defer-act),"scope":"one-step assumed cost comparison, not a real-option valuation","learning_credit_status":"exogenous assumption, not measured information value"}
def run(root: Path):
    rows=telemetry(); (root/"data").mkdir(parents=True,exist_ok=True); (root/"artifacts").mkdir(parents=True,exist_ok=True)
    with (root/"data/synthetic_telemetry.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    preds,error=forecast(rows); _,degraded_error=forecast(rows,True); policy=policy_cost(rows,preds); baseline={"cost":sum(r["failure"] for r in rows)*90000,"preventive_actions":0,"unmitigated_failures":sum(r["failure"] for r in rows)}
    option=real_option(rows[-1]["risk"]); passed=policy["cost"]<baseline["cost"] and degraded_error>=error
    result={"project_id":PROJECT_ID,"claim_scope":"synthetic industrial scenario estimate","forecast_mae":error,"degraded_data_mae":degraded_error,"baseline":baseline,"risk_policy":policy,"real_option":option,"prediction_passed":passed,"economic_impact_status":"modeled estimate, not realized savings"}
    (root/"artifacts/results.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    memo=f"# Industrial decision memo — synthetic demonstration\n\nModeled baseline cost: {baseline['cost']}. Risk-policy cost: {policy['cost']}. Act/defer result: {option['decision']}. All values are synthetic estimates and do not represent realized savings.\n"
    (root/"artifacts/decision-memo.md").write_text(memo,encoding="utf-8")
    arts=[]
    for rel in ["artifacts/results.json","artifacts/decision-memo.md","data/synthetic_telemetry.csv"]:
        p=root/rel; arts.append({"artifact_id":"ART-"+hashlib.sha256(rel.encode()).hexdigest()[:12].upper(),"path":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"validation_status":"tested","reproduce_command":"make reproduce"})
    (root/"artifacts/evidence-manifest.json").write_text(json.dumps({"project_id":PROJECT_ID,"generated":"2026-10-25","data_class":"synthetic","artifacts":arts},indent=2),encoding="utf-8")
    return result
