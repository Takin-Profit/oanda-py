from enum import Enum


class AccountFinancingMode(str, Enum):
    DAILY = "DAILY"
    NO_FINANCING = "NO_FINANCING"
    SECOND_BY_SECOND = "SECOND_BY_SECOND"

    def __str__(self) -> str:
        return str(self.value)
