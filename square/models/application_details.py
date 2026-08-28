from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.application_details_external_square_product import ApplicationDetailsExternalSquareProductOrStr


class ApplicationDetails(SdkBaseModel):
    """Details about the application that took the payment."""

    square_product: Optional[ApplicationDetailsExternalSquareProductOrStr] = UNSET
    """A list of products to return to external callers."""

    application_id: OptionalNullable[str] = UNSET
    """The Square ID assigned to the application used to take the payment. Application developers can use this
    information to identify payments that their application processed. For example, if a developer uses a custom
    application to process payments, this field contains the application ID from the Developer Dashboard. If a seller
    uses a `Square App Marketplace <https://developer.squareup.com/docs/app-marketplace>`__ application to process
    payments, the field contains the corresponding application ID."""


class ApplicationDetailsDict(TypedDict):
    square_product: NotRequired[ApplicationDetailsExternalSquareProductOrStr]
    application_id: NotRequired[str | None]
