from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ErrorCode(str, Enum):
    """Indicates the specific error that occurred during a request to a Square API."""

    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    """A general server error occurred."""

    UNAUTHORIZED = "UNAUTHORIZED"
    """A general authorization error occurred."""

    ACCESS_TOKEN_EXPIRED = "ACCESS_TOKEN_EXPIRED"
    """The provided access token has expired."""

    ACCESS_TOKEN_REVOKED = "ACCESS_TOKEN_REVOKED"
    """The provided access token has been revoked."""

    CLIENT_DISABLED = "CLIENT_DISABLED"
    """The provided client has been disabled."""

    FORBIDDEN = "FORBIDDEN"
    """A general access error occurred."""

    INSUFFICIENT_SCOPES = "INSUFFICIENT_SCOPES"
    """The provided access token does not have permission to execute the requested action."""

    APPLICATION_DISABLED = "APPLICATION_DISABLED"
    """The calling application was disabled."""

    V1_APPLICATION = "V1_APPLICATION"
    """The calling application was created prior to 2016-03-30 and is not compatible with v2 Square API calls."""

    V1_ACCESS_TOKEN = "V1_ACCESS_TOKEN"
    """The calling application is using an access token created prior to 2016-03-30 and is not compatible with v2 Square
    API calls."""

    CARD_PROCESSING_NOT_ENABLED = "CARD_PROCESSING_NOT_ENABLED"
    """The location provided in the API call is not enabled for credit card processing."""

    MERCHANT_SUBSCRIPTION_NOT_FOUND = "MERCHANT_SUBSCRIPTION_NOT_FOUND"
    """A required subscription was not found for the merchant"""

    BAD_REQUEST = "BAD_REQUEST"
    """A general error occurred with the request."""

    MISSING_REQUIRED_PARAMETER = "MISSING_REQUIRED_PARAMETER"
    """The request is missing a required path, query, or body parameter."""

    INCORRECT_TYPE = "INCORRECT_TYPE"
    """The value provided in the request is the wrong type. For example, a string instead of an integer."""

    INVALID_TIME = "INVALID_TIME"
    """Formatting for the provided time value is incorrect."""

    INVALID_TIME_RANGE = "INVALID_TIME_RANGE"
    """The time range provided in the request is invalid. For example, the end time is before the start time."""

    INVALID_VALUE = "INVALID_VALUE"
    """The provided value is invalid. For example, including ``%`` in a phone number."""

    INVALID_CURSOR = "INVALID_CURSOR"
    """The pagination cursor included in the request is invalid."""

    UNKNOWN_QUERY_PARAMETER = "UNKNOWN_QUERY_PARAMETER"
    """The query parameters provided is invalid for the requested endpoint."""

    CONFLICTING_PARAMETERS = "CONFLICTING_PARAMETERS"
    """One or more of the request parameters conflict with each other."""

    EXPECTED_JSON_BODY = "EXPECTED_JSON_BODY"
    """The request body is not a JSON object."""

    INVALID_SORT_ORDER = "INVALID_SORT_ORDER"
    """The provided sort order is not a valid key. Currently, sort order must be ``ASC`` or ``DESC``."""

    VALUE_REGEX_MISMATCH = "VALUE_REGEX_MISMATCH"
    """The provided value does not match an expected regular expression."""

    VALUE_TOO_SHORT = "VALUE_TOO_SHORT"
    """The provided string value is shorter than the minimum length allowed."""

    VALUE_TOO_LONG = "VALUE_TOO_LONG"
    """The provided string value is longer than the maximum length allowed."""

    VALUE_TOO_LOW = "VALUE_TOO_LOW"
    """The provided value is less than the supported minimum."""

    VALUE_TOO_HIGH = "VALUE_TOO_HIGH"
    """The provided value is greater than the supported maximum."""

    VALUE_EMPTY = "VALUE_EMPTY"
    """The provided value has a default (empty) value such as a blank string."""

    ARRAY_LENGTH_TOO_LONG = "ARRAY_LENGTH_TOO_LONG"
    """The provided array has too many elements."""

    ARRAY_LENGTH_TOO_SHORT = "ARRAY_LENGTH_TOO_SHORT"
    """The provided array has too few elements."""

    ARRAY_EMPTY = "ARRAY_EMPTY"
    """The provided array is empty."""

    EXPECTED_BOOLEAN = "EXPECTED_BOOLEAN"
    """The endpoint expected the provided value to be a boolean."""

    EXPECTED_INTEGER = "EXPECTED_INTEGER"
    """The endpoint expected the provided value to be an integer."""

    EXPECTED_FLOAT = "EXPECTED_FLOAT"
    """The endpoint expected the provided value to be a float."""

    EXPECTED_STRING = "EXPECTED_STRING"
    """The endpoint expected the provided value to be a string."""

    EXPECTED_OBJECT = "EXPECTED_OBJECT"
    """The endpoint expected the provided value to be a JSON object."""

    EXPECTED_ARRAY = "EXPECTED_ARRAY"
    """The endpoint expected the provided value to be an array or list."""

    EXPECTED_MAP = "EXPECTED_MAP"
    """The endpoint expected the provided value to be a map or associative array."""

    EXPECTED_BASE64_ENCODED_BYTE_ARRAY = "EXPECTED_BASE64_ENCODED_BYTE_ARRAY"
    """The endpoint expected the provided value to be an array encoded in base64."""

    INVALID_ARRAY_VALUE = "INVALID_ARRAY_VALUE"
    """One or more objects in the array does not match the array type."""

    INVALID_ENUM_VALUE = "INVALID_ENUM_VALUE"
    """The provided static string is not valid for the field."""

    INVALID_CONTENT_TYPE = "INVALID_CONTENT_TYPE"
    """Invalid content type header."""

    INVALID_FORM_VALUE = "INVALID_FORM_VALUE"
    """Only relevant for applications created prior to 2016-03-30. Indicates there was an error while parsing form
    values."""

    CUSTOMER_NOT_FOUND = "CUSTOMER_NOT_FOUND"
    """The provided customer id can't be found in the merchant's customers list."""

    ONE_INSTRUMENT_EXPECTED = "ONE_INSTRUMENT_EXPECTED"
    """A general error occurred."""

    NO_FIELDS_SET = "NO_FIELDS_SET"
    """A general error occurred."""

    TOO_MANY_MAP_ENTRIES = "TOO_MANY_MAP_ENTRIES"
    """Too many entries in the map field."""

    MAP_KEY_LENGTH_TOO_SHORT = "MAP_KEY_LENGTH_TOO_SHORT"
    """The length of one of the provided keys in the map is too short."""

    MAP_KEY_LENGTH_TOO_LONG = "MAP_KEY_LENGTH_TOO_LONG"
    """The length of one of the provided keys in the map is too long."""

    CUSTOMER_MISSING_NAME = "CUSTOMER_MISSING_NAME"
    """The provided customer does not have a recorded name."""

    CUSTOMER_MISSING_EMAIL = "CUSTOMER_MISSING_EMAIL"
    """The provided customer does not have a recorded email."""

    INVALID_PAUSE_LENGTH = "INVALID_PAUSE_LENGTH"
    """The subscription cannot be paused longer than the duration of the current phase."""

    INVALID_DATE = "INVALID_DATE"
    """The subscription cannot be paused/resumed on the given date."""

    UNSUPPORTED_COUNTRY = "UNSUPPORTED_COUNTRY"
    """The API request references an unsupported country."""

    UNSUPPORTED_CURRENCY = "UNSUPPORTED_CURRENCY"
    """The API request references an unsupported currency."""

    APPLE_TTP_PIN_TOKEN = "APPLE_TTP_PIN_TOKEN"
    """The payment was declined by the card issuer during an Apple Tap to Pay (TTP) transaction with a request for the
    card's PIN. This code will be returned alongside ``CARD_DECLINED_VERIFICATION_REQUIRED`` as a supplemental error,
    and will include an issuer-provided token in the ``details`` field that is needed to initiate the PIN collection
    flow on the iOS device."""

    CARD_EXPIRED = "CARD_EXPIRED"
    """The card issuer declined the request because the card is expired."""

    INVALID_EXPIRATION = "INVALID_EXPIRATION"
    """The expiration date for the payment card is invalid. For example, it indicates a date in the past."""

    INVALID_EXPIRATION_YEAR = "INVALID_EXPIRATION_YEAR"
    """The expiration year for the payment card is invalid. For example, it indicates a year in the past or contains
    invalid characters."""

    INVALID_EXPIRATION_DATE = "INVALID_EXPIRATION_DATE"
    """The expiration date for the payment card is invalid. For example, it contains invalid characters."""

    UNSUPPORTED_CARD_BRAND = "UNSUPPORTED_CARD_BRAND"
    """The credit card provided is not from a supported issuer."""

    UNSUPPORTED_ENTRY_METHOD = "UNSUPPORTED_ENTRY_METHOD"
    """The entry method for the credit card (swipe, dip, tap) is not supported."""

    INVALID_ENCRYPTED_CARD = "INVALID_ENCRYPTED_CARD"
    """The encrypted card information is invalid."""

    INVALID_CARD = "INVALID_CARD"
    """The credit card cannot be validated based on the provided details."""

    PAYMENT_AMOUNT_MISMATCH = "PAYMENT_AMOUNT_MISMATCH"
    """The payment was declined because there was a payment amount mismatch. The money amount Square was expecting does
    not match the amount provided."""

    GENERIC_DECLINE = "GENERIC_DECLINE"
    """Square received a decline without any additional information. If the payment information seems correct, the buyer
    can contact their issuer to ask for more information."""

    CVV_FAILURE = "CVV_FAILURE"
    """The card issuer declined the request because the CVV value is invalid."""

    ADDRESS_VERIFICATION_FAILURE = "ADDRESS_VERIFICATION_FAILURE"
    """The card issuer declined the request because the postal code is invalid."""

    INVALID_ACCOUNT = "INVALID_ACCOUNT"
    """The issuer was not able to locate the account on record."""

    CURRENCY_MISMATCH = "CURRENCY_MISMATCH"
    """The currency associated with the payment is not valid for the provided funding source. For example, a gift card
    funded in USD cannot be used to process payments in GBP."""

    INSUFFICIENT_FUNDS = "INSUFFICIENT_FUNDS"
    """The funding source has insufficient funds to cover the payment."""

    INSUFFICIENT_PERMISSIONS = "INSUFFICIENT_PERMISSIONS"
    """The Square account does not have the permissions to accept this payment. For example, Square may limit which
    merchants are allowed to receive gift card payments."""

    CARDHOLDER_INSUFFICIENT_PERMISSIONS = "CARDHOLDER_INSUFFICIENT_PERMISSIONS"
    """The card issuer has declined the transaction due to restrictions on where the card can be used. For example, a
    gift card is limited to a single merchant."""

    INVALID_LOCATION = "INVALID_LOCATION"
    """The Square account cannot take payments in the specified region. A Square account can take payments only from the
    region where the account was created."""

    TRANSACTION_LIMIT = "TRANSACTION_LIMIT"
    """The card issuer has determined the payment amount is either too high or too low. The API returns the error code
    mostly for credit cards (for example, the card reached the credit limit). However, sometimes the issuer bank can
    indicate the error for debit or prepaid cards (for example, card has insufficient funds)."""

    VOICE_FAILURE = "VOICE_FAILURE"
    """The card issuer declined the request because the issuer requires voice authorization from the cardholder. The
    seller should ask the customer to contact the card issuing bank to authorize the payment."""

    PAN_FAILURE = "PAN_FAILURE"
    """The specified card number is invalid. For example, it is of incorrect length or is incorrectly formatted."""

    EXPIRATION_FAILURE = "EXPIRATION_FAILURE"
    """The card expiration date is either invalid or indicates that the card is expired."""

    CARD_NOT_SUPPORTED = "CARD_NOT_SUPPORTED"
    """The card is not supported either in the geographic region or by the `merchant category code
    <https://developer.squareup.com/docs/locations-api#initialize-a-merchant-category-code>`__ (MCC)."""

    READER_DECLINED = "READER_DECLINED"
    """The Square Card Reader declined the payment for an unknown reason."""

    INVALID_PIN = "INVALID_PIN"
    """The card issuer declined the request because the PIN is invalid."""

    MISSING_PIN = "MISSING_PIN"
    """The payment is missing a required PIN."""

    MISSING_ACCOUNT_TYPE = "MISSING_ACCOUNT_TYPE"
    """The payment is missing a required ACCOUNT_TYPE parameter."""

    INVALID_POSTAL_CODE = "INVALID_POSTAL_CODE"
    """The postal code is incorrectly formatted."""

    INVALID_FEES = "INVALID_FEES"
    """The app_fee_money on a payment is too high."""

    MANUALLY_ENTERED_PAYMENT_NOT_SUPPORTED = "MANUALLY_ENTERED_PAYMENT_NOT_SUPPORTED"
    """The card must be swiped, tapped, or dipped. Payments attempted by manually entering the card number are
    declined."""

    PAYMENT_LIMIT_EXCEEDED = "PAYMENT_LIMIT_EXCEEDED"
    """Square declined the request because the payment amount exceeded the processing limit for this merchant."""

    GIFT_CARD_AVAILABLE_AMOUNT = "GIFT_CARD_AVAILABLE_AMOUNT"
    """Provides the available balance on a Square gift card when a gift card payment fails due to insufficient funds.
    This error is returned with an ``INSUFFICIENT_FUNDS`` error and contains the balance in the smallest denomination of
    the applicable currency. `Learn more
    <https://developer.squareup.com/docs/payments-api/error-codes#gift_card_available_amount>`__ about this error code.

    You can use the ``accept_partial_authorization`` field in a ``CreatePayment`` request to configure a payment flow
    that uses the available balance and allows collecting additional payments."""

    ACCOUNT_UNUSABLE = "ACCOUNT_UNUSABLE"
    """The account provided cannot carry out transactions."""

    BUYER_REFUSED_PAYMENT = "BUYER_REFUSED_PAYMENT"
    """Bank account rejected or was not authorized for the payment."""

    DELAYED_TRANSACTION_EXPIRED = "DELAYED_TRANSACTION_EXPIRED"
    """The application tried to update a delayed-capture payment that has expired."""

    DELAYED_TRANSACTION_CANCELED = "DELAYED_TRANSACTION_CANCELED"
    """The application tried to cancel a delayed-capture payment that was already cancelled."""

    DELAYED_TRANSACTION_CAPTURED = "DELAYED_TRANSACTION_CAPTURED"
    """The application tried to capture a delayed-capture payment that was already captured."""

    DELAYED_TRANSACTION_FAILED = "DELAYED_TRANSACTION_FAILED"
    """The application tried to update a delayed-capture payment that failed."""

    CARD_TOKEN_EXPIRED = "CARD_TOKEN_EXPIRED"
    """The provided card token (nonce) has expired."""

    CARD_TOKEN_USED = "CARD_TOKEN_USED"
    """The provided card token (nonce) was already used to process the payment or refund."""

    AMOUNT_TOO_HIGH = "AMOUNT_TOO_HIGH"
    """The requested payment amount is too high for the provided payment source."""

    UNSUPPORTED_INSTRUMENT_TYPE = "UNSUPPORTED_INSTRUMENT_TYPE"
    """The API request references an unsupported instrument type."""

    REFUND_AMOUNT_INVALID = "REFUND_AMOUNT_INVALID"
    """The requested refund amount exceeds the amount available to refund."""

    REFUND_ALREADY_PENDING = "REFUND_ALREADY_PENDING"
    """The payment already has a pending refund."""

    PAYMENT_NOT_REFUNDABLE = "PAYMENT_NOT_REFUNDABLE"
    """The payment is not refundable. For example, the payment is too old to be refunded."""

    PAYMENT_NOT_REFUNDABLE_DUE_TO_DISPUTE = "PAYMENT_NOT_REFUNDABLE_DUE_TO_DISPUTE"
    """The payment is not refundable because it has been disputed."""

    REFUND_ERROR_PAYMENT_NEEDS_COMPLETION = "REFUND_ERROR_PAYMENT_NEEDS_COMPLETION"
    """The payment is not refundable because the payment is approved and needs to be completed first before the refund
    is issued."""

    REFUND_DECLINED = "REFUND_DECLINED"
    """Request failed - The card issuer declined the refund."""

    INSUFFICIENT_PERMISSIONS_FOR_REFUND = "INSUFFICIENT_PERMISSIONS_FOR_REFUND"
    """The Square account does not have the permissions to process this refund."""

    INVALID_CARD_DATA = "INVALID_CARD_DATA"
    """Generic error - the provided card data is invalid."""

    SOURCE_USED = "SOURCE_USED"
    """The provided source id was already used to create a card."""

    SOURCE_EXPIRED = "SOURCE_EXPIRED"
    """The provided source id has expired."""

    UNSUPPORTED_LOYALTY_REWARD_TIER = "UNSUPPORTED_LOYALTY_REWARD_TIER"
    """The referenced loyalty program reward tier is not supported. This could happen if the reward tier created in a
    first party application is incompatible with the Loyalty API."""

    LOCATION_MISMATCH = "LOCATION_MISMATCH"
    """Generic error - the given location does not matching what is expected."""

    ORDER_UNPAID_NOT_RETURNABLE = "ORDER_UNPAID_NOT_RETURNABLE"
    """The order attempting to be returned is not yet paid and cannot be returned."""

    PARTIAL_PAYMENT_DELAY_CAPTURE_NOT_SUPPORTED = "PARTIAL_PAYMENT_DELAY_CAPTURE_NOT_SUPPORTED"
    """Delay capture of a partial payment is not supported."""

    IDEMPOTENCY_KEY_REUSED = "IDEMPOTENCY_KEY_REUSED"
    """The provided idempotency key has already been used."""

    UNEXPECTED_VALUE = "UNEXPECTED_VALUE"
    """General error - the value provided was unexpected."""

    SANDBOX_NOT_SUPPORTED = "SANDBOX_NOT_SUPPORTED"
    """The API request is not supported in sandbox."""

    INVALID_EMAIL_ADDRESS = "INVALID_EMAIL_ADDRESS"
    """The provided email address is invalid."""

    INVALID_PHONE_NUMBER = "INVALID_PHONE_NUMBER"
    """The provided phone number is invalid."""

    CHECKOUT_EXPIRED = "CHECKOUT_EXPIRED"
    """The provided checkout URL has expired."""

    BAD_CERTIFICATE = "BAD_CERTIFICATE"
    """Bad certificate."""

    INVALID_SQUARE_VERSION_FORMAT = "INVALID_SQUARE_VERSION_FORMAT"
    """The provided Square-Version is incorrectly formatted."""

    API_VERSION_INCOMPATIBLE = "API_VERSION_INCOMPATIBLE"
    """The provided Square-Version is incompatible with the requested action."""

    CARD_PRESENCE_REQUIRED = "CARD_PRESENCE_REQUIRED"
    """The transaction requires that a card be present."""

    UNSUPPORTED_SOURCE_TYPE = "UNSUPPORTED_SOURCE_TYPE"
    """The API request references an unsupported source type."""

    CARD_MISMATCH = "CARD_MISMATCH"
    """The provided card does not match what is expected."""

    PLAID_ERROR = "PLAID_ERROR"
    """Generic plaid error"""

    PLAID_ERROR_ITEM_LOGIN_REQUIRED = "PLAID_ERROR_ITEM_LOGIN_REQUIRED"
    """Plaid error - ITEM_LOGIN_REQUIRED"""

    PLAID_ERROR_RATE_LIMIT = "PLAID_ERROR_RATE_LIMIT"
    """Plaid error - RATE_LIMIT"""

    PAYMENT_SOURCE_NOT_ENABLED_FOR_TARGET = "PAYMENT_SOURCE_NOT_ENABLED_FOR_TARGET"
    """The provided merchant or location is not enabled to accept the requested payment source."""

    CARD_DECLINED = "CARD_DECLINED"
    """The card was declined."""

    VERIFY_CVV_FAILURE = "VERIFY_CVV_FAILURE"
    """The CVV could not be verified."""

    VERIFY_AVS_FAILURE = "VERIFY_AVS_FAILURE"
    """The AVS could not be verified."""

    CARD_DECLINED_CALL_ISSUER = "CARD_DECLINED_CALL_ISSUER"
    """The payment card was declined with a request for the card holder to call the issuer."""

    CARD_DECLINED_VERIFICATION_REQUIRED = "CARD_DECLINED_VERIFICATION_REQUIRED"
    """The payment card was declined with a request for additional verification."""

    BAD_EXPIRATION = "BAD_EXPIRATION"
    """The card expiration date is either missing or incorrectly formatted."""

    CHIP_INSERTION_REQUIRED = "CHIP_INSERTION_REQUIRED"
    """The card issuer requires that the card be read using a chip reader."""

    ALLOWABLE_PIN_TRIES_EXCEEDED = "ALLOWABLE_PIN_TRIES_EXCEEDED"
    """The card has exhausted its available pin entry retries set by the card issuer. Resolving the error typically
    requires the card holder to contact the card issuer."""

    RESERVATION_DECLINED = "RESERVATION_DECLINED"
    """The card issuer declined the refund."""

    UNKNOWN_BODY_PARAMETER = "UNKNOWN_BODY_PARAMETER"
    """The body parameter is not recognized by the requested endpoint."""

    NOT_FOUND = "NOT_FOUND"
    """Not Found - a general error occurred."""

    APPLE_PAYMENT_PROCESSING_CERTIFICATE_HASH_NOT_FOUND = "APPLE_PAYMENT_PROCESSING_CERTIFICATE_HASH_NOT_FOUND"
    """Square could not find the associated Apple Pay certificate."""

    METHOD_NOT_ALLOWED = "METHOD_NOT_ALLOWED"
    """Method Not Allowed - a general error occurred."""

    NOT_ACCEPTABLE = "NOT_ACCEPTABLE"
    """Not Acceptable - a general error occurred."""

    REQUEST_TIMEOUT = "REQUEST_TIMEOUT"
    """Request Timeout - a general error occurred."""

    CONFLICT = "CONFLICT"
    """Conflict - a general error occurred."""

    GONE = "GONE"
    """The target resource is no longer available and this condition is likely to be permanent."""

    REQUEST_ENTITY_TOO_LARGE = "REQUEST_ENTITY_TOO_LARGE"
    """Request Entity Too Large - a general error occurred."""

    UNSUPPORTED_MEDIA_TYPE = "UNSUPPORTED_MEDIA_TYPE"
    """Unsupported Media Type - a general error occurred."""

    UNPROCESSABLE_ENTITY = "UNPROCESSABLE_ENTITY"
    """Unprocessable Entity - a general error occurred."""

    RATE_LIMITED = "RATE_LIMITED"
    """Rate Limited - a general error occurred."""

    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
    """Not Implemented - a general error occurred."""

    BAD_GATEWAY = "BAD_GATEWAY"
    """Bad Gateway - a general error occurred."""

    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"
    """Service Unavailable - a general error occurred."""

    TEMPORARY_ERROR = "TEMPORARY_ERROR"
    """A temporary internal error occurred. You can safely retry your call using the same idempotency key."""

    GATEWAY_TIMEOUT = "GATEWAY_TIMEOUT"
    """Gateway Timeout - a general error occurred."""

    __str__ = str.__str__


ErrorCodeOrStr: TypeAlias = Annotated[ErrorCode | str, open_enum_validator(ErrorCode)]
