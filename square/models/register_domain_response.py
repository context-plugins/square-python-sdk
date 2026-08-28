from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.register_domain_response_status import RegisterDomainResponseStatusOrStr
from .error import Error, ErrorDict


class RegisterDomainResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `RegisterDomain
    <api-endpoint:ApplePay-RegisterDomain>`__ endpoint.

    Either ``errors`` or ``status`` are present in a given response (never both)."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    status: Optional[RegisterDomainResponseStatusOrStr] = UNSET
    """The status of the domain registration."""


class RegisterDomainResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    status: NotRequired[RegisterDomainResponseStatusOrStr]
