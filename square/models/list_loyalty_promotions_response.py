from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .loyalty_promotion import LoyaltyPromotion, LoyaltyPromotionDict


class ListLoyaltyPromotionsResponse(SdkBaseModel):
    """Represents a `ListLoyaltyPromotions <api-endpoint:Loyalty-ListLoyaltyPromotions>`__ response. One of
    ``loyalty_promotions``, an empty object, or ``errors`` is present in the response. If additional results are
    available, the ``cursor`` field is also present along with ``loyalty_promotions``."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    loyalty_promotions: Optional[list[LoyaltyPromotion]] = UNSET
    """The retrieved loyalty promotions."""

    cursor: Optional[str] = UNSET
    """The cursor to use in your next call to this endpoint to retrieve the next page of results for your original
    request. This field is present only if the request succeeded and additional results are available. For more
    information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class ListLoyaltyPromotionsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    loyalty_promotions: NotRequired[list[LoyaltyPromotion | LoyaltyPromotionDict]]
    cursor: NotRequired[str]
