from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .collected_data import CollectedData, CollectedDataDict
from .enums.data_collection_options_input_type import DataCollectionOptionsInputTypeOrStr


class DataCollectionOptions(SdkBaseModel):
    title: str
    """The title text to display in the data collection flow on the Terminal."""

    body: str
    """The body text to display under the title in the data collection screen flow on the Terminal."""

    input_type: DataCollectionOptionsInputTypeOrStr
    """Describes the input type of the data."""

    collected_data: Optional[CollectedData] = UNSET


class DataCollectionOptionsDict(TypedDict):
    title: str
    body: str
    input_type: DataCollectionOptionsInputTypeOrStr
    collected_data: NotRequired[CollectedData | CollectedDataDict]
