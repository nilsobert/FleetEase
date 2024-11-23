from dataclasses import dataclass

@dataclass
class Usage:
    cpu: float
    ram: float
    decision_time: float