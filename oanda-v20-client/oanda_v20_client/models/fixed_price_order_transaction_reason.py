from enum import Enum


class FixedPriceOrderTransactionReason(str, Enum):
    PLATFORM_ACCOUNT_MIGRATION = "PLATFORM_ACCOUNT_MIGRATION"

    def __str__(self) -> str:
        return str(self.value)
