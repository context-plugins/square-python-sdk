from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.payment_options_delay_action import PaymentOptionsDelayActionOrStr


class PaymentOptions(SdkBaseModel):
    autocomplete: OptionalNullable[bool] = UNSET
    """Indicates whether the ``Payment`` objects created from this ``TerminalCheckout`` are automatically ``COMPLETED``
    or left in an ``APPROVED`` state for later modification.

    Default: true"""

    delay_duration: OptionalNullable[str] = UNSET
    """The duration of time after the payment's creation when Square automatically resolves the payment. This automatic
    resolution applies only to payments that do not reach a terminal state (``COMPLETED`` or ``CANCELED``) before the
    ``delay_duration`` time period.

    This parameter should be specified as a time duration, in RFC 3339 format, with a minimum value of 1 minute and a
    maximum value of 36 hours. This feature is only supported for card payments, and all payments will be considered
    card-present.

    This parameter can only be set for a delayed capture payment (``autocomplete=false``). For more information, see
    `Delayed Capture
    <https://developer.squareup.com/docs/payments-api/take-payments/card-payments/delayed-capture#time-threshold>`__.

    Default: "PT36H" (36 hours) from the creation time"""

    accept_partial_authorization: OptionalNullable[bool] = UNSET
    """If set to ``true`` and charging a Square Gift Card, a payment might be returned with ``amount_money`` equal to
    less than what was requested. For example, a request for $20 when charging a Square Gift Card with a balance of $5
    results in an APPROVED payment of $5. You might choose to prompt the buyer for an additional payment to cover the
    remainder or cancel the Gift Card payment.

    This parameter can only be set for a delayed capture payment (``autocomplete=false``).

    For more information, see `Take Partial Payments
    <https://developer.squareup.com/docs/payments-api/take-payments/card-payments/partial-payments-with-gift-cards>`__.

    Default: false"""

    delay_action: Optional[PaymentOptionsDelayActionOrStr] = UNSET
    """Describes the action to be applied to a delayed capture payment when the delay_duration has elapsed."""


class PaymentOptionsDict(TypedDict):
    autocomplete: NotRequired[bool | None]
    delay_duration: NotRequired[str | None]
    accept_partial_authorization: NotRequired[bool | None]
    delay_action: NotRequired[PaymentOptionsDelayActionOrStr]
