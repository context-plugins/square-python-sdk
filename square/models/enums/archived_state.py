from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ArchivedState(str, Enum):
    """Defines the values for the ``archived_state`` query expression used in `SearchCatalogItems
    <api-endpoint:Catalog-SearchCatalogItems>`__ to return the archived, not archived or either type of catalog
    items."""

    ARCHIVED_STATE_NOT_ARCHIVED = "ARCHIVED_STATE_NOT_ARCHIVED"
    """Requested items are not archived with the ``is_archived`` attribute set to ``false``."""

    ARCHIVED_STATE_ARCHIVED = "ARCHIVED_STATE_ARCHIVED"
    """Requested items are archived with the ``is_archived`` attribute set to ``true``."""

    ARCHIVED_STATE_ALL = "ARCHIVED_STATE_ALL"
    """Requested items can be archived or not archived."""

    __str__ = str.__str__


ArchivedStateOrStr: TypeAlias = Annotated[ArchivedState | str, open_enum_validator(ArchivedState)]
