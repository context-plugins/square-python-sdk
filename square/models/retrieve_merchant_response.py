from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .merchant import Merchant, MerchantDict


class RetrieveMerchantResponse(SdkBaseModel):
    """The response object returned by the `RetrieveMerchant <api-endpoint:Merchants-RetrieveMerchant>`__ endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""

    merchant: Optional[Merchant] = UNSET
    """Represents a business that sells with Square."""


class RetrieveMerchantResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    merchant: NotRequired[Merchant | MerchantDict]
