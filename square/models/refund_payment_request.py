from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .destination_details_cash_refund_details import (
    DestinationDetailsCashRefundDetails,
    DestinationDetailsCashRefundDetailsDict,
)
from .destination_details_external_refund_details import (
    DestinationDetailsExternalRefundDetails,
    DestinationDetailsExternalRefundDetailsDict,
)
from .money import Money, MoneyDict


class RefundPaymentRequest(SdkBaseModel):
    """Describes a request to refund a payment using `RefundPayment <api-endpoint:Refunds-RefundPayment>`__."""

    idempotency_key: str
    """A unique string that identifies this ``RefundPayment`` request. The key can be any valid string but must be
    unique for every ``RefundPayment`` request.

    Keys are limited to a max of 45 characters - however, the number of allowed characters might be less than 45, if
    multi-byte characters are used.

    For more information, see `Idempotency <https://developer.squareup.com/docs/working-with-apis/idempotency>`__."""

    amount_money: Money
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    app_fee_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    payment_id: OptionalNullable[str] = UNSET
    """The unique ID of the payment being refunded. Required when unlinked=false, otherwise must not be set."""

    destination_id: OptionalNullable[str] = UNSET
    """The ID indicating where funds will be refunded to. Required for unlinked refunds. For more information, see
    `Process an Unlinked Refund <https://developer.squareup.com/docs/refunds-api/unlinked-refunds>`__.

    For refunds linked to Square payments, ``destination_id`` is usually omitted; in this case, funds will be returned
    to the original payment source. The field may be specified in order to request a cross-method refund to a gift card.
    For more information, see `Cross-method refunds to gift cards
    <https://developer.squareup.com/docs/payments-api/refund-payments#cross-method-refunds-to-gift-cards>`__."""

    unlinked: OptionalNullable[bool] = UNSET
    """Indicates that the refund is not linked to a Square payment. If set to true, ``destination_id`` and
    ``location_id`` must be supplied while ``payment_id`` must not be provided."""

    location_id: OptionalNullable[str] = UNSET
    """The location ID associated with the unlinked refund. Required for requests specifying ``unlinked=true``.
    Otherwise, if included when ``unlinked=false``, will throw an error."""

    customer_id: OptionalNullable[str] = UNSET
    """The `Customer <entity:Customer>`__ ID of the customer associated with the refund. This is required if the
    ``destination_id`` refers to a card on file created using the Cards API. Only allowed when ``unlinked=true``."""

    reason: OptionalNullable[str] = UNSET
    """A description of the reason for the refund."""

    payment_version_token: OptionalNullable[str] = UNSET
    """Used for optimistic concurrency. This opaque token identifies the current ``Payment`` version that the caller
    expects. If the server has a different version of the Payment, the update fails and a response with a
    VERSION_MISMATCH error is returned. If the versions match, or the field is not provided, the refund proceeds as
    normal."""

    team_member_id: OptionalNullable[str] = UNSET
    """An optional `TeamMember <entity:TeamMember>`__ ID to associate with this refund."""

    cash_details: Optional[DestinationDetailsCashRefundDetails] = UNSET
    """Stores details about a cash refund. Contains only non-confidential information."""

    external_details: Optional[DestinationDetailsExternalRefundDetails] = UNSET
    """Stores details about an external refund. Contains only non-confidential information."""


class RefundPaymentRequestDict(TypedDict):
    idempotency_key: str
    amount_money: Money | MoneyDict
    app_fee_money: NotRequired[Money | MoneyDict]
    payment_id: NotRequired[str | None]
    destination_id: NotRequired[str | None]
    unlinked: NotRequired[bool | None]
    location_id: NotRequired[str | None]
    customer_id: NotRequired[str | None]
    reason: NotRequired[str | None]
    payment_version_token: NotRequired[str | None]
    team_member_id: NotRequired[str | None]
    cash_details: NotRequired[DestinationDetailsCashRefundDetails | DestinationDetailsCashRefundDetailsDict]
    external_details: NotRequired[DestinationDetailsExternalRefundDetails | DestinationDetailsExternalRefundDetailsDict]
