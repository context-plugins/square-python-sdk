from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DisputeState(str, Enum):
    """The list of possible dispute states."""

    INQUIRY_EVIDENCE_REQUIRED = "INQUIRY_EVIDENCE_REQUIRED"
    """The initial state of an inquiry with evidence required"""

    INQUIRY_PROCESSING = "INQUIRY_PROCESSING"
    """Inquiry evidence has been submitted and the bank is processing the inquiry"""

    INQUIRY_CLOSED = "INQUIRY_CLOSED"
    """The inquiry is complete"""

    EVIDENCE_REQUIRED = "EVIDENCE_REQUIRED"
    """The initial state of a dispute with evidence required"""

    PROCESSING = "PROCESSING"
    """Dispute evidence has been submitted and the bank is processing the dispute"""

    WON = "WON"
    """The bank has completed processing the dispute and the seller has won"""

    LOST = "LOST"
    """The bank has completed processing the dispute and the seller has lost"""

    ACCEPTED = "ACCEPTED"
    """The seller has accepted the dispute"""

    __str__ = str.__str__


DisputeStateOrStr: TypeAlias = Annotated[DisputeState | str, open_enum_validator(DisputeState)]
