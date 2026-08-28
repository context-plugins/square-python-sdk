from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.product import ProductOrStr


class SourceApplication(SdkBaseModel):
    """Represents information about the application used to generate a change."""

    product: Optional[ProductOrStr] = UNSET
    """Indicates the Square product used to generate a change."""

    application_id: OptionalNullable[str] = UNSET
    """__Read only__ The Square-assigned ID of the application. This field is used only if the `product
    <entity:Product>`__ type is ``EXTERNAL_API``."""

    name: OptionalNullable[str] = UNSET
    """__Read only__ The display name of the application (for example, ``"Custom Application"`` or ``"Square POS 4.74
    for Android"``)."""


class SourceApplicationDict(TypedDict):
    product: NotRequired[ProductOrStr]
    application_id: NotRequired[str | None]
    name: NotRequired[str | None]
