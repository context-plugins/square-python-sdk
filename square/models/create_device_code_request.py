from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .device_code import DeviceCode, DeviceCodeDict


class CreateDeviceCodeRequest(SdkBaseModel):
    idempotency_key: str
    """A unique string that identifies this CreateDeviceCode request. Keys can be any valid string but must be unique
    for every CreateDeviceCode request.

    See `Idempotency keys <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__ for more
    information."""

    device_code: DeviceCode


class CreateDeviceCodeRequestDict(TypedDict):
    idempotency_key: str
    device_code: DeviceCodeDict
