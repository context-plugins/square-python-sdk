from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DataCollectionOptionsInputType(str, Enum):
    """Describes the input type of the data."""

    EMAIL = "EMAIL"
    """This value is used to represent an input text that contains a email validation on the client."""

    PHONE_NUMBER = "PHONE_NUMBER"
    """This value is used to represent an input text that contains a phone number validation on the client."""

    __str__ = str.__str__


DataCollectionOptionsInputTypeOrStr: TypeAlias = Annotated[
    DataCollectionOptionsInputType | str, open_enum_validator(DataCollectionOptionsInputType)
]
