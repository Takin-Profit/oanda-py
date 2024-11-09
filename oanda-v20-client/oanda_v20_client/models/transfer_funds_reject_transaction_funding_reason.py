from enum import Enum


class TransferFundsRejectTransactionFundingReason(str, Enum):
    ACCOUNT_TRANSFER = "ACCOUNT_TRANSFER"
    ADJUSTMENT = "ADJUSTMENT"
    CLIENT_FUNDING = "CLIENT_FUNDING"
    DIVISION_MIGRATION = "DIVISION_MIGRATION"
    SITE_MIGRATION = "SITE_MIGRATION"

    def __str__(self) -> str:
        return str(self.value)
