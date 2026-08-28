from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TerminalActionActionType(str, Enum):
    """Describes the type of this unit and indicates which field contains the unit information. This is an ‘open’
    enum."""

    QR_CODE = "QR_CODE"
    """The action represents a request to display a QR code. Details are contained in the ``qr_code_options`` object."""

    PING = "PING"
    """The action represents a request to check if the specific device is online or currently active with the merchant
    in question. Does not require an action options value."""

    SAVE_CARD = "SAVE_CARD"
    """Represents a request to save a card for future card-on-file use. Details are contained in the
    ``save_card_options`` object."""

    SIGNATURE = "SIGNATURE"
    """The action represents a request to capture a buyer's signature. Details are contained in the
    ``signature_options`` object."""

    CONFIRMATION = "CONFIRMATION"
    """The action represents a request to collect a buyer's confirmation decision to the displayed terms. Details are
    contained in the ``confirmation_options`` object."""

    RECEIPT = "RECEIPT"
    """The action represents a request to display the receipt screen options. Details are contained in the
    ``receipt_options`` object."""

    DATA_COLLECTION = "DATA_COLLECTION"
    """The action represents a request to collect a buyer's text data. Details are contained in the
    ``data_collection_options`` object."""

    SELECT = "SELECT"
    """The action represents a request to allow the buyer to select from provided options. Details are contained in the
    ``select_options`` object."""

    __str__ = str.__str__


TerminalActionActionTypeOrStr: TypeAlias = Annotated[
    TerminalActionActionType | str, open_enum_validator(TerminalActionActionType)
]
