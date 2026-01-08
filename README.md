# Campaign ID AntiFraud – Open Core

Rule-based, explainable antifraud engine for health campaign distribution.

**Organization:** oomus-dpi  
**Maintained by:** Oomus

---

## Features

- Transparent antifraud rules
- Risk scoring
- No sensitive data required
- Fully auditable

---

## Example

```python
from antifraud.engine import AntiFraudEngine
from antifraud.signals import DistributionSignal
from datetime import datetime

engine = AntiFraudEngine()
signals = [
    DistributionSignal(
        coupon_id="CDM25-0000001",
        distributor_id="RELAIS-01",
        timestamp=datetime.utcnow(),
        device_id="DEVICE-123"
    )
]

result = engine.analyze(signals)
print(result)
