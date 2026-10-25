import unittest
from arxa.core import telemetry, forecast, policy_cost, real_option
class ScenarioTest(unittest.TestCase):
    def test_policy_better_than_never_maintain(self):
        rows=telemetry(); preds,_=forecast(rows); policy=policy_cost(rows,preds); baseline=sum(r["failure"] for r in rows)*90000; self.assertLess(policy["cost"],baseline)
    def test_degradation_not_better(self):
        rows=telemetry(); _,a=forecast(rows); _,b=forecast(rows,True); self.assertGreaterEqual(b,a)
    def test_option_is_explicit(self): self.assertIn(real_option(.8)["decision"],{"act","defer"})
