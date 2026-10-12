from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_object_reference import CatalogObjectReference, CatalogObjectReferenceDict


class LoyaltyProgramRewardTier(SdkBaseModel):
    """Represents a reward tier in a loyalty program. A reward tier defines how buyers can redeem points for a reward,
    such as the number of points required and the value and scope of the discount. A loyalty program can offer multiple
    reward tiers."""

    id: Optional[str] = UNSET
    """The Square-assigned ID of the reward tier."""

    points: int
    """The points exchanged for the reward tier."""

    name: Optional[str] = UNSET
    """The name of the reward tier."""

    created_at: Optional[str] = UNSET
    """The timestamp when the reward tier was created, in RFC 3339 format."""

    pricing_rule_reference: CatalogObjectReference
    """A reference to a Catalog object at a specific version. In general this is used as an entry point into a graph of
    catalog objects, where the objects exist at a specific version."""


class LoyaltyProgramRewardTierDict(TypedDict):
    id: NotRequired[str]
    points: int
    name: NotRequired[str]
    created_at: NotRequired[str]
    pricing_rule_reference: CatalogObjectReferenceDict
