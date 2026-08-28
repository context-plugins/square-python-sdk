from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .fulfillment_recipient import FulfillmentRecipient, FulfillmentRecipientDict


class FulfillmentInStoreDetails(SdkBaseModel):
    """Contains the details necessary to fulfill an in-store order."""

    note: OptionalNullable[str] = UNSET
    """A note to provide additional instructions about the in-store fulfillment displayed in the Square Point of Sale
    application and set by the API."""

    recipient: Optional[FulfillmentRecipient] = UNSET
    """Information about the fulfillment recipient."""

    placed_at: OptionalNullable[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    fulfillment was placed. The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    completed_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    fulfillment was completed. This field is automatically set when the fulfillment ``state`` changes to ``COMPLETED``.
    The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    in_progress_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicates when the seller
    started processing the fulfillment. This field is automatically set when the fulfillment ``state`` changes to
    ``RESERVED``. The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    prepared_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    fulfillment was moved to the ``PREPARED`` state, which indicates that the fulfillment is ready. The timestamp must
    be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""

    canceled_at: Optional[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the
    fulfillment was canceled. This field is automatically set when the fulfillment ``state`` changes to ``CANCELED``.
    The timestamp must be in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z")."""


class FulfillmentInStoreDetailsDict(TypedDict):
    note: NotRequired[str | None]
    recipient: NotRequired[FulfillmentRecipient | FulfillmentRecipientDict]
    placed_at: NotRequired[str | None]
    completed_at: NotRequired[str]
    in_progress_at: NotRequired[str]
    prepared_at: NotRequired[str]
    canceled_at: NotRequired[str]
