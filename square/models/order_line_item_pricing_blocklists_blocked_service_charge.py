from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class OrderLineItemPricingBlocklistsBlockedServiceCharge(SdkBaseModel):
    """A service charge to block from applying to a line item. The service charge must be identified by either
    ``service_charge_uid`` or ``service_charge_catalog_object_id``, but not both."""

    uid: OptionalNullable[str] = UNSET
    """A unique ID of the ``BlockedServiceCharge`` within the order."""

    service_charge_uid: OptionalNullable[str] = UNSET
    """The ``uid`` of the service charge that should be blocked. Use this field to block ad hoc service charges. For
    catalog service charges, use the ``service_charge_catalog_object_id`` field."""

    service_charge_catalog_object_id: OptionalNullable[str] = UNSET
    """The ``catalog_object_id`` of the service charge that should be blocked. Use this field to block catalog service
    charges. For ad hoc service charges, use the ``service_charge_uid`` field."""


class OrderLineItemPricingBlocklistsBlockedServiceChargeDict(TypedDict):
    uid: NotRequired[str | None]
    service_charge_uid: NotRequired[str | None]
    service_charge_catalog_object_id: NotRequired[str | None]
