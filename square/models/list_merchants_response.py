from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .merchant import Merchant, MerchantDict


class ListMerchantsResponse(SdkBaseModel):
    """The response object returned by the `ListMerchant <api-endpoint:Merchants-ListMerchants>`__ endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""

    merchant: Optional[list[Merchant]] = UNSET
    """The requested ``Merchant`` entities."""

    cursor: Optional[int] = UNSET
    """If the response is truncated, the cursor to use in next request to fetch next set of objects."""


class ListMerchantsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    merchant: NotRequired[list[Merchant | MerchantDict]]
    cursor: NotRequired[int]
