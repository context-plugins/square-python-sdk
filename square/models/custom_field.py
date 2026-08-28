from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CustomField(SdkBaseModel):
    """Describes a custom form field to add to the checkout page to collect more information from buyers during
    checkout. For more information, see `Specify checkout options
    <https://developer.squareup.com/docs/checkout-api/optional-checkout-configurations#specify-checkout-options-1>`__."""

    title: str
    """The title of the custom field."""


class CustomFieldDict(TypedDict):
    title: str
