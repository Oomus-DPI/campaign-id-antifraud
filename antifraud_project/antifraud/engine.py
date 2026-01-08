from typing import List
from .signals import DistributionSignal
from .rules import (
    TooFastDistributionRule,
    SameDeviceMultipleCouponsRule
)
from .scorer import RiskScorer


class AntiFraudEngine:
    """
    Open Core antifraud engine (rule-based & explainable)
    """

    def __init__(self):
        rules = [
            TooFastDistributionRule(),
            SameDeviceMultipleCouponsRule()
        ]
        self.scorer = RiskScorer(rules)

    def analyze(self, signals: List[DistributionSignal]):
        """
        Analyze a set of distribution signals and return risk assessment
        """
        return self.scorer.score(signals)
