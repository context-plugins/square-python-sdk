from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class BulkSwapPlanResponse(SdkBaseModel):
    """Defines output parameters in a response of the `BulkSwapPlan <api-endpoint:Subscriptions-BulkSwapPlan>`__
    endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered during the request."""

    affected_subscriptions: Optional[int] = UNSET
    """The number of affected subscriptions."""


class BulkSwapPlanResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    affected_subscriptions: NotRequired[int]
