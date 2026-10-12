from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.customer_creation_source import CustomerCreationSourceOrStr
from .enums.customer_inclusion_exclusion import CustomerInclusionExclusionOrStr


class CustomerCreationSourceFilter(SdkBaseModel):
    """The creation source filter.

    If one or more creation sources are set, customer profiles are included in, or excluded from, the result if they
    match at least one of the filter criteria."""

    values: OptionalNullable[list[CustomerCreationSourceOrStr]] = UNSET
    """The list of creation sources used as filtering criteria. See `CustomerCreationSource
    <#type-customercreationsource>`__ for possible values"""

    rule: Optional[CustomerInclusionExclusionOrStr] = UNSET
    """Indicates whether customers should be included in, or excluded from, the result set when they match the filtering
    criteria."""


class CustomerCreationSourceFilterDict(TypedDict):
    values: NotRequired[list[CustomerCreationSourceOrStr] | None]
    rule: NotRequired[CustomerInclusionExclusionOrStr]
