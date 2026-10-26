import unittest
from arxa.core import telemetry, forecast, policy_cost, real_option
class ScenarioTest(unittest.TestCase):
    def test_policy_better_than_never_maintain(self):
        rows=telemetry(); preds,_=forecast(rows); policy=policy_cost(rows,preds); baseline=sum(r["failure"] for r in rows)*90000; self.assertLess(policy["cost"],baseline)
    def test_degradation_not_better(self):
        rows=telemetry(); _,a=forecast(rows); _,b=forecast(rows,True); self.assertGreaterEqual(b,a)
    def test_option_is_explicit(self): self.assertIn(real_option(.8)["decision"],{"act","defer"})
    def test_zero_efficacy_reverses_benefit(self):
        rows=telemetry(); preds,_=forecast(rows)
        baseline=sum(r['failure'] for r in rows)*90000
        self.assertGreater(policy_cost(rows,preds,efficacy=0)['cost'],baseline)
    def test_capacity_zero_matches_no_intervention(self):
        rows=telemetry(); preds,_=forecast(rows)
        self.assertEqual(policy_cost(rows,preds,max_actions=0)['cost'],sum(r['failure'] for r in rows)*90000)
    def test_no_silent_truncation_or_empty_forecast(self):
        with self.assertRaises(ValueError): policy_cost(telemetry(),[])
        with self.assertRaises(ValueError): forecast([])
        with self.assertRaises(ValueError): real_option(float('nan'))
    def test_cost_gap_not_option_value(self):
        r=real_option(.8)
        self.assertNotIn('option_value',r); self.assertIn('not a real-option',r['scope'])
