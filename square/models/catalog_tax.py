from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.tax_calculation_phase import TaxCalculationPhaseOrStr
from .enums.tax_inclusion_type import TaxInclusionTypeOrStr


class CatalogTax(SdkBaseModel):
    """A tax applicable to an item."""

    name: OptionalNullable[str] = UNSET
    """The tax's name. This is a searchable attribute for use in applicable query filters, and its value length is of
    Unicode code points."""

    calculation_phase: Optional[TaxCalculationPhaseOrStr] = UNSET
    """When to calculate the taxes due on a cart."""

    inclusion_type: Optional[TaxInclusionTypeOrStr] = UNSET
    """Whether to the tax amount should be additional to or included in the CatalogItem price."""

    percentage: OptionalNullable[str] = UNSET
    """The percentage of the tax in decimal form, using a ``'.'`` as the decimal separator and without a ``'%'`` sign. A
    value of ``7.5`` corresponds to 7.5%. For a location-specific tax rate, contact the tax authority of the location or
    a tax consultant."""

    applies_to_custom_amounts: OptionalNullable[bool] = UNSET
    """If ``true``, the fee applies to custom amounts entered into the Square Point of Sale app that are not associated
    with a particular ``CatalogItem``."""

    enabled: OptionalNullable[bool] = UNSET
    """A Boolean flag to indicate whether the tax is displayed as enabled (``true``) in the Square Point of Sale app or
    not (``false``)."""

    applies_to_product_set_id: OptionalNullable[str] = UNSET
    """The ID of a ``CatalogProductSet`` object. If set, the tax is applicable to all products in the product set."""


class CatalogTaxDict(TypedDict):
    name: NotRequired[str | None]
    calculation_phase: NotRequired[TaxCalculationPhaseOrStr]
    inclusion_type: NotRequired[TaxInclusionTypeOrStr]
    percentage: NotRequired[str | None]
    applies_to_custom_amounts: NotRequired[bool | None]
    enabled: NotRequired[bool | None]
    applies_to_product_set_id: NotRequired[str | None]
