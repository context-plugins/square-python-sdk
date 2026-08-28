from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LoyaltyProgramAccrualRuleItemVariationData(SdkBaseModel):
    """Represents additional data for rules with the ``ITEM_VARIATION`` accrual type."""

    item_variation_id: str
    """The ID of the ``ITEM_VARIATION`` `catalog object <entity:CatalogObject>`__ that buyers can purchase to earn
    points."""


class LoyaltyProgramAccrualRuleItemVariationDataDict(TypedDict):
    item_variation_id: str
