from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CardIssuerAlert(str, Enum):
    """Indicates the type of issuer alert for a `card on file <entity:Card>`__."""

    ISSUER_ALERT_CARD_CLOSED = "ISSUER_ALERT_CARD_CLOSED"
    """The underlying account of the card was closed, which is a strong signal that future charges to the card are
    likely to fail."""

    __str__ = str.__str__


CardIssuerAlertOrStr: TypeAlias = Annotated[CardIssuerAlert | str, open_enum_validator(CardIssuerAlert)]
