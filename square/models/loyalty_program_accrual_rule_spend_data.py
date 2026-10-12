from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.loyalty_program_accrual_rule_tax_mode import LoyaltyProgramAccrualRuleTaxModeOrStr
from .money import Money, MoneyDict


class LoyaltyProgramAccrualRuleSpendData(SdkBaseModel):
    """Represents additional data for rules with the ``SPEND`` accrual type."""

    amount_money: Money
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    excluded_category_ids: OptionalNullable[list[str]] = UNSET
    """The IDs of any ``CATEGORY`` catalog objects that are excluded from points accrual.

    You can use the `BatchRetrieveCatalogObjects <api-endpoint:Catalog-BatchRetrieveCatalogObjects>`__ endpoint to
    retrieve information about the excluded categories."""

    excluded_item_variation_ids: OptionalNullable[list[str]] = UNSET
    """The IDs of any ``ITEM_VARIATION`` catalog objects that are excluded from points accrual.

    You can use the `BatchRetrieveCatalogObjects <api-endpoint:Catalog-BatchRetrieveCatalogObjects>`__ endpoint to
    retrieve information about the excluded item variations."""

    tax_mode: LoyaltyProgramAccrualRuleTaxModeOrStr
    """Indicates how taxes should be treated when calculating the purchase amount used for loyalty points accrual. This
    setting applies only to ``SPEND`` accrual rules or ``VISIT`` accrual rules that have a minimum spend requirement."""


class LoyaltyProgramAccrualRuleSpendDataDict(TypedDict):
    amount_money: MoneyDict
    excluded_category_ids: NotRequired[list[str] | None]
    excluded_item_variation_ids: NotRequired[list[str] | None]
    tax_mode: LoyaltyProgramAccrualRuleTaxModeOrStr
