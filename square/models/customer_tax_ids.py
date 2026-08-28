from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CustomerTaxIds(SdkBaseModel):
    """Represents the tax ID associated with a `customer profile <entity:Customer>`__. The corresponding ``tax_ids``
    field is available only for customers of sellers in EU countries or the United Kingdom. For more information, see
    `Customer tax IDs <https://developer.squareup.com/docs/customers-api/what-it-does#customer-tax-ids>`__."""

    eu_vat: OptionalNullable[str] = UNSET
    """The EU VAT identification number for the customer. For example, ``IE3426675K``. The ID can contain alphanumeric
    characters only."""


class CustomerTaxIdsDict(TypedDict):
    eu_vat: NotRequired[str | None]
