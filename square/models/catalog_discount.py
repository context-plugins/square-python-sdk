from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.catalog_discount_modify_tax_basis import CatalogDiscountModifyTaxBasisOrStr
from .enums.catalog_discount_type import CatalogDiscountTypeOrStr
from .money import Money, MoneyDict


class CatalogDiscount(SdkBaseModel):
    """A discount applicable to items."""

    name: OptionalNullable[str] = UNSET
    """The discount name. This is a searchable attribute for use in applicable query filters, and its value length is of
    Unicode code points."""

    discount_type: Optional[CatalogDiscountTypeOrStr] = UNSET
    """How to apply a CatalogDiscount to a CatalogItem."""

    percentage: OptionalNullable[str] = UNSET
    """The percentage of the discount as a string representation of a decimal number, using a ``.`` as the decimal
    separator and without a ``%`` sign. A value of ``7.5`` corresponds to ``7.5%``. Specify a percentage of ``0`` if
    ``discount_type`` is ``VARIABLE_PERCENTAGE``.

    Do not use this field for amount-based or variable discounts."""

    amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    pin_required: OptionalNullable[bool] = UNSET
    """Indicates whether a mobile staff member needs to enter their PIN to apply the discount to a payment in the Square
    Point of Sale app."""

    label_color: OptionalNullable[str] = UNSET
    """The color of the discount display label in the Square Point of Sale app. This must be a valid hex color code."""

    modify_tax_basis: Optional[CatalogDiscountModifyTaxBasisOrStr] = UNSET
    maximum_amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class CatalogDiscountDict(TypedDict):
    name: NotRequired[str | None]
    discount_type: NotRequired[CatalogDiscountTypeOrStr]
    percentage: NotRequired[str | None]
    amount_money: NotRequired[MoneyDict]
    pin_required: NotRequired[bool | None]
    label_color: NotRequired[str | None]
    modify_tax_basis: NotRequired[CatalogDiscountModifyTaxBasisOrStr]
    maximum_amount_money: NotRequired[MoneyDict]
