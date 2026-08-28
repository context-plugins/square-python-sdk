from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OauthAuthorizationRevokedEventRevokerType(str, Enum):
    """Defines the possible types for the revoking client."""

    APPLICATION = "APPLICATION"
    """The application that requested access to a merchant's data."""

    MERCHANT = "MERCHANT"
    """The admin for the merchant."""

    SQUARE = "SQUARE"
    """An internal Square employee."""

    __str__ = str.__str__


OauthAuthorizationRevokedEventRevokerTypeOrStr: TypeAlias = Annotated[
    OauthAuthorizationRevokedEventRevokerType | str, open_enum_validator(OauthAuthorizationRevokedEventRevokerType)
]
