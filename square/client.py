from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.apple_pay import ApplePay
from .apis.bank_accounts import BankAccounts
from .apis.booking_custom_attributes import BookingCustomAttributes
from .apis.bookings import Bookings
from .apis.cards import Cards
from .apis.cash_drawers import CashDrawers
from .apis.catalog import Catalog
from .apis.channels import Channels
from .apis.checkout_api import CheckoutApi
from .apis.customer_custom_attributes import CustomerCustomAttributes
from .apis.customer_groups import CustomerGroups
from .apis.customer_segments import CustomerSegments
from .apis.customers import Customers
from .apis.devices import Devices
from .apis.disputes import Disputes
from .apis.employees import Employees
from .apis.events import Events
from .apis.gift_card_activities import GiftCardActivities
from .apis.gift_cards import GiftCards
from .apis.inventory import Inventory
from .apis.invoices import Invoices
from .apis.labor import Labor
from .apis.location_custom_attributes import LocationCustomAttributes
from .apis.locations import Locations
from .apis.loyalty import Loyalty
from .apis.merchant_custom_attributes import MerchantCustomAttributes
from .apis.merchants import Merchants
from .apis.oauth import Oauth
from .apis.order_custom_attributes import OrderCustomAttributes
from .apis.orders import Orders
from .apis.payments import Payments
from .apis.payouts import Payouts
from .apis.refunds import Refunds
from .apis.sites import Sites
from .apis.snippets import Snippets
from .apis.subscriptions import Subscriptions
from .apis.team import Team
from .apis.terminal import Terminal
from .apis.transactions import Transactions
from .apis.transfer_order_api import TransferOrderApi
from .apis.v1_transactions import V1Transactions
from .apis.vendors import Vendors
from .apis.webhook_subscriptions import WebhookSubscriptions
from .auth import AuthSchemes, Oauth2Scope
from .base_client import DEFAULT_TIMEOUT, BaseSquareClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    AuthorizationCodeCredentials,
    AuthorizationCodeCredentialsOrDict,
    AuthorizationCodeTokenSource,
    HttpClient,
    Httpx2Client,
    OAuth2RefreshableScheme,
    RawClient,
    RefreshableTokenSource,
    RetryOptionsOrDict,
    client_secret_basic,
    no_auth,
    param,
)
from .server.environment import Environment


class SquareClient(BaseSquareClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        custom_http_client: HttpClient | None = None,
        oauth2: AuthorizationCodeCredentialsOrDict[Oauth2Scope] | None = None,
        oauth2_token_source: RefreshableTokenSource[AuthorizationCodeCredentials[Oauth2Scope]] | None = None,
        oauth2_client_secret: str | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout, retry_options=retry_options)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else Httpx2Client(timeout=timeout),
            retry_options=self._retry_options,
            global_headers=[
                param[str]("User-Agent", "SquareClient/2.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "2.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(
            oauth2=(
                OAuth2RefreshableScheme(
                    credentials=AuthorizationCodeCredentials[Oauth2Scope].coerce(oauth2),
                    source=(
                        oauth2_token_source
                        if oauth2_token_source is not None
                        else AuthorizationCodeTokenSource[Oauth2Scope](
                            client=self._raw_client,
                            authorization_url=self._server.default("/oauth2/authorize"),
                            token_url=self._server.default("/oauth2/token"),
                            refresh_url=self._server.default("/oauth2/token"),
                            placement=client_secret_basic,
                        )
                    ),
                )
                if oauth2 is not None
                else no_auth
            ),
            oauth2_client_secret=(
                ApiKeyHeaderScheme("Authorization", oauth2_client_secret)
                if oauth2_client_secret is not None
                else no_auth
            ),
        )

    @cached_property
    def apple_pay(self) -> ApplePay:
        return ApplePay(self._raw_client, self._server, self._auth)

    @cached_property
    def bank_accounts(self) -> BankAccounts:
        return BankAccounts(self._raw_client, self._server, self._auth)

    @cached_property
    def booking_custom_attributes(self) -> BookingCustomAttributes:
        return BookingCustomAttributes(self._raw_client, self._server, self._auth)

    @cached_property
    def bookings(self) -> Bookings:
        return Bookings(self._raw_client, self._server, self._auth)

    @cached_property
    def cards(self) -> Cards:
        return Cards(self._raw_client, self._server, self._auth)

    @cached_property
    def cash_drawers(self) -> CashDrawers:
        return CashDrawers(self._raw_client, self._server, self._auth)

    @cached_property
    def catalog(self) -> Catalog:
        return Catalog(self._raw_client, self._server, self._auth)

    @cached_property
    def channels(self) -> Channels:
        return Channels(self._raw_client, self._server, self._auth)

    @cached_property
    def checkout_api(self) -> CheckoutApi:
        return CheckoutApi(self._raw_client, self._server, self._auth)

    @cached_property
    def customer_custom_attributes(self) -> CustomerCustomAttributes:
        return CustomerCustomAttributes(self._raw_client, self._server, self._auth)

    @cached_property
    def customer_groups(self) -> CustomerGroups:
        return CustomerGroups(self._raw_client, self._server, self._auth)

    @cached_property
    def customer_segments(self) -> CustomerSegments:
        return CustomerSegments(self._raw_client, self._server, self._auth)

    @cached_property
    def customers(self) -> Customers:
        return Customers(self._raw_client, self._server, self._auth)

    @cached_property
    def devices(self) -> Devices:
        return Devices(self._raw_client, self._server, self._auth)

    @cached_property
    def disputes(self) -> Disputes:
        return Disputes(self._raw_client, self._server, self._auth)

    @cached_property
    def employees(self) -> Employees:
        return Employees(self._raw_client, self._server, self._auth)

    @cached_property
    def events(self) -> Events:
        return Events(self._raw_client, self._server, self._auth)

    @cached_property
    def gift_card_activities(self) -> GiftCardActivities:
        return GiftCardActivities(self._raw_client, self._server, self._auth)

    @cached_property
    def gift_cards(self) -> GiftCards:
        return GiftCards(self._raw_client, self._server, self._auth)

    @cached_property
    def inventory(self) -> Inventory:
        return Inventory(self._raw_client, self._server, self._auth)

    @cached_property
    def invoices(self) -> Invoices:
        return Invoices(self._raw_client, self._server, self._auth)

    @cached_property
    def labor(self) -> Labor:
        return Labor(self._raw_client, self._server, self._auth)

    @cached_property
    def location_custom_attributes(self) -> LocationCustomAttributes:
        return LocationCustomAttributes(self._raw_client, self._server, self._auth)

    @cached_property
    def locations(self) -> Locations:
        return Locations(self._raw_client, self._server, self._auth)

    @cached_property
    def loyalty(self) -> Loyalty:
        return Loyalty(self._raw_client, self._server, self._auth)

    @cached_property
    def merchant_custom_attributes(self) -> MerchantCustomAttributes:
        return MerchantCustomAttributes(self._raw_client, self._server, self._auth)

    @cached_property
    def merchants(self) -> Merchants:
        return Merchants(self._raw_client, self._server, self._auth)

    @cached_property
    def oauth(self) -> Oauth:
        return Oauth(self._raw_client, self._server, self._auth)

    @cached_property
    def order_custom_attributes(self) -> OrderCustomAttributes:
        return OrderCustomAttributes(self._raw_client, self._server, self._auth)

    @cached_property
    def orders(self) -> Orders:
        return Orders(self._raw_client, self._server, self._auth)

    @cached_property
    def payments(self) -> Payments:
        return Payments(self._raw_client, self._server, self._auth)

    @cached_property
    def payouts(self) -> Payouts:
        return Payouts(self._raw_client, self._server, self._auth)

    @cached_property
    def refunds(self) -> Refunds:
        return Refunds(self._raw_client, self._server, self._auth)

    @cached_property
    def sites(self) -> Sites:
        return Sites(self._raw_client, self._server, self._auth)

    @cached_property
    def snippets(self) -> Snippets:
        return Snippets(self._raw_client, self._server, self._auth)

    @cached_property
    def subscriptions(self) -> Subscriptions:
        return Subscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def team(self) -> Team:
        return Team(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal(self) -> Terminal:
        return Terminal(self._raw_client, self._server, self._auth)

    @cached_property
    def transactions(self) -> Transactions:
        return Transactions(self._raw_client, self._server, self._auth)

    @cached_property
    def transfer_order_api(self) -> TransferOrderApi:
        return TransferOrderApi(self._raw_client, self._server, self._auth)

    @cached_property
    def v1_transactions(self) -> V1Transactions:
        return V1Transactions(self._raw_client, self._server, self._auth)

    @cached_property
    def vendors(self) -> Vendors:
        return Vendors(self._raw_client, self._server, self._auth)

    @cached_property
    def webhook_subscriptions(self) -> WebhookSubscriptions:
        return WebhookSubscriptions(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = SquareClient
