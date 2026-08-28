from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LoyaltyProgramAccrualRuleCategoryData(SdkBaseModel):
    """Represents additional data for rules with the ``CATEGORY`` accrual type."""

    category_id: str
    """The ID of the ``CATEGORY`` `catalog object <entity:CatalogObject>`__ that buyers can purchase to earn points."""


class LoyaltyProgramAccrualRuleCategoryDataDict(TypedDict):
    category_id: str
