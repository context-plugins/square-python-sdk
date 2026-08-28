from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ErrorCategory(str, Enum):
    """Indicates which high-level category of error has occurred during a request to the Connect API."""

    API_ERROR = "API_ERROR"
    """An error occurred with the Connect API itself."""

    AUTHENTICATION_ERROR = "AUTHENTICATION_ERROR"
    """An authentication error occurred. Most commonly, the request had a missing, malformed, or otherwise invalid
    ``Authorization`` header."""

    INVALID_REQUEST_ERROR = "INVALID_REQUEST_ERROR"
    """The request was invalid. Most commonly, a required parameter was missing, or a provided parameter had an invalid
    value."""

    RATE_LIMIT_ERROR = "RATE_LIMIT_ERROR"
    """Your application reached the Square API rate limit. You might receive this error if your application sends a high
    number of requests to Square APIs in a short period of time.

    Your application should monitor responses for ``429 RATE_LIMITED`` errors and use a retry mechanism with an
    `exponential backoff <https://en.wikipedia.org/wiki/Exponential_backoff>`__ schedule to resend the requests at an
    increasingly slower rate. It is also a good practice to use a randomized delay (jitter) in your retry schedule."""

    PAYMENT_METHOD_ERROR = "PAYMENT_METHOD_ERROR"
    """An error occurred while processing a payment method. Most commonly, the details of the payment method were
    invalid (such as a card's CVV or expiration date)."""

    REFUND_ERROR = "REFUND_ERROR"
    """An error occurred while attempting to process a refund."""

    MERCHANT_SUBSCRIPTION_ERROR = "MERCHANT_SUBSCRIPTION_ERROR"
    """An error occurred when checking a merchant subscription status"""

    EXTERNAL_VENDOR_ERROR = "EXTERNAL_VENDOR_ERROR"
    """An error that is returned from an external vendor's API"""

    __str__ = str.__str__


ErrorCategoryOrStr: TypeAlias = Annotated[ErrorCategory | str, open_enum_validator(ErrorCategory)]
