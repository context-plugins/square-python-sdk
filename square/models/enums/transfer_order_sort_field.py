from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransferOrderSortField(str, Enum):
    """Fields that can be used for sorting `TransferOrder <entity:TransferOrder>`__s in search results. Used with
    `SearchTransferOrders <api-endpoint:TransferOrders-SearchTransferOrders>`__ to control the order of returned
    results."""

    CREATED_AT = "CREATED_AT"
    """Sort by creation date (created_at field). Useful for:
    - Finding newest transfers
    - Chronological order processing
    - Historical analysis
    - Auditing transfer patterns"""

    UPDATED_AT = "UPDATED_AT"
    """Sort by last update date (updated_at field). Useful for:
    - Finding recently modified transfers
    - Tracking status changes
    - Monitoring receiving progress
    - Synchronizing with external systems"""

    __str__ = str.__str__


TransferOrderSortFieldOrStr: TypeAlias = Annotated[
    TransferOrderSortField | str, open_enum_validator(TransferOrderSortField)
]
