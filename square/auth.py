from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypeAlias

from .core import AsyncAuthScheme, AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AuthSchemes:
    oauth2: AuthScheme
    oauth2_client_secret: AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AsyncAuthSchemes:
    oauth2: AsyncAuthScheme
    oauth2_client_secret: AsyncAuthScheme


Oauth2Scope: TypeAlias = Literal[
    "ADDON_CONFIGURATIONS_READ",
    "ADDON_CONFIGURATIONS_WRITE",
    "APPOINTMENTS_ALL_READ",
    "APPOINTMENTS_ALL_WRITE",
    "APPOINTMENTS_BUSINESS_SETTINGS_READ",
    "APPOINTMENTS_READ",
    "APPOINTMENTS_WRITE",
    "BANK_ACCOUNTS_READ",
    "CASH_DRAWER_READ",
    "CHANNELS_CREATE",
    "CHANNELS_READ",
    "CHANNELS_UPDATE",
    "CUSTOMERS_READ",
    "CUSTOMERS_WRITE",
    "DEVICES_READ",
    "DEVICE_CREDENTIAL_MANAGEMENT",
    "DISCOUNT_CODES_READ",
    "DISCOUNT_CODES_WRITE",
    "DISPUTES_READ",
    "DISPUTES_WRITE",
    "EMPLOYEES_READ",
    "EMPLOYEES_WRITE",
    "GIFTCARDS_READ",
    "GIFTCARDS_WRITE",
    "INVENTORY_READ",
    "INVENTORY_WRITE",
    "INVOICES_READ",
    "INVOICES_WRITE",
    "ITEMS_READ",
    "ITEMS_WRITE",
    "LOYALTY_READ",
    "LOYALTY_WRITE",
    "MERCHANT_PROFILE_READ",
    "MERCHANT_PROFILE_WRITE",
    "ONLINE_STORE_SITE_READ",
    "ONLINE_STORE_SNIPPETS_READ",
    "ONLINE_STORE_SNIPPETS_WRITE",
    "ORDERS_READ",
    "ORDERS_WRITE",
    "PAYMENTS_READ",
    "PAYMENTS_WRITE",
    "PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS",
    "PAYMENTS_WRITE_IN_PERSON",
    "PAYMENTS_WRITE_SHARED_ONFILE",
    "PAYOUTS_READ",
    "PAYOUTS_WRITE",
    "PERMISSION_SETS_READ",
    "PERMISSION_SETS_WRITE",
    "RESERVATIONS_READ",
    "RESERVATIONS_WRITE",
    "RESTAURANT_CHECKS_READ",
    "SETTLEMENTS_READ",
    "SUBSCRIPTIONS_READ",
    "SUBSCRIPTIONS_WRITE",
    "TIMECARDS_READ",
    "TIMECARDS_SETTINGS_READ",
    "TIMECARDS_SETTINGS_WRITE",
    "TIMECARDS_WRITE",
    "VENDOR_READ",
    "VENDOR_WRITE",
    "BANK_ACCOUNTS_WRITE",
    "PAYMENT_METHODS_READ",
]
"""``ADDON_CONFIGURATIONS_READ``: __HTTP Method__: ``GET``

Grants write access for third-party Add-ons to read configurations of their Add-ons, for example, when calling
``RetrieveConfiguration`` endpoint. ``ADDON_CONFIGURATIONS_WRITE``: __HTTP Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access for third-party Add-ons to store configurations of their Add-ons, for example, when calling
``CreateConfiguration`` endpoint. ``APPOINTMENTS_ALL_READ``: __HTTP Method__: ``GET``, ``POST``

Grants read access to all of a seller's booking information, calendar, and business details. This permission must be
accompanied by the ``APPOINTMENTS_READ`` permission. ``APPOINTMENTS_ALL_WRITE``: __HTTP Method__: ``POST``, ``PUT``,
``DELETE``

Grants write access to all booking details, including double-booking a seller. This permission must be accompanied by
the ``APPOINTMENTS_WRITE`` permission. ``APPOINTMENTS_BUSINESS_SETTINGS_READ``: __HTTP Method__: ``GET``

Grants read access to booking business settings. For example, to call the ListTeamMemberBookingProfiles endpoint.
``APPOINTMENTS_READ``: __HTTP Method__: ``GET``, ``POST``

Grants read access to booking information. For example, to call the RetrieveBooking endpoint. ``APPOINTMENTS_WRITE``:
__HTTP Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to booking information. For example, to call the CreateBooking endpoint. ``BANK_ACCOUNTS_READ``:
__HTTP Method__: ``GET``

Grants read access to bank account information associated with the targeted Square account. For example, to call the
Connect v1 ListBankAccounts endpoint. ``CASH_DRAWER_READ``: __HTTP Method__: ``GET``

Grants read access to cash drawer shift information. For example, to call the ListCashDrawerShifts endpoint.
``CHANNELS_CREATE``: __HTTP Method__: ``POST``

Grants write access to create channels, for example, when calling the ``CreateChannel`` endpoint. ``CHANNELS_READ``:
__HTTP Method__: ``GET``

Grants read access to view channels, for example, when calling the ``RetrieveChannel`` endpoint. ``CHANNELS_UPDATE``:
__HTTP Method__: ``PUT``

Grants write access to update channels, for example, when calling the ``UpdateChannel`` endpoint. ``CUSTOMERS_READ``:
__HTTP Method__: ``GET``

Grants read access to customer information. For example, to call the ListCustomers endpoint. ``CUSTOMERS_WRITE``: __HTTP
Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to customer information. For example, to create and update customer profiles. ``DEVICES_READ``:
__HTTP Method__: ``GET``

Grants read access to device information. For example, to call the ``GetDevice`` and ``ListDevices`` endpoints.
``DEVICE_CREDENTIAL_MANAGEMENT``: __HTTP Method__: ``POST``, ``GET``

Grants read/write access to device credentials information. For example, to call the CreateDeviceCode endpoint.
``DISCOUNT_CODES_READ``: __HTTP Method__: ``GET``

Grants read access to Discount Codes API. For example, to call the ``RetrieveDiscountCode`` and ``RetrieveRedemption``
endpoints. ``DISCOUNT_CODES_WRITE``: __HTTP Method__: ``POST``

Grants write access to Discount Codes API. ``DISPUTES_READ``: __HTTP Method__: ``GET``

Grants read access to dispute information. For example, to call the RetrieveDispute endpoint. ``DISPUTES_WRITE``: __HTTP
Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to dispute information. For example, to call the SubmitEvidence endpoint. ``EMPLOYEES_READ``: __HTTP
Method__: ``GET``

Grants read access to employee profile information. For example, to call the Connect v1 Employees API.
``EMPLOYEES_WRITE``: __HTTP Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to employee profile information. For example, to create and modify employee profiles.
``GIFTCARDS_READ``: __HTTP Method__: ``GET``, ``POST``

Grants read access to gift card information. For example, to call the RetrieveGiftCard endpoint. ``GIFTCARDS_WRITE``:
__HTTP Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to gift card information. For example, to call the CreateGiftCard endpoint. ``INVENTORY_READ``:
__HTTP Method__: ``GET``

Grants read access to inventory information. For example, to call the RetrieveInventoryCount endpoint.
``INVENTORY_WRITE``: __HTTP Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to inventory information. For example, to call the BatchChangeInventory endpoint. ``INVOICES_READ``:
__HTTP Method__: ``GET``, ``POST``

Grants read access to invoice information. For example, to call the ListInvoices endpoint. ``INVOICES_WRITE``: __HTTP
Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to invoice information. For example, to call the CreateInvoice endpoint. ``ITEMS_READ``: __HTTP
Method__: ``GET``

Grants read access to product catalog information. For example, to obtain objects in a product catalog. ``ITEMS_WRITE``:
__HTTP Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to product catalog information. For example, to modify or add to a product catalog.
``LOYALTY_READ``: __HTTP Method__: ``GET``

Grants read access to loyalty information. For example, to call the ListLoyaltyPrograms endpoint. ``LOYALTY_WRITE``:
__HTTP Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to loyalty information. For example, to call the CreateLoyaltyAccount endpoint.
``MERCHANT_PROFILE_READ``: __HTTP Method__: ``GET``

Grants read access to business and location information. For example, to obtain a location ID for subsequent activity.
``MERCHANT_PROFILE_WRITE``: __HTTP Method__: ``POST``, ``PUT``

Grants write access to business and location information. For example, to create a new location or update the business
hours at an existing location. ``ONLINE_STORE_SITE_READ``: __HTTP Method__: ``GET``, ``POST``

Read access to ECOM online store site details. ``ONLINE_STORE_SNIPPETS_READ``: __HTTP Method__: ``GET``, ``POST``

Read access to ECOM online store snippets on published websites. ``ONLINE_STORE_SNIPPETS_WRITE``: __HTTP Method__:
``POST``, ``PUT``, ``DELETE``

Write access to ECOM online store snippets on published websites. ``ORDERS_READ``: __HTTP Method__: ``GET``

Grants read access to order information. For example, to call the BatchRetrieveOrders endpoint. ``ORDERS_WRITE``: __HTTP
Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to order information. For example, to call the CreateCheckout endpoint. ``PAYMENTS_READ``: __HTTP
Method__: ``GET``

Grants read access to transaction and refund information. For example, to call the RetrieveTransaction endpoint.
``PAYMENTS_WRITE``: __HTTP Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to transaction and refunds information. For example, to process payments with the Payments or
Checkout API. ``PAYMENTS_WRITE_ADDITIONAL_RECIPIENTS``: __HTTP Method__: ``POST``, ``PUT``, ``DELETE``

Allow third party applications to deduct a portion of each transaction amount. __Required__ to use multiparty
transaction functionality with the Payments API. ``PAYMENTS_WRITE_IN_PERSON``: __HTTP Method__: ``POST``, ``PUT``,
``DELETE``

Grants write access to payments and refunds information. For example, to process in-person payments.
``PAYMENTS_WRITE_SHARED_ONFILE``: __HTTP Method__: ``POST``, ``PUT``, ``DELETE``

Allows the developer to process payments on behalf of a seller using a shared on file payment method. ``PAYOUTS_READ``:
__HTTP Method__: ``GET``

Grants read access to payouts and payout entries information. For example, to call the Connect v2 ``ListPayouts``
endpoint. ``PAYOUTS_WRITE``: __HTTP Method__: ``POST``

Grants access to schedule a payout. ``PERMISSION_SETS_READ``: __HTTP Method__: ``GET``

Grants read access to Permission Sets. For example, to call the ``ListPermissionSets`` and ``RetrievePermissionSet``
endpoints. ``PERMISSION_SETS_WRITE``: __HTTP Method__: ``PUT``

Grants write access to Permission Sets. ``RESERVATIONS_READ``: __HTTP Method__: ``GET``

Grants read access to reservation information, for example, when calling the ``RetrieveReservation`` endpoint.
``RESERVATIONS_WRITE``: __HTTP Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to reservation information, for example, when calling the ``CreateReservation`` endpoint.
``RESTAURANT_CHECKS_READ``: __HTTP Method__: ``GET``

Grants read access to check information, for example, when calling the ``RetrieveCheck`` endpoint. ``SETTLEMENTS_READ``:
__HTTP Method__: ``GET``

Grants read access to settlement (deposit) information. For example, to call the Connect v1 ListSettlements endpoint.
``SUBSCRIPTIONS_READ``: __HTTP Method__: ``GET``, ``POST``

Grants read access to subscription information. For example, to call the RetrieveSubscription endpoint.
``SUBSCRIPTIONS_WRITE``: __HTTP Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to subscription information. For example, to call the CreateSubscription endpoint.
``TIMECARDS_READ``: __HTTP Method__: ``GET``

Grants read access to employee timecard information. For example, to call the Connect v2 SearchShifts endpoint.
``TIMECARDS_SETTINGS_READ``: __HTTP Method__: ``GET``

Grants read access to employee timecard settings information. For example, to call the GetBreakType endpoint.
``TIMECARDS_SETTINGS_WRITE``: __HTTP Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to employee timecard settings information. For example, to call the UpdateBreakType endpoint.
``TIMECARDS_WRITE``: __HTTP Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to employee shift information. For example, to create and modify employee shifts. ``VENDOR_READ``:
__HTTP Method__: ``GET``, ``POST``

Grants read access to vendor information, for example, when calling the ``RetrieveVendor`` endpoint. ``VENDOR_WRITE``:
__HTTP Method__: ``POST``, ``PUT``, ``DELETE``

Grants write access to vendor information, for example, when calling the ``BulkUpdateVendors`` endpoint.
``BANK_ACCOUNTS_WRITE``. ``PAYMENT_METHODS_READ``."""
