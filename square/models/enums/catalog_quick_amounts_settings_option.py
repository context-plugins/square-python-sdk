from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogQuickAmountsSettingsOption(str, Enum):
    """Determines a seller's option on Quick Amounts feature."""

    DISABLED = "DISABLED"
    """Option for seller to disable Quick Amounts."""

    MANUAL = "MANUAL"
    """Option for seller to choose manually created Quick Amounts."""

    AUTO = "AUTO"
    """Option for seller to choose automatically created Quick Amounts."""

    __str__ = str.__str__


CatalogQuickAmountsSettingsOptionOrStr: TypeAlias = Annotated[
    CatalogQuickAmountsSettingsOption | str, open_enum_validator(CatalogQuickAmountsSettingsOption)
]
