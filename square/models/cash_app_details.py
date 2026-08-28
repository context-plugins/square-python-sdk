from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class CashAppDetails(SdkBaseModel):
    """Additional details about ``WALLET`` type payments with the ``brand`` of ``CASH_APP``."""

    buyer_full_name: OptionalNullable[str] = UNSET
    """The name of the Cash App account holder."""

    buyer_country_code: OptionalNullable[str] = UNSET
    """The country of the Cash App account holder, in ISO 3166-1-alpha-2 format.

    For possible values, see `Country <entity:Country>`__."""

    buyer_cashtag: Optional[str] = UNSET
    """$Cashtag of the Cash App account holder."""


class CashAppDetailsDict(TypedDict):
    buyer_full_name: NotRequired[str | None]
    buyer_country_code: NotRequired[str | None]
    buyer_cashtag: NotRequired[str]
