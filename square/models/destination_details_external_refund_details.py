from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class DestinationDetailsExternalRefundDetails(SdkBaseModel):
    """Stores details about an external refund. Contains only non-confidential information."""

    type_: str = Field(alias="type")
    r"""The type of external refund the seller paid to the buyer. It can be one of the following:
    - CHECK - Refunded using a physical check.
    - BANK_TRANSFER - Refunded using external bank transfer.
    - OTHER\_GIFT\_CARD - Refunded using a non-Square gift card.
    - CRYPTO - Refunded using a crypto currency.
    - SQUARE_CASH - Refunded using Square Cash App.
    - SOCIAL - Refunded using peer-to-peer payment applications.
    - EXTERNAL - A third-party application gathered this refund outside of Square.
    - EMONEY - Refunded using an E-money provider.
    - CARD - A credit or debit card that Square does not support.
    - STORED_BALANCE - Use for house accounts, store credit, and so forth.
    - FOOD_VOUCHER - Restaurant voucher provided by employers to employees to pay for meals
    - OTHER - A type not listed here."""

    source: str
    """A description of the external refund source. For example, "Food Delivery Service"."""

    source_id: OptionalNullable[str] = UNSET
    """An ID to associate the refund to its originating source."""


class DestinationDetailsExternalRefundDetailsDict(TypedDict):
    type_: str
    source: str
    source_id: NotRequired[str | None]
