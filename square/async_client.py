from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.apple_pay import AsyncApplePay
from .apis.bank_accounts import AsyncBankAccounts
from .apis.booking_custom_attributes import AsyncBookingCustomAttributes
from .apis.bookings import AsyncBookings
from .apis.cards import AsyncCards
from .apis.cash_drawers import AsyncCashDrawers
from .apis.catalog import AsyncCatalog
from .apis.channels import AsyncChannels
from .apis.checkout_api import AsyncCheckoutApi
from .apis.customer_custom_attributes import AsyncCustomerCustomAttributes
from .apis.customer_groups import AsyncCustomerGroups
from .apis.customer_segments import AsyncCustomerSegments
from .apis.customers import AsyncCustomers
from .apis.devices import AsyncDevices
from .apis.disputes import AsyncDisputes
from .apis.employees import AsyncEmployees
from .apis.events import AsyncEvents
from .apis.gift_card_activities import AsyncGiftCardActivities
from .apis.gift_cards import AsyncGiftCards
from .apis.inventory import AsyncInventory
from .apis.invoices import AsyncInvoices
from .apis.labor import AsyncLabor
from .apis.location_custom_attributes import AsyncLocationCustomAttributes
from .apis.locations import AsyncLocations
from .apis.loyalty import AsyncLoyalty
from .apis.merchant_custom_attributes import AsyncMerchantCustomAttributes
from .apis.merchants import AsyncMerchants
from .apis.oauth import AsyncOauth
from .apis.order_custom_attributes import AsyncOrderCustomAttributes
from .apis.orders import AsyncOrders
from .apis.payments import AsyncPayments
from .apis.payouts import AsyncPayouts
from .apis.refunds import AsyncRefunds
from .apis.sites import AsyncSites
from .apis.snippets import AsyncSnippets
from .apis.subscriptions import AsyncSubscriptions
from .apis.team import AsyncTeam
from .apis.terminal import AsyncTerminal
from .apis.transactions import AsyncTransactions
from .apis.transfer_order_api import AsyncTransferOrderApi
from .apis.v1_transactions import AsyncV1Transactions
from .apis.vendors import AsyncVendors
from .apis.webhook_subscriptions import AsyncWebhookSubscriptions
from .auth import AsyncAuthSchemes, Oauth2Scope
from .base_client import DEFAULT_TIMEOUT, BaseSquareClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    AsyncAuthorizationCodeCredentials,
    AsyncAuthorizationCodeCredentialsOrDict,
    AsyncAuthorizationCodeTokenSource,
    AsyncHttpClient,
    AsyncHttpx2Client,
    AsyncOAuth2RefreshableScheme,
    AsyncRawClient,
    AsyncRefreshableTokenSource,
    RetryOptionsOrDict,
    client_secret_basic,
    no_auth,
    param,
)
from .server.environment import Environment


class AsyncSquareClient(BaseSquareClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        custom_async_http_client: AsyncHttpClient | None = None,
        oauth2: AsyncAuthorizationCodeCredentialsOrDict[Oauth2Scope] | None = None,
        oauth2_token_source: AsyncRefreshableTokenSource[AsyncAuthorizationCodeCredentials[Oauth2Scope]] | None = None,
        oauth2_client_secret: str | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout, retry_options=retry_options)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpx2Client(timeout=timeout)
            ),
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
        self._auth = AsyncAuthSchemes(
            oauth2=(
                AsyncOAuth2RefreshableScheme(
                    credentials=AsyncAuthorizationCodeCredentials[Oauth2Scope].coerce(oauth2),
                    source=(
                        oauth2_token_source
                        if oauth2_token_source is not None
                        else AsyncAuthorizationCodeTokenSource[Oauth2Scope](
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
    def apple_pay(self) -> AsyncApplePay:
        return AsyncApplePay(self._raw_client, self._server, self._auth)

    @cached_property
    def bank_accounts(self) -> AsyncBankAccounts:
        return AsyncBankAccounts(self._raw_client, self._server, self._auth)

    @cached_property
    def booking_custom_attributes(self) -> AsyncBookingCustomAttributes:
        return AsyncBookingCustomAttributes(self._raw_client, self._server, self._auth)

    @cached_property
    def bookings(self) -> AsyncBookings:
        return AsyncBookings(self._raw_client, self._server, self._auth)

    @cached_property
    def cards(self) -> AsyncCards:
        return AsyncCards(self._raw_client, self._server, self._auth)

    @cached_property
    def cash_drawers(self) -> AsyncCashDrawers:
        return AsyncCashDrawers(self._raw_client, self._server, self._auth)

    @cached_property
    def catalog(self) -> AsyncCatalog:
        return AsyncCatalog(self._raw_client, self._server, self._auth)

    @cached_property
    def channels(self) -> AsyncChannels:
        return AsyncChannels(self._raw_client, self._server, self._auth)

    @cached_property
    def checkout_api(self) -> AsyncCheckoutApi:
        return AsyncCheckoutApi(self._raw_client, self._server, self._auth)

    @cached_property
    def customer_custom_attributes(self) -> AsyncCustomerCustomAttributes:
        return AsyncCustomerCustomAttributes(self._raw_client, self._server, self._auth)

    @cached_property
    def customer_groups(self) -> AsyncCustomerGroups:
        return AsyncCustomerGroups(self._raw_client, self._server, self._auth)

    @cached_property
    def customer_segments(self) -> AsyncCustomerSegments:
        return AsyncCustomerSegments(self._raw_client, self._server, self._auth)

    @cached_property
    def customers(self) -> AsyncCustomers:
        return AsyncCustomers(self._raw_client, self._server, self._auth)

    @cached_property
    def devices(self) -> AsyncDevices:
        return AsyncDevices(self._raw_client, self._server, self._auth)

    @cached_property
    def disputes(self) -> AsyncDisputes:
        return AsyncDisputes(self._raw_client, self._server, self._auth)

    @cached_property
    def employees(self) -> AsyncEmployees:
        return AsyncEmployees(self._raw_client, self._server, self._auth)

    @cached_property
    def events(self) -> AsyncEvents:
        return AsyncEvents(self._raw_client, self._server, self._auth)

    @cached_property
    def gift_card_activities(self) -> AsyncGiftCardActivities:
        return AsyncGiftCardActivities(self._raw_client, self._server, self._auth)

    @cached_property
    def gift_cards(self) -> AsyncGiftCards:
        return AsyncGiftCards(self._raw_client, self._server, self._auth)

    @cached_property
    def inventory(self) -> AsyncInventory:
        return AsyncInventory(self._raw_client, self._server, self._auth)

    @cached_property
    def invoices(self) -> AsyncInvoices:
        return AsyncInvoices(self._raw_client, self._server, self._auth)

    @cached_property
    def labor(self) -> AsyncLabor:
        return AsyncLabor(self._raw_client, self._server, self._auth)

    @cached_property
    def location_custom_attributes(self) -> AsyncLocationCustomAttributes:
        return AsyncLocationCustomAttributes(self._raw_client, self._server, self._auth)

    @cached_property
    def locations(self) -> AsyncLocations:
        return AsyncLocations(self._raw_client, self._server, self._auth)

    @cached_property
    def loyalty(self) -> AsyncLoyalty:
        return AsyncLoyalty(self._raw_client, self._server, self._auth)

    @cached_property
    def merchant_custom_attributes(self) -> AsyncMerchantCustomAttributes:
        return AsyncMerchantCustomAttributes(self._raw_client, self._server, self._auth)

    @cached_property
    def merchants(self) -> AsyncMerchants:
        return AsyncMerchants(self._raw_client, self._server, self._auth)

    @cached_property
    def oauth(self) -> AsyncOauth:
        return AsyncOauth(self._raw_client, self._server, self._auth)

    @cached_property
    def order_custom_attributes(self) -> AsyncOrderCustomAttributes:
        return AsyncOrderCustomAttributes(self._raw_client, self._server, self._auth)

    @cached_property
    def orders(self) -> AsyncOrders:
        return AsyncOrders(self._raw_client, self._server, self._auth)

    @cached_property
    def payments(self) -> AsyncPayments:
        return AsyncPayments(self._raw_client, self._server, self._auth)

    @cached_property
    def payouts(self) -> AsyncPayouts:
        return AsyncPayouts(self._raw_client, self._server, self._auth)

    @cached_property
    def refunds(self) -> AsyncRefunds:
        return AsyncRefunds(self._raw_client, self._server, self._auth)

    @cached_property
    def sites(self) -> AsyncSites:
        return AsyncSites(self._raw_client, self._server, self._auth)

    @cached_property
    def snippets(self) -> AsyncSnippets:
        return AsyncSnippets(self._raw_client, self._server, self._auth)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptions:
        return AsyncSubscriptions(self._raw_client, self._server, self._auth)

    @cached_property
    def team(self) -> AsyncTeam:
        return AsyncTeam(self._raw_client, self._server, self._auth)

    @cached_property
    def terminal(self) -> AsyncTerminal:
        return AsyncTerminal(self._raw_client, self._server, self._auth)

    @cached_property
    def transactions(self) -> AsyncTransactions:
        return AsyncTransactions(self._raw_client, self._server, self._auth)

    @cached_property
    def transfer_order_api(self) -> AsyncTransferOrderApi:
        return AsyncTransferOrderApi(self._raw_client, self._server, self._auth)

    @cached_property
    def v1_transactions(self) -> AsyncV1Transactions:
        return AsyncV1Transactions(self._raw_client, self._server, self._auth)

    @cached_property
    def vendors(self) -> AsyncVendors:
        return AsyncVendors(self._raw_client, self._server, self._auth)

    @cached_property
    def webhook_subscriptions(self) -> AsyncWebhookSubscriptions:
        return AsyncWebhookSubscriptions(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncSquareClient
