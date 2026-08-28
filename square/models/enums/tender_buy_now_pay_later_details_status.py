from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TenderBuyNowPayLaterDetailsStatus(str, Enum):
    AUTHORIZED = "AUTHORIZED"
    """The buy now pay later payment has been authorized but not yet captured."""

    CAPTURED = "CAPTURED"
    """The buy now pay later payment was authorized and subsequently captured (i.e., completed)."""

    VOIDED = "VOIDED"
    """The buy now pay later payment was authorized and subsequently voided (i.e., canceled)."""

    FAILED = "FAILED"
    """The buy now pay later payment failed."""

    __str__ = str.__str__


TenderBuyNowPayLaterDetailsStatusOrStr: TypeAlias = Annotated[
    TenderBuyNowPayLaterDetailsStatus | str, open_enum_validator(TenderBuyNowPayLaterDetailsStatus)
]
