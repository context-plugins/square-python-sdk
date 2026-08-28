from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reference_type import ReferenceTypeOrStr


class Reference(SdkBaseModel):
    type_: Optional[ReferenceTypeOrStr] = Field(default=UNSET, alias="type")
    """The type of platform concept a channel can represent."""

    id: Optional[str] = UNSET
    """The id of the entity a channel is associated with."""


class ReferenceDict(TypedDict):
    type_: NotRequired[ReferenceTypeOrStr]
    id: NotRequired[str]
