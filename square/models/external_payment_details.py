from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class ExternalPaymentDetails(SdkBaseModel):
    """Stores details about an external payment. Contains only non-confidential information. For more information, see
    `Take External Payments <https://developer.squareup.com/docs/payments-api/take-payments/external-payments>`__."""

    type_: str = Field(alias="type")
    r"""The type of external payment the seller received. It can be one of the following:
    - CHECK - Paid using a physical check.
    - BANK_TRANSFER - Paid using external bank transfer.
    - OTHER\_GIFT\_CARD - Paid using a non-Square gift card.
    - CRYPTO - Paid using a crypto currency.
    - SQUARE_CASH - Paid using Square Cash App.
    - SOCIAL - Paid using peer-to-peer payment applications.
    - EXTERNAL - A third-party application gathered this payment outside of Square.
    - EMONEY - Paid using an E-money provider.
    - CARD - A credit or debit card that Square does not support.
    - STORED_BALANCE - Use for house accounts, store credit, and so forth.
    - FOOD_VOUCHER - Restaurant voucher provided by employers to employees to pay for meals
    - OTHER - A type not listed here."""

    source: str
    """A description of the external payment source. For example, "Food Delivery Service"."""

    source_id: OptionalNullable[str] = UNSET
    """An ID to associate the payment to its originating source."""

    source_fee_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class ExternalPaymentDetailsDict(TypedDict):
    type_: str
    source: str
    source_id: NotRequired[str | None]
    source_fee_money: NotRequired[Money | MoneyDict]
