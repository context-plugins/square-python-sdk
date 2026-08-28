from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .card import Card, CardDict
from .error import Error, ErrorDict


class ListCardsResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `ListCards
    <api-endpoint:Cards-ListCards>`__ endpoint.

    Note: if there are errors processing the request, the card field will not be present."""

    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""

    cards: Optional[list[Card]] = UNSET
    """The requested list of ``Card``s."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If empty, this is the final response.

    See `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more
    information."""


class ListCardsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    cards: NotRequired[list[Card | CardDict]]
    cursor: NotRequired[str]
