from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .charge_request_additional_recipient import ChargeRequestAdditionalRecipient, ChargeRequestAdditionalRecipientDict
from .create_order_request import CreateOrderRequest, CreateOrderRequestDict


class CreateCheckoutRequest(SdkBaseModel):
    """Defines the parameters that can be included in the body of a request to the ``CreateCheckout`` endpoint."""

    idempotency_key: str
    """A unique string that identifies this checkout among others you have created. It can be any valid string but must
    be unique for every order sent to Square Checkout for a given location ID.

    The idempotency key is used to avoid processing the same order more than once. If you are unsure whether a
    particular checkout was created successfully, you can attempt it again with the same idempotency key and all the
    same other parameters without worrying about creating duplicates.

    You should use a random number/string generator native to the language you are working in to generate strings for
    your idempotency keys.

    For more information, see `Idempotency <https://developer.squareup.com/docs/working-with-apis/idempotency>`__."""

    order: CreateOrderRequest
    ask_for_shipping_address: Optional[bool] = UNSET
    """If ``true``, Square Checkout collects shipping information on your behalf and stores that information with the
    transaction information in the Square Seller Dashboard.

    Default: ``false``."""

    merchant_support_email: Optional[str] = UNSET
    """The email address to display on the Square Checkout confirmation page and confirmation email that the buyer can
    use to contact the seller.

    If this value is not set, the confirmation page and email display the primary email address associated with the
    seller's Square account.

    Default: none; only exists if explicitly set."""

    pre_populate_buyer_email: Optional[str] = UNSET
    """If provided, the buyer's email is prepopulated on the checkout page as an editable text field.

    Default: none; only exists if explicitly set."""

    pre_populate_shipping_address: Optional[Address] = UNSET
    """Represents a postal address in a country. For more information, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""

    redirect_url: Optional[str] = UNSET
    """The URL to redirect to after the checkout is completed with ``checkoutId``, ``transactionId``, and
    ``referenceId`` appended as URL parameters. For example, if the provided redirect URL is
    ``http://www.example.com/order-complete``, a successful transaction redirects the customer to:

    ``http://www.example.com/order-complete?checkoutId=xxxxxx&amp;referenceId=xxxxxx&amp;transactionId=xxxxxx``

    If you do not provide a redirect URL, Square Checkout displays an order confirmation page on your behalf; however,
    it is strongly recommended that you provide a redirect URL so you can verify the transaction results and finalize
    the order through your existing/normal confirmation workflow.

    Default: none; only exists if explicitly set."""

    additional_recipients: Optional[list[ChargeRequestAdditionalRecipient]] = UNSET
    """The basic primitive of a multi-party transaction. The value is optional. The transaction facilitated by you can
    be split from here.

    If you provide this value, the ``amount_money`` value in your ``additional_recipients`` field cannot be more than
    90% of the ``total_money`` calculated by Square for your order. The ``location_id`` must be a valid seller location
    where the checkout is occurring.

    This field requires ``PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS`` OAuth permission.

    This field is currently not supported in the Square Sandbox."""

    note: Optional[str] = UNSET
    """An optional note to associate with the ``checkout`` object.

    This value cannot exceed 60 characters."""


class CreateCheckoutRequestDict(TypedDict):
    idempotency_key: str
    order: CreateOrderRequestDict
    ask_for_shipping_address: NotRequired[bool]
    merchant_support_email: NotRequired[str]
    pre_populate_buyer_email: NotRequired[str]
    pre_populate_shipping_address: NotRequired[AddressDict]
    redirect_url: NotRequired[str]
    additional_recipients: NotRequired[list[ChargeRequestAdditionalRecipientDict]]
    note: NotRequired[str]
