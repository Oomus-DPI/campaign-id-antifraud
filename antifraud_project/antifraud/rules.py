from typing import List
from .signals import DistributionSignal
from datetime import timedelta


class FraudRule:
    """Base class for antifraud rules"""
    name = "base_rule"
    weight = 1

    def evaluate(self, signals: List[DistributionSignal]) -> int:
        """
        Return a risk score increment (0 = no risk)
        """
        return 0


class TooFastDistributionRule(FraudRule):
    name = "too_fast_distribution"
    weight = 3

    def evaluate(self, signals: List[DistributionSignal]) -> int:
        if len(signals) < 2:
            return 0

        signals = sorted(signals, key=lambda s: s.timestamp)
        for i in range(1, len(signals)):
            delta = signals[i].timestamp - signals[i - 1].timestamp
            if delta < timedelta(seconds=30):
                return self.weight
        return 0


class SameDeviceMultipleCouponsRule(FraudRule):
    name = "same_device_multiple_coupons"
    weight = 2

    def evaluate(self, signals: List[DistributionSignal]) -> int:
        devices = [s.device_id for s in signals if s.device_id]
        if len(set(devices)) == 1 and len(devices) > 1:
            return self.weight
        return 0
