from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RegisterDomainResponseStatus(str, Enum):
    """The status of the domain registration."""

    PENDING = "PENDING"
    """The domain is added, but not verified."""

    VERIFIED = "VERIFIED"
    """The domain is added and verified. It can be used to accept Apple Pay transactions."""

    __str__ = str.__str__


RegisterDomainResponseStatusOrStr: TypeAlias = Annotated[
    RegisterDomainResponseStatus | str, open_enum_validator(RegisterDomainResponseStatus)
]
