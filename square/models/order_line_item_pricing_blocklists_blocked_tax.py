from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class OrderLineItemPricingBlocklistsBlockedTax(SdkBaseModel):
    """A tax to block from applying to a line item. The tax must be identified by either ``tax_uid`` or
    ``tax_catalog_object_id``, but not both."""

    uid: OptionalNullable[str] = UNSET
    """A unique ID of the ``BlockedTax`` within the order."""

    tax_uid: OptionalNullable[str] = UNSET
    """The ``uid`` of the tax that should be blocked. Use this field to block ad hoc taxes. For catalog, taxes use the
    ``tax_catalog_object_id`` field."""

    tax_catalog_object_id: OptionalNullable[str] = UNSET
    """The ``catalog_object_id`` of the tax that should be blocked. Use this field to block catalog taxes. For ad hoc
    taxes, use the ``tax_uid`` field."""


class OrderLineItemPricingBlocklistsBlockedTaxDict(TypedDict):
    uid: NotRequired[str | None]
    tax_uid: NotRequired[str | None]
    tax_catalog_object_id: NotRequired[str | None]
