from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class OrderLineItemPricingBlocklistsBlockedDiscount(SdkBaseModel):
    """A discount to block from applying to a line item. The discount must be identified by either ``discount_uid`` or
    ``discount_catalog_object_id``, but not both."""

    uid: OptionalNullable[str] = UNSET
    """A unique ID of the ``BlockedDiscount`` within the order."""

    discount_uid: OptionalNullable[str] = UNSET
    """The ``uid`` of the discount that should be blocked. Use this field to block ad hoc discounts. For catalog
    discounts, use the ``discount_catalog_object_id`` field."""

    discount_catalog_object_id: OptionalNullable[str] = UNSET
    """The ``catalog_object_id`` of the discount that should be blocked. Use this field to block catalog discounts. For
    ad hoc discounts, use the ``discount_uid`` field."""


class OrderLineItemPricingBlocklistsBlockedDiscountDict(TypedDict):
    uid: NotRequired[str | None]
    discount_uid: NotRequired[str | None]
    discount_catalog_object_id: NotRequired[str | None]
