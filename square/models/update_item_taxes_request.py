from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class UpdateItemTaxesRequest(SdkBaseModel):
    item_ids: list[str]
    """IDs for the CatalogItems associated with the CatalogTax objects being updated. No more than 1,000 IDs may be
    provided."""

    taxes_to_enable: OptionalNullable[list[str]] = UNSET
    """IDs of the CatalogTax objects to enable. At least one of ``taxes_to_enable`` or ``taxes_to_disable`` must be
    specified."""

    taxes_to_disable: OptionalNullable[list[str]] = UNSET
    """IDs of the CatalogTax objects to disable. At least one of ``taxes_to_enable`` or ``taxes_to_disable`` must be
    specified."""


class UpdateItemTaxesRequestDict(TypedDict):
    item_ids: list[str]
    taxes_to_enable: NotRequired[list[str] | None]
    taxes_to_disable: NotRequired[list[str] | None]
