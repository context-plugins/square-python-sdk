from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .custom_attribute_event_data import CustomAttributeEventData, CustomAttributeEventDataDict


class LocationCustomAttributeVisibleDeletedEvent(SdkBaseModel):
    """Published when a location `custom attribute <entity:CustomAttribute>`__ that is visible to the subscribing
    application is deleted. A notification is sent when:
    - Your application deletes a custom attribute owned by your application, regardless of the ``visibility`` setting.
    - Any application deletes a custom attribute whose ``visibility`` is ``VISIBILITY_READ_ONLY``
    or ``VISIBILITY_READ_WRITE_VALUES``.

    Custom attributes set to ``VISIBILITY_READ_WRITE_VALUES`` can be deleted by any application, but those set to
    ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_HIDDEN`` can only be deleted by the owner. Custom attributes are owned by
    the application that created the corresponding `custom attribute definition
    <entity:CustomAttributeDefinition>`__."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the seller associated with the event that triggered the event notification."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of this event. The value is ``"location.custom_attribute.visible.deleted"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event notification."""

    created_at: Optional[str] = UNSET
    """The timestamp that indicates when the event notification was created, in RFC 3339 format."""

    data: Optional[CustomAttributeEventData] = UNSET


class LocationCustomAttributeVisibleDeletedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[CustomAttributeEventData | CustomAttributeEventDataDict]
