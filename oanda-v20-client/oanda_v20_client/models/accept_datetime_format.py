from enum import Enum


class AcceptDatetimeFormat(str, Enum):
    RFC3339 = "RFC3339"
    UNIX = "UNIX"

    def __str__(self) -> str:
        return str(self.value)
