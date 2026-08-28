from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RegisterDomainRequest(SdkBaseModel):
    """Defines the parameters that can be included in the body of a request to the `RegisterDomain
    <api-endpoint:ApplePay-RegisterDomain>`__ endpoint."""

    domain_name: str
    """A domain name as described in RFC-1034 that will be registered with ApplePay."""


class RegisterDomainRequestDict(TypedDict):
    domain_name: str
