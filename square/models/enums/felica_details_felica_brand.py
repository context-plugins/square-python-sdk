from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FelicaDetailsFelicaBrand(str, Enum):
    """A Felica card's "sub-brand"--the actual brand on the Felica card"""

    UNKNOWN = "UNKNOWN"
    FELICA_ID = "FELICA_ID"
    FELICA_TRANSPORTATION = "FELICA_TRANSPORTATION"
    FELICA_QP = "FELICA_QP"

    __str__ = str.__str__


FelicaDetailsFelicaBrandOrStr: TypeAlias = Annotated[
    FelicaDetailsFelicaBrand | str, open_enum_validator(FelicaDetailsFelicaBrand)
]
