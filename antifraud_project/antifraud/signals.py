from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class DistributionSignal:
    """
    Standard antifraud signals (open & explainable)
    """
    coupon_id: str
    distributor_id: str
    timestamp: datetime
    gps_lat: Optional[float] = None
    gps_lon: Optional[float] = None
    device_id: Optional[str] = None
