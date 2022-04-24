from enum import Enum

class ReportType(Enum):
    PAYMENT = 1
    CLAIM = 2

    def __str__(self):
        if self.CLAIM:
            return "claim"
        if self.PAYMENT:
            return "payment"