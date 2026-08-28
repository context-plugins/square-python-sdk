from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayoutType(str, Enum):
    """The type of payout: “BATCH” or “SIMPLE”. BATCH payouts include a list of payout entries that can be considered
    settled. SIMPLE payouts do not have any payout entries associated with them and will show up as one of the payout
    entries in a future BATCH payout."""

    BATCH = "BATCH"
    """Payouts that include a list of payout entries that can be considered settled."""

    SIMPLE = "SIMPLE"
    """Payouts that do not have any payout entries associated with them and will show up as one of the payout entries in
    a future BATCH payout."""

    __str__ = str.__str__


PayoutTypeOrStr: TypeAlias = Annotated[PayoutType | str, open_enum_validator(PayoutType)]
