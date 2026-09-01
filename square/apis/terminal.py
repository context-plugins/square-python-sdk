from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.cancel_terminal_action_response import CancelTerminalActionResponse
from ..models.cancel_terminal_checkout_response import CancelTerminalCheckoutResponse
from ..models.cancel_terminal_refund_response import CancelTerminalRefundResponse
from ..models.create_terminal_action_request import CreateTerminalActionRequest, CreateTerminalActionRequestDict
from ..models.create_terminal_action_response import CreateTerminalActionResponse
from ..models.create_terminal_checkout_request import CreateTerminalCheckoutRequest, CreateTerminalCheckoutRequestDict
from ..models.create_terminal_checkout_response import CreateTerminalCheckoutResponse
from ..models.create_terminal_refund_request import CreateTerminalRefundRequest, CreateTerminalRefundRequestDict
from ..models.create_terminal_refund_response import CreateTerminalRefundResponse
from ..models.dismiss_terminal_action_response import DismissTerminalActionResponse
from ..models.dismiss_terminal_checkout_response import DismissTerminalCheckoutResponse
from ..models.dismiss_terminal_refund_response import DismissTerminalRefundResponse
from ..models.get_terminal_action_response import GetTerminalActionResponse
from ..models.get_terminal_checkout_response import GetTerminalCheckoutResponse
from ..models.get_terminal_refund_response import GetTerminalRefundResponse
from ..models.search_terminal_actions_request import SearchTerminalActionsRequest, SearchTerminalActionsRequestDict
from ..models.search_terminal_actions_response import SearchTerminalActionsResponse
from ..models.search_terminal_checkouts_request import (
    SearchTerminalCheckoutsRequest,
    SearchTerminalCheckoutsRequestDict,
)
from ..models.search_terminal_checkouts_response import SearchTerminalCheckoutsResponse
from ..models.search_terminal_refunds_request import SearchTerminalRefundsRequest, SearchTerminalRefundsRequestDict
from ..models.search_terminal_refunds_response import SearchTerminalRefundsResponse
from ..server.server import Server


class Terminal:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TerminalWithRawResponse(client, server, auth)

    def cancel_terminal_action(
        self, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelTerminalActionResponse:
        """Cancels a Terminal action request if the status of the request permits it.

        Args:
            action_id: Unique ID for the desired ``TerminalAction``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.cancel_terminal_action(action_id, request_options=request_options).unwrap()

    def cancel_terminal_checkout(
        self, checkout_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelTerminalCheckoutResponse:
        """Cancels a Terminal checkout request if the status of the request permits it.

        Args:
            checkout_id: The unique ID for the desired ``TerminalCheckout``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.cancel_terminal_checkout(checkout_id, request_options=request_options).unwrap()

    def cancel_terminal_refund(
        self, terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelTerminalRefundResponse:
        """Cancels an Interac Terminal refund request by refund request ID if the status of the request permits it.

        Args:
            terminal_refund_id: The unique ID for the desired ``TerminalRefund``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.cancel_terminal_refund(
            terminal_refund_id, request_options=request_options
        ).unwrap()

    def create_terminal_action(
        self,
        body: CreateTerminalActionRequest | CreateTerminalActionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTerminalActionResponse:
        """Creates a Terminal action request and sends it to the specified device.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_terminal_action(body, request_options=request_options).unwrap()

    def create_terminal_checkout(
        self,
        body: CreateTerminalCheckoutRequest | CreateTerminalCheckoutRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTerminalCheckoutResponse:
        """Creates a Terminal checkout request and sends it to the specified device to take a payment for the requested
        amount.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_terminal_checkout(body, request_options=request_options).unwrap()

    def create_terminal_refund(
        self,
        body: CreateTerminalRefundRequest | CreateTerminalRefundRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTerminalRefundResponse:
        """Creates a request to refund an Interac payment completed on a Square Terminal. Refunds for Interac payments
        on a Square Terminal are supported only for Interac debit cards in Canada. Other refunds for Terminal payments
        should use the Refunds API. For more information, see `Refunds API <api:Refunds>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_terminal_refund(body, request_options=request_options).unwrap()

    def dismiss_terminal_action(
        self, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DismissTerminalActionResponse:
        """Dismisses a Terminal action request if the status and type of the request permits it.

        See `Link and Dismiss Actions
        <https://developer.squareup.com/docs/terminal-api/advanced-features/custom-workflows/link-and-dismiss-actions>`__
        for more details.

        Args:
            action_id: Unique ID for the ``TerminalAction`` associated with the action to be dismissed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.dismiss_terminal_action(action_id, request_options=request_options).unwrap()

    def dismiss_terminal_checkout(
        self, checkout_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DismissTerminalCheckoutResponse:
        """Dismisses a Terminal checkout request if the status and type of the request permits it.

        Args:
            checkout_id: Unique ID for the ``TerminalCheckout`` associated with the checkout to be dismissed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.dismiss_terminal_checkout(checkout_id, request_options=request_options).unwrap()

    def dismiss_terminal_refund(
        self, terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DismissTerminalRefundResponse:
        """Dismisses a Terminal refund request if the status and type of the request permits it.

        Args:
            terminal_refund_id: Unique ID for the ``TerminalRefund`` associated with the refund to be dismissed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.dismiss_terminal_refund(
            terminal_refund_id, request_options=request_options
        ).unwrap()

    def get_terminal_action(
        self, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetTerminalActionResponse:
        """Retrieves a Terminal action request by ``action_id``. Terminal action requests are available for 30 days.

        Args:
            action_id: Unique ID for the desired ``TerminalAction``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_terminal_action(action_id, request_options=request_options).unwrap()

    def get_terminal_checkout(
        self, checkout_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetTerminalCheckoutResponse:
        """Retrieves a Terminal checkout request by ``checkout_id``. Terminal checkout requests are available for 30
        days.

        Args:
            checkout_id: The unique ID for the desired ``TerminalCheckout``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_terminal_checkout(checkout_id, request_options=request_options).unwrap()

    def get_terminal_refund(
        self, terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetTerminalRefundResponse:
        """Retrieves an Interac Terminal refund object by ID. Terminal refund objects are available for 30 days.

        Args:
            terminal_refund_id: The unique ID for the desired ``TerminalRefund``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_terminal_refund(terminal_refund_id, request_options=request_options).unwrap()

    def search_terminal_actions(
        self,
        body: SearchTerminalActionsRequest | SearchTerminalActionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchTerminalActionsResponse:
        """Retrieves a filtered list of Terminal action requests created by the account making the request. Terminal
        action requests are available for 30 days.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_terminal_actions(body, request_options=request_options).unwrap()

    def search_terminal_checkouts(
        self,
        body: SearchTerminalCheckoutsRequest | SearchTerminalCheckoutsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchTerminalCheckoutsResponse:
        """Returns a filtered list of Terminal checkout requests created by the application making the request. Only
        Terminal checkout requests created for the merchant scoped to the OAuth token are returned. Terminal checkout
        requests are available for 30 days.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_terminal_checkouts(body, request_options=request_options).unwrap()

    def search_terminal_refunds(
        self,
        body: SearchTerminalRefundsRequest | SearchTerminalRefundsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchTerminalRefundsResponse:
        """Retrieves a filtered list of Interac Terminal refund requests created by the seller making the request.
        Terminal refund requests are available for 30 days.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_terminal_refunds(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> TerminalWithRawResponse:
        return self._with_raw_response


class AsyncTerminal:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTerminalWithRawResponse(client, server, auth)

    async def cancel_terminal_action(
        self, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelTerminalActionResponse:
        """Cancels a Terminal action request if the status of the request permits it.

        Args:
            action_id: Unique ID for the desired ``TerminalAction``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.cancel_terminal_action(action_id, request_options=request_options)
        ).unwrap()

    async def cancel_terminal_checkout(
        self, checkout_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelTerminalCheckoutResponse:
        """Cancels a Terminal checkout request if the status of the request permits it.

        Args:
            checkout_id: The unique ID for the desired ``TerminalCheckout``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.cancel_terminal_checkout(checkout_id, request_options=request_options)
        ).unwrap()

    async def cancel_terminal_refund(
        self, terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelTerminalRefundResponse:
        """Cancels an Interac Terminal refund request by refund request ID if the status of the request permits it.

        Args:
            terminal_refund_id: The unique ID for the desired ``TerminalRefund``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.cancel_terminal_refund(terminal_refund_id, request_options=request_options)
        ).unwrap()

    async def create_terminal_action(
        self,
        body: CreateTerminalActionRequest | CreateTerminalActionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTerminalActionResponse:
        """Creates a Terminal action request and sends it to the specified device.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_terminal_action(body, request_options=request_options)).unwrap()

    async def create_terminal_checkout(
        self,
        body: CreateTerminalCheckoutRequest | CreateTerminalCheckoutRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTerminalCheckoutResponse:
        """Creates a Terminal checkout request and sends it to the specified device to take a payment for the requested
        amount.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_terminal_checkout(body, request_options=request_options)).unwrap()

    async def create_terminal_refund(
        self,
        body: CreateTerminalRefundRequest | CreateTerminalRefundRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTerminalRefundResponse:
        """Creates a request to refund an Interac payment completed on a Square Terminal. Refunds for Interac payments
        on a Square Terminal are supported only for Interac debit cards in Canada. Other refunds for Terminal payments
        should use the Refunds API. For more information, see `Refunds API <api:Refunds>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_terminal_refund(body, request_options=request_options)).unwrap()

    async def dismiss_terminal_action(
        self, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DismissTerminalActionResponse:
        """Dismisses a Terminal action request if the status and type of the request permits it.

        See `Link and Dismiss Actions
        <https://developer.squareup.com/docs/terminal-api/advanced-features/custom-workflows/link-and-dismiss-actions>`__
        for more details.

        Args:
            action_id: Unique ID for the ``TerminalAction`` associated with the action to be dismissed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.dismiss_terminal_action(action_id, request_options=request_options)
        ).unwrap()

    async def dismiss_terminal_checkout(
        self, checkout_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DismissTerminalCheckoutResponse:
        """Dismisses a Terminal checkout request if the status and type of the request permits it.

        Args:
            checkout_id: Unique ID for the ``TerminalCheckout`` associated with the checkout to be dismissed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.dismiss_terminal_checkout(checkout_id, request_options=request_options)
        ).unwrap()

    async def dismiss_terminal_refund(
        self, terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DismissTerminalRefundResponse:
        """Dismisses a Terminal refund request if the status and type of the request permits it.

        Args:
            terminal_refund_id: Unique ID for the ``TerminalRefund`` associated with the refund to be dismissed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.dismiss_terminal_refund(terminal_refund_id, request_options=request_options)
        ).unwrap()

    async def get_terminal_action(
        self, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetTerminalActionResponse:
        """Retrieves a Terminal action request by ``action_id``. Terminal action requests are available for 30 days.

        Args:
            action_id: Unique ID for the desired ``TerminalAction``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_terminal_action(action_id, request_options=request_options)).unwrap()

    async def get_terminal_checkout(
        self, checkout_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetTerminalCheckoutResponse:
        """Retrieves a Terminal checkout request by ``checkout_id``. Terminal checkout requests are available for 30
        days.

        Args:
            checkout_id: The unique ID for the desired ``TerminalCheckout``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_terminal_checkout(checkout_id, request_options=request_options)
        ).unwrap()

    async def get_terminal_refund(
        self, terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetTerminalRefundResponse:
        """Retrieves an Interac Terminal refund object by ID. Terminal refund objects are available for 30 days.

        Args:
            terminal_refund_id: The unique ID for the desired ``TerminalRefund``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_terminal_refund(terminal_refund_id, request_options=request_options)
        ).unwrap()

    async def search_terminal_actions(
        self,
        body: SearchTerminalActionsRequest | SearchTerminalActionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchTerminalActionsResponse:
        """Retrieves a filtered list of Terminal action requests created by the account making the request. Terminal
        action requests are available for 30 days.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search_terminal_actions(body, request_options=request_options)).unwrap()

    async def search_terminal_checkouts(
        self,
        body: SearchTerminalCheckoutsRequest | SearchTerminalCheckoutsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchTerminalCheckoutsResponse:
        """Returns a filtered list of Terminal checkout requests created by the application making the request. Only
        Terminal checkout requests created for the merchant scoped to the OAuth token are returned. Terminal checkout
        requests are available for 30 days.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search_terminal_checkouts(body, request_options=request_options)).unwrap()

    async def search_terminal_refunds(
        self,
        body: SearchTerminalRefundsRequest | SearchTerminalRefundsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchTerminalRefundsResponse:
        """Retrieves a filtered list of Interac Terminal refund requests created by the seller making the request.
        Terminal refund requests are available for 30 days.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search_terminal_refunds(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncTerminalWithRawResponse:
        return self._with_raw_response


class TerminalWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_terminal_action(
        self, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelTerminalActionResponse, RawError]:
        """Cancels a Terminal action request if the status of the request permits it.

        Args:
            action_id: Unique ID for the desired ``TerminalAction``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/actions/{action_id}/cancel"),
            path_params=[param[str]("action_id", action_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelTerminalActionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def cancel_terminal_checkout(
        self, checkout_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelTerminalCheckoutResponse, RawError]:
        """Cancels a Terminal checkout request if the status of the request permits it.

        Args:
            checkout_id: The unique ID for the desired ``TerminalCheckout``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/checkouts/{checkout_id}/cancel"),
            path_params=[param[str]("checkout_id", checkout_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelTerminalCheckoutResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def cancel_terminal_refund(
        self, terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelTerminalRefundResponse, RawError]:
        """Cancels an Interac Terminal refund request by refund request ID if the status of the request permits it.

        Args:
            terminal_refund_id: The unique ID for the desired ``TerminalRefund``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/refunds/{terminal_refund_id}/cancel"),
            path_params=[param[str]("terminal_refund_id", terminal_refund_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelTerminalRefundResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_terminal_action(
        self,
        body: CreateTerminalActionRequest | CreateTerminalActionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTerminalActionResponse, RawError]:
        """Creates a Terminal action request and sends it to the specified device.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/actions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTerminalActionRequest | CreateTerminalActionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateTerminalActionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_terminal_checkout(
        self,
        body: CreateTerminalCheckoutRequest | CreateTerminalCheckoutRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTerminalCheckoutResponse, RawError]:
        """Creates a Terminal checkout request and sends it to the specified device to take a payment for the requested
        amount.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/checkouts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTerminalCheckoutRequest | CreateTerminalCheckoutRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateTerminalCheckoutResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_terminal_refund(
        self,
        body: CreateTerminalRefundRequest | CreateTerminalRefundRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTerminalRefundResponse, RawError]:
        """Creates a request to refund an Interac payment completed on a Square Terminal. Refunds for Interac payments
        on a Square Terminal are supported only for Interac debit cards in Canada. Other refunds for Terminal payments
        should use the Refunds API. For more information, see `Refunds API <api:Refunds>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/refunds"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTerminalRefundRequest | CreateTerminalRefundRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateTerminalRefundResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def dismiss_terminal_action(
        self, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DismissTerminalActionResponse, RawError]:
        """Dismisses a Terminal action request if the status and type of the request permits it.

        See `Link and Dismiss Actions
        <https://developer.squareup.com/docs/terminal-api/advanced-features/custom-workflows/link-and-dismiss-actions>`__
        for more details.

        Args:
            action_id: Unique ID for the ``TerminalAction`` associated with the action to be dismissed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/actions/{action_id}/dismiss"),
            path_params=[param[str]("action_id", action_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DismissTerminalActionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def dismiss_terminal_checkout(
        self, checkout_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DismissTerminalCheckoutResponse, RawError]:
        """Dismisses a Terminal checkout request if the status and type of the request permits it.

        Args:
            checkout_id: Unique ID for the ``TerminalCheckout`` associated with the checkout to be dismissed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/checkouts/{checkout_id}/dismiss"),
            path_params=[param[str]("checkout_id", checkout_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DismissTerminalCheckoutResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def dismiss_terminal_refund(
        self, terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DismissTerminalRefundResponse, RawError]:
        """Dismisses a Terminal refund request if the status and type of the request permits it.

        Args:
            terminal_refund_id: Unique ID for the ``TerminalRefund`` associated with the refund to be dismissed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/refunds/{terminal_refund_id}/dismiss"),
            path_params=[param[str]("terminal_refund_id", terminal_refund_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DismissTerminalRefundResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_terminal_action(
        self, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetTerminalActionResponse, RawError]:
        """Retrieves a Terminal action request by ``action_id``. Terminal action requests are available for 30 days.

        Args:
            action_id: Unique ID for the desired ``TerminalAction``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/terminals/actions/{action_id}"),
            path_params=[param[str]("action_id", action_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetTerminalActionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_terminal_checkout(
        self, checkout_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetTerminalCheckoutResponse, RawError]:
        """Retrieves a Terminal checkout request by ``checkout_id``. Terminal checkout requests are available for 30
        days.

        Args:
            checkout_id: The unique ID for the desired ``TerminalCheckout``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/terminals/checkouts/{checkout_id}"),
            path_params=[param[str]("checkout_id", checkout_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetTerminalCheckoutResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_terminal_refund(
        self, terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetTerminalRefundResponse, RawError]:
        """Retrieves an Interac Terminal refund object by ID. Terminal refund objects are available for 30 days.

        Args:
            terminal_refund_id: The unique ID for the desired ``TerminalRefund``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/terminals/refunds/{terminal_refund_id}"),
            path_params=[param[str]("terminal_refund_id", terminal_refund_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetTerminalRefundResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_terminal_actions(
        self,
        body: SearchTerminalActionsRequest | SearchTerminalActionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchTerminalActionsResponse, RawError]:
        """Retrieves a filtered list of Terminal action requests created by the account making the request. Terminal
        action requests are available for 30 days.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/actions/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchTerminalActionsRequest | SearchTerminalActionsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchTerminalActionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_terminal_checkouts(
        self,
        body: SearchTerminalCheckoutsRequest | SearchTerminalCheckoutsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchTerminalCheckoutsResponse, RawError]:
        """Returns a filtered list of Terminal checkout requests created by the application making the request. Only
        Terminal checkout requests created for the merchant scoped to the OAuth token are returned. Terminal checkout
        requests are available for 30 days.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/checkouts/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchTerminalCheckoutsRequest | SearchTerminalCheckoutsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchTerminalCheckoutsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_terminal_refunds(
        self,
        body: SearchTerminalRefundsRequest | SearchTerminalRefundsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchTerminalRefundsResponse, RawError]:
        """Retrieves a filtered list of Interac Terminal refund requests created by the seller making the request.
        Terminal refund requests are available for 30 days.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/refunds/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchTerminalRefundsRequest | SearchTerminalRefundsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchTerminalRefundsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTerminalWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_terminal_action(
        self, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelTerminalActionResponse, RawError]:
        """Cancels a Terminal action request if the status of the request permits it.

        Args:
            action_id: Unique ID for the desired ``TerminalAction``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/actions/{action_id}/cancel"),
            path_params=[param[str]("action_id", action_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelTerminalActionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def cancel_terminal_checkout(
        self, checkout_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelTerminalCheckoutResponse, RawError]:
        """Cancels a Terminal checkout request if the status of the request permits it.

        Args:
            checkout_id: The unique ID for the desired ``TerminalCheckout``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/checkouts/{checkout_id}/cancel"),
            path_params=[param[str]("checkout_id", checkout_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelTerminalCheckoutResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def cancel_terminal_refund(
        self, terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelTerminalRefundResponse, RawError]:
        """Cancels an Interac Terminal refund request by refund request ID if the status of the request permits it.

        Args:
            terminal_refund_id: The unique ID for the desired ``TerminalRefund``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/refunds/{terminal_refund_id}/cancel"),
            path_params=[param[str]("terminal_refund_id", terminal_refund_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelTerminalRefundResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_terminal_action(
        self,
        body: CreateTerminalActionRequest | CreateTerminalActionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTerminalActionResponse, RawError]:
        """Creates a Terminal action request and sends it to the specified device.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/actions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTerminalActionRequest | CreateTerminalActionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateTerminalActionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_terminal_checkout(
        self,
        body: CreateTerminalCheckoutRequest | CreateTerminalCheckoutRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTerminalCheckoutResponse, RawError]:
        """Creates a Terminal checkout request and sends it to the specified device to take a payment for the requested
        amount.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/checkouts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTerminalCheckoutRequest | CreateTerminalCheckoutRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateTerminalCheckoutResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_terminal_refund(
        self,
        body: CreateTerminalRefundRequest | CreateTerminalRefundRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTerminalRefundResponse, RawError]:
        """Creates a request to refund an Interac payment completed on a Square Terminal. Refunds for Interac payments
        on a Square Terminal are supported only for Interac debit cards in Canada. Other refunds for Terminal payments
        should use the Refunds API. For more information, see `Refunds API <api:Refunds>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/refunds"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTerminalRefundRequest | CreateTerminalRefundRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateTerminalRefundResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def dismiss_terminal_action(
        self, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DismissTerminalActionResponse, RawError]:
        """Dismisses a Terminal action request if the status and type of the request permits it.

        See `Link and Dismiss Actions
        <https://developer.squareup.com/docs/terminal-api/advanced-features/custom-workflows/link-and-dismiss-actions>`__
        for more details.

        Args:
            action_id: Unique ID for the ``TerminalAction`` associated with the action to be dismissed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/actions/{action_id}/dismiss"),
            path_params=[param[str]("action_id", action_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DismissTerminalActionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def dismiss_terminal_checkout(
        self, checkout_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DismissTerminalCheckoutResponse, RawError]:
        """Dismisses a Terminal checkout request if the status and type of the request permits it.

        Args:
            checkout_id: Unique ID for the ``TerminalCheckout`` associated with the checkout to be dismissed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/checkouts/{checkout_id}/dismiss"),
            path_params=[param[str]("checkout_id", checkout_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DismissTerminalCheckoutResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def dismiss_terminal_refund(
        self, terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DismissTerminalRefundResponse, RawError]:
        """Dismisses a Terminal refund request if the status and type of the request permits it.

        Args:
            terminal_refund_id: Unique ID for the ``TerminalRefund`` associated with the refund to be dismissed.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/refunds/{terminal_refund_id}/dismiss"),
            path_params=[param[str]("terminal_refund_id", terminal_refund_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DismissTerminalRefundResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_terminal_action(
        self, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetTerminalActionResponse, RawError]:
        """Retrieves a Terminal action request by ``action_id``. Terminal action requests are available for 30 days.

        Args:
            action_id: Unique ID for the desired ``TerminalAction``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/terminals/actions/{action_id}"),
            path_params=[param[str]("action_id", action_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetTerminalActionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_terminal_checkout(
        self, checkout_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetTerminalCheckoutResponse, RawError]:
        """Retrieves a Terminal checkout request by ``checkout_id``. Terminal checkout requests are available for 30
        days.

        Args:
            checkout_id: The unique ID for the desired ``TerminalCheckout``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/terminals/checkouts/{checkout_id}"),
            path_params=[param[str]("checkout_id", checkout_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetTerminalCheckoutResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_terminal_refund(
        self, terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetTerminalRefundResponse, RawError]:
        """Retrieves an Interac Terminal refund object by ID. Terminal refund objects are available for 30 days.

        Args:
            terminal_refund_id: The unique ID for the desired ``TerminalRefund``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/terminals/refunds/{terminal_refund_id}"),
            path_params=[param[str]("terminal_refund_id", terminal_refund_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetTerminalRefundResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_terminal_actions(
        self,
        body: SearchTerminalActionsRequest | SearchTerminalActionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchTerminalActionsResponse, RawError]:
        """Retrieves a filtered list of Terminal action requests created by the account making the request. Terminal
        action requests are available for 30 days.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/actions/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchTerminalActionsRequest | SearchTerminalActionsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchTerminalActionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_terminal_checkouts(
        self,
        body: SearchTerminalCheckoutsRequest | SearchTerminalCheckoutsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchTerminalCheckoutsResponse, RawError]:
        """Returns a filtered list of Terminal checkout requests created by the application making the request. Only
        Terminal checkout requests created for the merchant scoped to the OAuth token are returned. Terminal checkout
        requests are available for 30 days.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/checkouts/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchTerminalCheckoutsRequest | SearchTerminalCheckoutsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchTerminalCheckoutsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_terminal_refunds(
        self,
        body: SearchTerminalRefundsRequest | SearchTerminalRefundsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchTerminalRefundsResponse, RawError]:
        """Retrieves a filtered list of Interac Terminal refund requests created by the seller making the request.
        Terminal refund requests are available for 30 days.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/terminals/refunds/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchTerminalRefundsRequest | SearchTerminalRefundsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchTerminalRefundsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
