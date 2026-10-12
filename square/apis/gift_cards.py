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
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.create_gift_card_request import CreateGiftCardRequest, CreateGiftCardRequestDict
from ..models.create_gift_card_response import CreateGiftCardResponse
from ..models.link_customer_to_gift_card_request import LinkCustomerToGiftCardRequest, LinkCustomerToGiftCardRequestDict
from ..models.link_customer_to_gift_card_response import LinkCustomerToGiftCardResponse
from ..models.list_gift_cards_response import ListGiftCardsResponse
from ..models.retrieve_gift_card_from_ganrequest import (
    RetrieveGiftCardFromGanrequest,
    RetrieveGiftCardFromGanrequestDict,
)
from ..models.retrieve_gift_card_from_ganresponse import RetrieveGiftCardFromGanresponse
from ..models.retrieve_gift_card_from_nonce_request import (
    RetrieveGiftCardFromNonceRequest,
    RetrieveGiftCardFromNonceRequestDict,
)
from ..models.retrieve_gift_card_from_nonce_response import RetrieveGiftCardFromNonceResponse
from ..models.retrieve_gift_card_response import RetrieveGiftCardResponse
from ..models.unlink_customer_from_gift_card_request import (
    UnlinkCustomerFromGiftCardRequest,
    UnlinkCustomerFromGiftCardRequestDict,
)
from ..models.unlink_customer_from_gift_card_response import UnlinkCustomerFromGiftCardResponse
from ..server.server import Server


class GiftCards:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GiftCardsWithRawResponse(client, server, auth)

    def create_gift_card(
        self,
        body: CreateGiftCardRequest | CreateGiftCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateGiftCardResponse:
        """Creates a digital gift card or registers a physical (plastic) gift card. The resulting gift card has a
        ``PENDING`` state. To activate a gift card so that it can be redeemed for purchases, call
        `CreateGiftCardActivity <api-endpoint:GiftCardActivities-CreateGiftCardActivity>`__ and create an ``ACTIVATE``
        activity with the initial balance. Alternatively, you can use `RefundPayment
        <api-endpoint:Refunds-RefundPayment>`__ to refund a payment to the new gift card.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_gift_card(body, request_options=request_options))

    def link_customer_to_gift_card(
        self,
        gift_card_id: str,
        body: LinkCustomerToGiftCardRequest | LinkCustomerToGiftCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LinkCustomerToGiftCardResponse:
        """Links a customer to a gift card, which is also referred to as adding a card on file.

        Args:
            gift_card_id: The ID of the gift card to be linked.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.link_customer_to_gift_card(gift_card_id, body, request_options=request_options)
        )

    def list_gift_cards(
        self,
        *,
        type_: str | None = None,
        state: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        customer_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListGiftCardsResponse:
        """Lists all gift cards. You can specify optional filters to retrieve a subset of the gift cards. Results are
        sorted by ``created_at`` in ascending order.

        Args:
            type_: If a `type <entity:GiftCardType>`__ is provided, the endpoint returns gift cards of the specified
                type. Otherwise, the endpoint returns gift cards of all types.
            state: If a `state <entity:GiftCardStatus>`__ is provided, the endpoint returns the gift cards in the
                specified state. Otherwise, the endpoint returns the gift cards of all states.
            limit: If a limit is provided, the endpoint returns only the specified number of results per page. The
                maximum value is 200. The default value is 30. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. If a cursor is not provided, the endpoint returns the
                first page of the results. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            customer_id: If a customer ID is provided, the endpoint returns only the gift cards linked to the specified
                customer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_gift_cards(
                type_=type_,
                state=state,
                limit=limit,
                cursor=cursor,
                customer_id=customer_id,
                request_options=request_options,
            ),
        )

    def retrieve_gift_card(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveGiftCardResponse:
        """Retrieves a gift card using the gift card ID.

        Args:
            id_: The ID of the gift card to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_gift_card(id_, request_options=request_options))

    def retrieve_gift_card_from_gan(
        self,
        body: RetrieveGiftCardFromGanrequest | RetrieveGiftCardFromGanrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveGiftCardFromGanresponse:
        """Retrieves a gift card using the gift card account number (GAN).

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_gift_card_from_gan(body, request_options=request_options))

    def retrieve_gift_card_from_nonce(
        self,
        body: RetrieveGiftCardFromNonceRequest | RetrieveGiftCardFromNonceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveGiftCardFromNonceResponse:
        """Retrieves a gift card using a secure payment token that represents the gift card.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_gift_card_from_nonce(body, request_options=request_options))

    def unlink_customer_from_gift_card(
        self,
        gift_card_id: str,
        body: UnlinkCustomerFromGiftCardRequest | UnlinkCustomerFromGiftCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UnlinkCustomerFromGiftCardResponse:
        """Unlinks a customer from a gift card, which is also referred to as removing a card on file.

        Args:
            gift_card_id: The ID of the gift card to be unlinked.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.unlink_customer_from_gift_card(gift_card_id, body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> GiftCardsWithRawResponse:
        return self._with_raw_response


class AsyncGiftCards:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGiftCardsWithRawResponse(client, server, auth)

    async def create_gift_card(
        self,
        body: CreateGiftCardRequest | CreateGiftCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateGiftCardResponse:
        """Creates a digital gift card or registers a physical (plastic) gift card. The resulting gift card has a
        ``PENDING`` state. To activate a gift card so that it can be redeemed for purchases, call
        `CreateGiftCardActivity <api-endpoint:GiftCardActivities-CreateGiftCardActivity>`__ and create an ``ACTIVATE``
        activity with the initial balance. Alternatively, you can use `RefundPayment
        <api-endpoint:Refunds-RefundPayment>`__ to refund a payment to the new gift card.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_gift_card(body, request_options=request_options))

    async def link_customer_to_gift_card(
        self,
        gift_card_id: str,
        body: LinkCustomerToGiftCardRequest | LinkCustomerToGiftCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> LinkCustomerToGiftCardResponse:
        """Links a customer to a gift card, which is also referred to as adding a card on file.

        Args:
            gift_card_id: The ID of the gift card to be linked.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.link_customer_to_gift_card(
                gift_card_id, body, request_options=request_options
            ),
        )

    async def list_gift_cards(
        self,
        *,
        type_: str | None = None,
        state: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        customer_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListGiftCardsResponse:
        """Lists all gift cards. You can specify optional filters to retrieve a subset of the gift cards. Results are
        sorted by ``created_at`` in ascending order.

        Args:
            type_: If a `type <entity:GiftCardType>`__ is provided, the endpoint returns gift cards of the specified
                type. Otherwise, the endpoint returns gift cards of all types.
            state: If a `state <entity:GiftCardStatus>`__ is provided, the endpoint returns the gift cards in the
                specified state. Otherwise, the endpoint returns the gift cards of all states.
            limit: If a limit is provided, the endpoint returns only the specified number of results per page. The
                maximum value is 200. The default value is 30. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. If a cursor is not provided, the endpoint returns the
                first page of the results. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            customer_id: If a customer ID is provided, the endpoint returns only the gift cards linked to the specified
                customer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_gift_cards(
                type_=type_,
                state=state,
                limit=limit,
                cursor=cursor,
                customer_id=customer_id,
                request_options=request_options,
            ),
        )

    async def retrieve_gift_card(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveGiftCardResponse:
        """Retrieves a gift card using the gift card ID.

        Args:
            id_: The ID of the gift card to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.retrieve_gift_card(id_, request_options=request_options))

    async def retrieve_gift_card_from_gan(
        self,
        body: RetrieveGiftCardFromGanrequest | RetrieveGiftCardFromGanrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveGiftCardFromGanresponse:
        """Retrieves a gift card using the gift card account number (GAN).

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.retrieve_gift_card_from_gan(body, request_options=request_options))

    async def retrieve_gift_card_from_nonce(
        self,
        body: RetrieveGiftCardFromNonceRequest | RetrieveGiftCardFromNonceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveGiftCardFromNonceResponse:
        """Retrieves a gift card using a secure payment token that represents the gift card.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.retrieve_gift_card_from_nonce(body, request_options=request_options)
        )

    async def unlink_customer_from_gift_card(
        self,
        gift_card_id: str,
        body: UnlinkCustomerFromGiftCardRequest | UnlinkCustomerFromGiftCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UnlinkCustomerFromGiftCardResponse:
        """Unlinks a customer from a gift card, which is also referred to as removing a card on file.

        Args:
            gift_card_id: The ID of the gift card to be unlinked.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.unlink_customer_from_gift_card(
                gift_card_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncGiftCardsWithRawResponse:
        return self._with_raw_response


class GiftCardsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_gift_card(
        self,
        body: CreateGiftCardRequest | CreateGiftCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateGiftCardResponse, RawError]:
        """Creates a digital gift card or registers a physical (plastic) gift card. The resulting gift card has a
        ``PENDING`` state. To activate a gift card so that it can be redeemed for purchases, call
        `CreateGiftCardActivity <api-endpoint:GiftCardActivities-CreateGiftCardActivity>`__ and create an ``ACTIVATE``
        activity with the initial balance. Alternatively, you can use `RefundPayment
        <api-endpoint:Refunds-RefundPayment>`__ to refund a payment to the new gift card.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/gift-cards"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateGiftCardRequest | CreateGiftCardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateGiftCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def link_customer_to_gift_card(
        self,
        gift_card_id: str,
        body: LinkCustomerToGiftCardRequest | LinkCustomerToGiftCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LinkCustomerToGiftCardResponse, RawError]:
        """Links a customer to a gift card, which is also referred to as adding a card on file.

        Args:
            gift_card_id: The ID of the gift card to be linked.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/gift-cards/{gift_card_id}/link-customer"),
            path_params=[param[str]("gift_card_id", gift_card_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LinkCustomerToGiftCardRequest | LinkCustomerToGiftCardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[LinkCustomerToGiftCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_gift_cards(
        self,
        *,
        type_: str | None = None,
        state: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        customer_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListGiftCardsResponse, RawError]:
        """Lists all gift cards. You can specify optional filters to retrieve a subset of the gift cards. Results are
        sorted by ``created_at`` in ascending order.

        Args:
            type_: If a `type <entity:GiftCardType>`__ is provided, the endpoint returns gift cards of the specified
                type. Otherwise, the endpoint returns gift cards of all types.
            state: If a `state <entity:GiftCardStatus>`__ is provided, the endpoint returns the gift cards in the
                specified state. Otherwise, the endpoint returns the gift cards of all states.
            limit: If a limit is provided, the endpoint returns only the specified number of results per page. The
                maximum value is 200. The default value is 30. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. If a cursor is not provided, the endpoint returns the
                first page of the results. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            customer_id: If a customer ID is provided, the endpoint returns only the gift cards linked to the specified
                customer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/gift-cards"),
            query_params=[
                param[str | None]("type", type_),
                param[str | None]("state", state),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("customer_id", customer_id),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListGiftCardsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_gift_card(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveGiftCardResponse, RawError]:
        """Retrieves a gift card using the gift card ID.

        Args:
            id_: The ID of the gift card to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/gift-cards/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveGiftCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_gift_card_from_gan(
        self,
        body: RetrieveGiftCardFromGanrequest | RetrieveGiftCardFromGanrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveGiftCardFromGanresponse, RawError]:
        """Retrieves a gift card using the gift card account number (GAN).

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/gift-cards/from-gan"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RetrieveGiftCardFromGanrequest | RetrieveGiftCardFromGanrequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveGiftCardFromGanresponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_gift_card_from_nonce(
        self,
        body: RetrieveGiftCardFromNonceRequest | RetrieveGiftCardFromNonceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveGiftCardFromNonceResponse, RawError]:
        """Retrieves a gift card using a secure payment token that represents the gift card.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/gift-cards/from-nonce"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RetrieveGiftCardFromNonceRequest | RetrieveGiftCardFromNonceRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveGiftCardFromNonceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def unlink_customer_from_gift_card(
        self,
        gift_card_id: str,
        body: UnlinkCustomerFromGiftCardRequest | UnlinkCustomerFromGiftCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UnlinkCustomerFromGiftCardResponse, RawError]:
        """Unlinks a customer from a gift card, which is also referred to as removing a card on file.

        Args:
            gift_card_id: The ID of the gift card to be unlinked.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/gift-cards/{gift_card_id}/unlink-customer"),
            path_params=[param[str]("gift_card_id", gift_card_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UnlinkCustomerFromGiftCardRequest | UnlinkCustomerFromGiftCardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UnlinkCustomerFromGiftCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncGiftCardsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_gift_card(
        self,
        body: CreateGiftCardRequest | CreateGiftCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateGiftCardResponse, RawError]:
        """Creates a digital gift card or registers a physical (plastic) gift card. The resulting gift card has a
        ``PENDING`` state. To activate a gift card so that it can be redeemed for purchases, call
        `CreateGiftCardActivity <api-endpoint:GiftCardActivities-CreateGiftCardActivity>`__ and create an ``ACTIVATE``
        activity with the initial balance. Alternatively, you can use `RefundPayment
        <api-endpoint:Refunds-RefundPayment>`__ to refund a payment to the new gift card.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/gift-cards"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateGiftCardRequest | CreateGiftCardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CreateGiftCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def link_customer_to_gift_card(
        self,
        gift_card_id: str,
        body: LinkCustomerToGiftCardRequest | LinkCustomerToGiftCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[LinkCustomerToGiftCardResponse, RawError]:
        """Links a customer to a gift card, which is also referred to as adding a card on file.

        Args:
            gift_card_id: The ID of the gift card to be linked.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/gift-cards/{gift_card_id}/link-customer"),
            path_params=[param[str]("gift_card_id", gift_card_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[LinkCustomerToGiftCardRequest | LinkCustomerToGiftCardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[LinkCustomerToGiftCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_gift_cards(
        self,
        *,
        type_: str | None = None,
        state: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        customer_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListGiftCardsResponse, RawError]:
        """Lists all gift cards. You can specify optional filters to retrieve a subset of the gift cards. Results are
        sorted by ``created_at`` in ascending order.

        Args:
            type_: If a `type <entity:GiftCardType>`__ is provided, the endpoint returns gift cards of the specified
                type. Otherwise, the endpoint returns gift cards of all types.
            state: If a `state <entity:GiftCardStatus>`__ is provided, the endpoint returns the gift cards in the
                specified state. Otherwise, the endpoint returns the gift cards of all states.
            limit: If a limit is provided, the endpoint returns only the specified number of results per page. The
                maximum value is 200. The default value is 30. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. If a cursor is not provided, the endpoint returns the
                first page of the results. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            customer_id: If a customer ID is provided, the endpoint returns only the gift cards linked to the specified
                customer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/gift-cards"),
            query_params=[
                param[str | None]("type", type_),
                param[str | None]("state", state),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("customer_id", customer_id),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListGiftCardsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_gift_card(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveGiftCardResponse, RawError]:
        """Retrieves a gift card using the gift card ID.

        Args:
            id_: The ID of the gift card to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/gift-cards/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveGiftCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_gift_card_from_gan(
        self,
        body: RetrieveGiftCardFromGanrequest | RetrieveGiftCardFromGanrequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveGiftCardFromGanresponse, RawError]:
        """Retrieves a gift card using the gift card account number (GAN).

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/gift-cards/from-gan"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RetrieveGiftCardFromGanrequest | RetrieveGiftCardFromGanrequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveGiftCardFromGanresponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_gift_card_from_nonce(
        self,
        body: RetrieveGiftCardFromNonceRequest | RetrieveGiftCardFromNonceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveGiftCardFromNonceResponse, RawError]:
        """Retrieves a gift card using a secure payment token that represents the gift card.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/gift-cards/from-nonce"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RetrieveGiftCardFromNonceRequest | RetrieveGiftCardFromNonceRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveGiftCardFromNonceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def unlink_customer_from_gift_card(
        self,
        gift_card_id: str,
        body: UnlinkCustomerFromGiftCardRequest | UnlinkCustomerFromGiftCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UnlinkCustomerFromGiftCardResponse, RawError]:
        """Unlinks a customer from a gift card, which is also referred to as removing a card on file.

        Args:
            gift_card_id: The ID of the gift card to be unlinked.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/gift-cards/{gift_card_id}/unlink-customer"),
            path_params=[param[str]("gift_card_id", gift_card_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UnlinkCustomerFromGiftCardRequest | UnlinkCustomerFromGiftCardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[UnlinkCustomerFromGiftCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
