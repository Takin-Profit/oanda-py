from enum import Enum


class FixedPriceOrderReason(str, Enum):
    PLATFORM_ACCOUNT_MIGRATION = "PLATFORM_ACCOUNT_MIGRATION"

    def __str__(self) -> str:
        return str(self.value)
