from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .confirmation_options import ConfirmationOptions, ConfirmationOptionsDict
from .data_collection_options import DataCollectionOptions, DataCollectionOptionsDict
from .device_metadata import DeviceMetadata, DeviceMetadataDict
from .enums.action_cancel_reason import ActionCancelReasonOrStr
from .enums.terminal_action_action_type import TerminalActionActionTypeOrStr
from .qr_code_options import QrCodeOptions, QrCodeOptionsDict
from .receipt_options import ReceiptOptions, ReceiptOptionsDict
from .save_card_options import SaveCardOptions, SaveCardOptionsDict
from .select_options import SelectOptions, SelectOptionsDict
from .signature_options import SignatureOptions, SignatureOptionsDict


class TerminalAction(SdkBaseModel):
    """Represents an action processed by the Square Terminal."""

    id: Optional[str] = UNSET
    """A unique ID for this ``TerminalAction``."""

    device_id: OptionalNullable[str] = UNSET
    """The unique Id of the device intended for this ``TerminalAction``. The Id can be retrieved from /v2/devices
    api."""

    deadline_duration: OptionalNullable[str] = UNSET
    """The duration as an RFC 3339 duration, after which the action will be automatically canceled. TerminalActions that
    are ``PENDING`` will be automatically ``CANCELED`` and have a cancellation reason of ``TIMED_OUT``

    Default: 5 minutes from creation

    Maximum: 5 minutes"""

    status: Optional[str] = UNSET
    """The status of the ``TerminalAction``. Options: ``PENDING``, ``IN_PROGRESS``, ``CANCEL_REQUESTED``, ``CANCELED``,
    ``COMPLETED``"""

    cancel_reason: Optional[ActionCancelReasonOrStr] = UNSET
    created_at: Optional[str] = UNSET
    """The time when the ``TerminalAction`` was created as an RFC 3339 timestamp."""

    updated_at: Optional[str] = UNSET
    """The time when the ``TerminalAction`` was last updated as an RFC 3339 timestamp."""

    app_id: Optional[str] = UNSET
    """The ID of the application that created the action."""

    location_id: Optional[str] = UNSET
    """The location id the action is attached to, if a link can be made."""

    type_: Optional[TerminalActionActionTypeOrStr] = Field(default=UNSET, alias="type")
    """Describes the type of this unit and indicates which field contains the unit information. This is an ‘open’
    enum."""

    qr_code_options: Optional[QrCodeOptions] = UNSET
    """Fields to describe the action that displays QR-Codes."""

    save_card_options: Optional[SaveCardOptions] = UNSET
    """Describes save-card action fields."""

    signature_options: Optional[SignatureOptions] = UNSET
    confirmation_options: Optional[ConfirmationOptions] = UNSET
    receipt_options: Optional[ReceiptOptions] = UNSET
    """Describes receipt action fields."""

    data_collection_options: Optional[DataCollectionOptions] = UNSET
    select_options: Optional[SelectOptions] = UNSET
    device_metadata: Optional[DeviceMetadata] = UNSET
    await_next_action: OptionalNullable[bool] = UNSET
    """Indicates the action will be linked to another action and requires a waiting dialog to be displayed instead of
    returning to the idle screen on completion of the action.

    Only supported on SIGNATURE, CONFIRMATION, DATA_COLLECTION, and SELECT types."""

    await_next_action_duration: OptionalNullable[str] = UNSET
    """The timeout duration of the waiting dialog as an RFC 3339 duration, after which the waiting dialog will no longer
    be displayed and the Terminal will return to the idle screen.

    Default: 5 minutes from when the waiting dialog is displayed

    Maximum: 5 minutes"""


class TerminalActionDict(TypedDict):
    id: NotRequired[str]
    device_id: NotRequired[str | None]
    deadline_duration: NotRequired[str | None]
    status: NotRequired[str]
    cancel_reason: NotRequired[ActionCancelReasonOrStr]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    app_id: NotRequired[str]
    location_id: NotRequired[str]
    type_: NotRequired[TerminalActionActionTypeOrStr]
    qr_code_options: NotRequired[QrCodeOptionsDict]
    save_card_options: NotRequired[SaveCardOptionsDict]
    signature_options: NotRequired[SignatureOptionsDict]
    confirmation_options: NotRequired[ConfirmationOptionsDict]
    receipt_options: NotRequired[ReceiptOptionsDict]
    data_collection_options: NotRequired[DataCollectionOptionsDict]
    select_options: NotRequired[SelectOptionsDict]
    device_metadata: NotRequired[DeviceMetadataDict]
    await_next_action: NotRequired[bool | None]
    await_next_action_duration: NotRequired[str | None]
