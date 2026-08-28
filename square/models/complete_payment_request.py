from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CompletePaymentRequest(SdkBaseModel):
    """Describes a request to complete (capture) a payment using `CompletePayment
    <api-endpoint:Payments-CompletePayment>`__.

    By default, payments are set to ``autocomplete`` immediately after they are created. To complete payments manually,
    set ``autocomplete`` to ``false``."""

    version_token: OptionalNullable[str] = UNSET
    """Used for optimistic concurrency. This opaque token identifies the current ``Payment`` version that the caller
    expects. If the server has a different version of the Payment, the update fails and a response with a
    VERSION_MISMATCH error is returned."""


class CompletePaymentRequestDict(TypedDict):
    version_token: NotRequired[str | None]
