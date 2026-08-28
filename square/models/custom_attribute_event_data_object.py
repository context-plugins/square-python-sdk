from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_attribute import CustomAttribute, CustomAttributeDict


class CustomAttributeEventDataObject(SdkBaseModel):
    custom_attribute: Optional[CustomAttribute] = UNSET
    """A custom attribute value. Each custom attribute value has a corresponding ``CustomAttributeDefinition``
    object."""


class CustomAttributeEventDataObjectDict(TypedDict):
    custom_attribute: NotRequired[CustomAttribute | CustomAttributeDict]
