from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CatalogStockConversion(SdkBaseModel):
    """Represents the rule of conversion between a stockable `CatalogItemVariation <entity:CatalogItemVariation>`__ and
    a non-stockable sell-by or receive-by ``CatalogItemVariation`` that share the same underlying stock."""

    stockable_item_variation_id: str
    """References to the stockable `CatalogItemVariation <entity:CatalogItemVariation>`__ for this stock conversion.
    Selling, receiving or recounting the non-stockable ``CatalogItemVariation`` defined with a stock conversion results
    in adjustments of this stockable ``CatalogItemVariation``. This immutable field must reference a stockable
    ``CatalogItemVariation`` that shares the parent `CatalogItem <entity:CatalogItem>`__ of the converted
    ``CatalogItemVariation.``"""

    stockable_quantity: str
    """The quantity of the stockable item variation (as identified by ``stockable_item_variation_id``) equivalent to the
    non-stockable item variation quantity (as specified in ``nonstockable_quantity``) as defined by this stock
    conversion. It accepts a decimal number in a string format that can take up to 10 digits before the decimal point
    and up to 5 digits after the decimal point."""

    nonstockable_quantity: str
    """The converted equivalent quantity of the non-stockable `CatalogItemVariation <entity:CatalogItemVariation>`__ in
    its measurement unit. The ``stockable_quantity`` value and this ``nonstockable_quantity`` value together define the
    conversion ratio between stockable item variation and the non-stockable item variation. It accepts a decimal number
    in a string format that can take up to 10 digits before the decimal point and up to 5 digits after the decimal
    point."""


class CatalogStockConversionDict(TypedDict):
    stockable_item_variation_id: str
    stockable_quantity: str
    nonstockable_quantity: str
