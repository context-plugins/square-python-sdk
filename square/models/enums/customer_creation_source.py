from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CustomerCreationSource(str, Enum):
    """Indicates the method used to create the customer profile."""

    OTHER = "OTHER"
    """The default creation source. This source is typically used for backward/future compatibility when the original
    source of a customer profile is unrecognized. For example, when older clients do not support newer source types."""

    APPOINTMENTS = "APPOINTMENTS"
    """The customer profile was created automatically when an appointment was scheduled."""

    COUPON = "COUPON"
    """The customer profile was created automatically when a coupon was issued using Square Point of Sale."""

    DELETION_RECOVERY = "DELETION_RECOVERY"
    """The customer profile was restored through Square's deletion recovery process."""

    DIRECTORY = "DIRECTORY"
    """The customer profile was created manually through Square Seller Dashboard or the Point of Sale application."""

    EGIFTING = "EGIFTING"
    """The customer profile was created automatically when a gift card was issued using Square Point of Sale. Customer
    profiles are created for both the buyer and the recipient of the gift card."""

    EMAIL_COLLECTION = "EMAIL_COLLECTION"
    """The customer profile was created through Square Point of Sale when signing up for marketing emails during
    checkout."""

    FEEDBACK = "FEEDBACK"
    """The customer profile was created automatically when providing feedback through a digital receipt."""

    IMPORT = "IMPORT"
    """The customer profile was created automatically when importing customer data through Square Seller Dashboard."""

    INVOICES = "INVOICES"
    """The customer profile was created automatically during an invoice payment."""

    LOYALTY = "LOYALTY"
    """The customer profile was created automatically when customers provide a phone number for loyalty reward programs
    during checkout."""

    MARKETING = "MARKETING"
    """The customer profile was created as the result of a campaign managed through Square’s Facebook integration."""

    MERGE = "MERGE"
    """The customer profile was created as the result of explicitly merging multiple customer profiles through the
    Square Seller Dashboard or the Point of Sale application."""

    ONLINE_STORE = "ONLINE_STORE"
    """The customer profile was created through Square's Online Store solution (legacy service)."""

    INSTANT_PROFILE = "INSTANT_PROFILE"
    """The customer profile was created automatically as the result of a successful transaction that did not explicitly
    link to an existing customer profile."""

    TERMINAL = "TERMINAL"
    """The customer profile was created through Square's Virtual Terminal."""

    THIRD_PARTY = "THIRD_PARTY"
    """The customer profile was created through a Square API call."""

    THIRD_PARTY_IMPORT = "THIRD_PARTY_IMPORT"
    """The customer profile was created by a third-party product and imported through an official integration."""

    UNMERGE_RECOVERY = "UNMERGE_RECOVERY"
    """The customer profile was restored through Square's unmerge recovery process."""

    __str__ = str.__str__


CustomerCreationSourceOrStr: TypeAlias = Annotated[
    CustomerCreationSource | str, open_enum_validator(CustomerCreationSource)
]
