from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .destination_details_card_refund_details import (
    DestinationDetailsCardRefundDetails,
    DestinationDetailsCardRefundDetailsDict,
)
from .destination_details_cash_refund_details import (
    DestinationDetailsCashRefundDetails,
    DestinationDetailsCashRefundDetailsDict,
)
from .destination_details_external_refund_details import (
    DestinationDetailsExternalRefundDetails,
    DestinationDetailsExternalRefundDetailsDict,
)


class DestinationDetails(SdkBaseModel):
    """Details about a refund's destination."""

    card_details: Optional[DestinationDetailsCardRefundDetails] = UNSET
    cash_details: Optional[DestinationDetailsCashRefundDetails] = UNSET
    """Stores details about a cash refund. Contains only non-confidential information."""

    external_details: Optional[DestinationDetailsExternalRefundDetails] = UNSET
    """Stores details about an external refund. Contains only non-confidential information."""


class DestinationDetailsDict(TypedDict):
    card_details: NotRequired[DestinationDetailsCardRefundDetailsDict]
    cash_details: NotRequired[DestinationDetailsCashRefundDetailsDict]
    external_details: NotRequired[DestinationDetailsExternalRefundDetailsDict]
