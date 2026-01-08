from typing import List, Dict
from .rules import FraudRule
from .signals import DistributionSignal


class RiskScorer:
    """
    Aggregates antifraud rules into a transparent risk score
    """

    def __init__(self, rules: List[FraudRule]):
        self.rules = rules

    def score(self, signals: List[DistributionSignal]) -> Dict:
        total_score = 0
        triggered = []

        for rule in self.rules:
            value = rule.evaluate(signals)
            if value > 0:
                total_score += value
                triggered.append(rule.name)

        return {
            "risk_score": total_score,
            "triggered_rules": triggered
        }
