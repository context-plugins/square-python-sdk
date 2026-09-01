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
from ..models.create_card_request import CreateCardRequest, CreateCardRequestDict
from ..models.create_card_response import CreateCardResponse
from ..models.disable_card_response import DisableCardResponse
from ..models.enums.sort_order import SortOrderOrStr
from ..models.list_cards_response import ListCardsResponse
from ..models.retrieve_card_response import RetrieveCardResponse
from ..server.server import Server


class Cards:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CardsWithRawResponse(client, server, auth)

    def create_card(
        self, body: CreateCardRequest | CreateCardRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> CreateCardResponse:
        """Adds a card on file to an existing merchant.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_card(body, request_options=request_options).unwrap()

    def disable_card(self, card_id: str, *, request_options: RequestOptionsOrDict | None = None) -> DisableCardResponse:
        """Disables the card, preventing any further updates or charges. Disabling an already disabled card is allowed
        but has no effect.

        Args:
            card_id: Unique ID for the desired Card.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.disable_card(card_id, request_options=request_options).unwrap()

    def list_cards(
        self,
        *,
        cursor: str | None = None,
        customer_id: str | None = None,
        include_disabled: bool | None = False,
        reference_id: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCardsResponse:
        """Retrieves a list of cards owned by the account making the request. A max of 25 cards will be returned.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. See `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more
                information.
            customer_id: Limit results to cards associated with the customer supplied. By default, all cards owned by
                the merchant are returned.
            include_disabled: Includes disabled cards. By default, all enabled cards owned by the merchant are returned.
            reference_id: Limit results to cards associated with the reference_id supplied.
            sort_order: Sorts the returned list by when the card was created with the specified order. This field
                defaults to ASC.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_cards(
            cursor=cursor,
            customer_id=customer_id,
            include_disabled=include_disabled,
            reference_id=reference_id,
            sort_order=sort_order,
            request_options=request_options,
        ).unwrap()

    def retrieve_card(
        self, card_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveCardResponse:
        """Retrieves details for a specific Card.

        Args:
            card_id: Unique ID for the desired Card.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_card(card_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CardsWithRawResponse:
        return self._with_raw_response


class AsyncCards:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCardsWithRawResponse(client, server, auth)

    async def create_card(
        self, body: CreateCardRequest | CreateCardRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> CreateCardResponse:
        """Adds a card on file to an existing merchant.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_card(body, request_options=request_options)).unwrap()

    async def disable_card(
        self, card_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DisableCardResponse:
        """Disables the card, preventing any further updates or charges. Disabling an already disabled card is allowed
        but has no effect.

        Args:
            card_id: Unique ID for the desired Card.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.disable_card(card_id, request_options=request_options)).unwrap()

    async def list_cards(
        self,
        *,
        cursor: str | None = None,
        customer_id: str | None = None,
        include_disabled: bool | None = False,
        reference_id: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCardsResponse:
        """Retrieves a list of cards owned by the account making the request. A max of 25 cards will be returned.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. See `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more
                information.
            customer_id: Limit results to cards associated with the customer supplied. By default, all cards owned by
                the merchant are returned.
            include_disabled: Includes disabled cards. By default, all enabled cards owned by the merchant are returned.
            reference_id: Limit results to cards associated with the reference_id supplied.
            sort_order: Sorts the returned list by when the card was created with the specified order. This field
                defaults to ASC.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_cards(
                cursor=cursor,
                customer_id=customer_id,
                include_disabled=include_disabled,
                reference_id=reference_id,
                sort_order=sort_order,
                request_options=request_options,
            )
        ).unwrap()

    async def retrieve_card(
        self, card_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveCardResponse:
        """Retrieves details for a specific Card.

        Args:
            card_id: Unique ID for the desired Card.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.retrieve_card(card_id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncCardsWithRawResponse:
        return self._with_raw_response


class CardsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_card(
        self, body: CreateCardRequest | CreateCardRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CreateCardResponse, RawError]:
        """Adds a card on file to an existing merchant.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/cards"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCardRequest | CreateCardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def disable_card(
        self, card_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DisableCardResponse, RawError]:
        """Disables the card, preventing any further updates or charges. Disabling an already disabled card is allowed
        but has no effect.

        Args:
            card_id: Unique ID for the desired Card.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/cards/{card_id}/disable"),
            path_params=[param[str]("card_id", card_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DisableCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_cards(
        self,
        *,
        cursor: str | None = None,
        customer_id: str | None = None,
        include_disabled: bool | None = False,
        reference_id: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCardsResponse, RawError]:
        """Retrieves a list of cards owned by the account making the request. A max of 25 cards will be returned.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. See `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more
                information.
            customer_id: Limit results to cards associated with the customer supplied. By default, all cards owned by
                the merchant are returned.
            include_disabled: Includes disabled cards. By default, all enabled cards owned by the merchant are returned.
            reference_id: Limit results to cards associated with the reference_id supplied.
            sort_order: Sorts the returned list by when the card was created with the specified order. This field
                defaults to ASC.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cards"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[str | None]("customer_id", customer_id),
                param[bool | None]("include_disabled", include_disabled),
                param[str | None]("reference_id", reference_id),
                param[SortOrderOrStr | None]("sort_order", sort_order),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCardsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_card(
        self, card_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveCardResponse, RawError]:
        """Retrieves details for a specific Card.

        Args:
            card_id: Unique ID for the desired Card.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cards/{card_id}"),
            path_params=[param[str]("card_id", card_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCardsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_card(
        self, body: CreateCardRequest | CreateCardRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CreateCardResponse, RawError]:
        """Adds a card on file to an existing merchant.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/cards"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCardRequest | CreateCardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def disable_card(
        self, card_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DisableCardResponse, RawError]:
        """Disables the card, preventing any further updates or charges. Disabling an already disabled card is allowed
        but has no effect.

        Args:
            card_id: Unique ID for the desired Card.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/cards/{card_id}/disable"),
            path_params=[param[str]("card_id", card_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DisableCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_cards(
        self,
        *,
        cursor: str | None = None,
        customer_id: str | None = None,
        include_disabled: bool | None = False,
        reference_id: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCardsResponse, RawError]:
        """Retrieves a list of cards owned by the account making the request. A max of 25 cards will be returned.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. See `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more
                information.
            customer_id: Limit results to cards associated with the customer supplied. By default, all cards owned by
                the merchant are returned.
            include_disabled: Includes disabled cards. By default, all enabled cards owned by the merchant are returned.
            reference_id: Limit results to cards associated with the reference_id supplied.
            sort_order: Sorts the returned list by when the card was created with the specified order. This field
                defaults to ASC.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cards"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[str | None]("customer_id", customer_id),
                param[bool | None]("include_disabled", include_disabled),
                param[str | None]("reference_id", reference_id),
                param[SortOrderOrStr | None]("sort_order", sort_order),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCardsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_card(
        self, card_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveCardResponse, RawError]:
        """Retrieves details for a specific Card.

        Args:
            card_id: Unique ID for the desired Card.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cards/{card_id}"),
            path_params=[param[str]("card_id", card_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
