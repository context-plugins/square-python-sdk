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
from ..models.create_gift_card_activity_request import CreateGiftCardActivityRequest, CreateGiftCardActivityRequestDict
from ..models.create_gift_card_activity_response import CreateGiftCardActivityResponse
from ..models.list_gift_card_activities_response import ListGiftCardActivitiesResponse
from ..server.server import Server


class GiftCardActivities:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GiftCardActivitiesWithRawResponse(client, server, auth)

    def create_gift_card_activity(
        self,
        body: CreateGiftCardActivityRequest | CreateGiftCardActivityRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateGiftCardActivityResponse:
        """Creates a gift card activity to manage the balance or state of a `gift card <entity:GiftCard>`__. For
        example, create an ``ACTIVATE`` activity to activate a gift card with an initial balance before first use.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_gift_card_activity(body, request_options=request_options).unwrap()

    def list_gift_card_activities(
        self,
        *,
        gift_card_id: str | None = None,
        type_: str | None = None,
        location_id: str | None = None,
        begin_time: str | None = None,
        end_time: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        sort_order: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListGiftCardActivitiesResponse:
        """Lists gift card activities. By default, you get gift card activities for all gift cards in the seller's
        account. You can optionally specify query parameters to filter the list. For example, you can get a list of gift
        card activities for a gift card, for all gift cards in a specific region, or for activities within a time
        window.

        Args:
            gift_card_id: If a gift card ID is provided, the endpoint returns activities related to the specified gift
                card. Otherwise, the endpoint returns all gift card activities for the seller.
            type_: If a `type <entity:GiftCardActivityType>`__ is provided, the endpoint returns gift card activities of
                the specified type. Otherwise, the endpoint returns all types of gift card activities.
            location_id: If a location ID is provided, the endpoint returns gift card activities for the specified
                location. Otherwise, the endpoint returns gift card activities for all locations.
            begin_time: The timestamp for the beginning of the reporting period, in RFC 3339 format. This start time is
                inclusive. The default value is the current time minus one year.
            end_time: The timestamp for the end of the reporting period, in RFC 3339 format. This end time is inclusive.
                The default value is the current time.
            limit: If a limit is provided, the endpoint returns the specified number of results (or fewer) per page. The
                maximum value is 100. The default value is 50. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. If a cursor is not provided, the endpoint returns the
                first page of the results. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            sort_order: The order in which the endpoint returns the activities, based on ``created_at``. - ``ASC`` -
                Oldest to newest. - ``DESC`` - Newest to oldest (default).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_gift_card_activities(
            gift_card_id=gift_card_id,
            type_=type_,
            location_id=location_id,
            begin_time=begin_time,
            end_time=end_time,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> GiftCardActivitiesWithRawResponse:
        return self._with_raw_response


class AsyncGiftCardActivities:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGiftCardActivitiesWithRawResponse(client, server, auth)

    async def create_gift_card_activity(
        self,
        body: CreateGiftCardActivityRequest | CreateGiftCardActivityRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateGiftCardActivityResponse:
        """Creates a gift card activity to manage the balance or state of a `gift card <entity:GiftCard>`__. For
        example, create an ``ACTIVATE`` activity to activate a gift card with an initial balance before first use.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_gift_card_activity(body, request_options=request_options)).unwrap()

    async def list_gift_card_activities(
        self,
        *,
        gift_card_id: str | None = None,
        type_: str | None = None,
        location_id: str | None = None,
        begin_time: str | None = None,
        end_time: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        sort_order: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListGiftCardActivitiesResponse:
        """Lists gift card activities. By default, you get gift card activities for all gift cards in the seller's
        account. You can optionally specify query parameters to filter the list. For example, you can get a list of gift
        card activities for a gift card, for all gift cards in a specific region, or for activities within a time
        window.

        Args:
            gift_card_id: If a gift card ID is provided, the endpoint returns activities related to the specified gift
                card. Otherwise, the endpoint returns all gift card activities for the seller.
            type_: If a `type <entity:GiftCardActivityType>`__ is provided, the endpoint returns gift card activities of
                the specified type. Otherwise, the endpoint returns all types of gift card activities.
            location_id: If a location ID is provided, the endpoint returns gift card activities for the specified
                location. Otherwise, the endpoint returns gift card activities for all locations.
            begin_time: The timestamp for the beginning of the reporting period, in RFC 3339 format. This start time is
                inclusive. The default value is the current time minus one year.
            end_time: The timestamp for the end of the reporting period, in RFC 3339 format. This end time is inclusive.
                The default value is the current time.
            limit: If a limit is provided, the endpoint returns the specified number of results (or fewer) per page. The
                maximum value is 100. The default value is 50. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. If a cursor is not provided, the endpoint returns the
                first page of the results. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            sort_order: The order in which the endpoint returns the activities, based on ``created_at``. - ``ASC`` -
                Oldest to newest. - ``DESC`` - Newest to oldest (default).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_gift_card_activities(
                gift_card_id=gift_card_id,
                type_=type_,
                location_id=location_id,
                begin_time=begin_time,
                end_time=end_time,
                limit=limit,
                cursor=cursor,
                sort_order=sort_order,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncGiftCardActivitiesWithRawResponse:
        return self._with_raw_response


class GiftCardActivitiesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_gift_card_activity(
        self,
        body: CreateGiftCardActivityRequest | CreateGiftCardActivityRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateGiftCardActivityResponse, RawError]:
        """Creates a gift card activity to manage the balance or state of a `gift card <entity:GiftCard>`__. For
        example, create an ``ACTIVATE`` activity to activate a gift card with an initial balance before first use.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/gift-cards/activities"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateGiftCardActivityRequest | CreateGiftCardActivityRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateGiftCardActivityResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_gift_card_activities(
        self,
        *,
        gift_card_id: str | None = None,
        type_: str | None = None,
        location_id: str | None = None,
        begin_time: str | None = None,
        end_time: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        sort_order: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListGiftCardActivitiesResponse, RawError]:
        """Lists gift card activities. By default, you get gift card activities for all gift cards in the seller's
        account. You can optionally specify query parameters to filter the list. For example, you can get a list of gift
        card activities for a gift card, for all gift cards in a specific region, or for activities within a time
        window.

        Args:
            gift_card_id: If a gift card ID is provided, the endpoint returns activities related to the specified gift
                card. Otherwise, the endpoint returns all gift card activities for the seller.
            type_: If a `type <entity:GiftCardActivityType>`__ is provided, the endpoint returns gift card activities of
                the specified type. Otherwise, the endpoint returns all types of gift card activities.
            location_id: If a location ID is provided, the endpoint returns gift card activities for the specified
                location. Otherwise, the endpoint returns gift card activities for all locations.
            begin_time: The timestamp for the beginning of the reporting period, in RFC 3339 format. This start time is
                inclusive. The default value is the current time minus one year.
            end_time: The timestamp for the end of the reporting period, in RFC 3339 format. This end time is inclusive.
                The default value is the current time.
            limit: If a limit is provided, the endpoint returns the specified number of results (or fewer) per page. The
                maximum value is 100. The default value is 50. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. If a cursor is not provided, the endpoint returns the
                first page of the results. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            sort_order: The order in which the endpoint returns the activities, based on ``created_at``. - ``ASC`` -
                Oldest to newest. - ``DESC`` - Newest to oldest (default).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/gift-cards/activities"),
            query_params=[
                param[str | None]("gift_card_id", gift_card_id),
                param[str | None]("type", type_),
                param[str | None]("location_id", location_id),
                param[str | None]("begin_time", begin_time),
                param[str | None]("end_time", end_time),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("sort_order", sort_order),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListGiftCardActivitiesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncGiftCardActivitiesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_gift_card_activity(
        self,
        body: CreateGiftCardActivityRequest | CreateGiftCardActivityRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateGiftCardActivityResponse, RawError]:
        """Creates a gift card activity to manage the balance or state of a `gift card <entity:GiftCard>`__. For
        example, create an ``ACTIVATE`` activity to activate a gift card with an initial balance before first use.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/gift-cards/activities"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateGiftCardActivityRequest | CreateGiftCardActivityRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateGiftCardActivityResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_gift_card_activities(
        self,
        *,
        gift_card_id: str | None = None,
        type_: str | None = None,
        location_id: str | None = None,
        begin_time: str | None = None,
        end_time: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        sort_order: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListGiftCardActivitiesResponse, RawError]:
        """Lists gift card activities. By default, you get gift card activities for all gift cards in the seller's
        account. You can optionally specify query parameters to filter the list. For example, you can get a list of gift
        card activities for a gift card, for all gift cards in a specific region, or for activities within a time
        window.

        Args:
            gift_card_id: If a gift card ID is provided, the endpoint returns activities related to the specified gift
                card. Otherwise, the endpoint returns all gift card activities for the seller.
            type_: If a `type <entity:GiftCardActivityType>`__ is provided, the endpoint returns gift card activities of
                the specified type. Otherwise, the endpoint returns all types of gift card activities.
            location_id: If a location ID is provided, the endpoint returns gift card activities for the specified
                location. Otherwise, the endpoint returns gift card activities for all locations.
            begin_time: The timestamp for the beginning of the reporting period, in RFC 3339 format. This start time is
                inclusive. The default value is the current time minus one year.
            end_time: The timestamp for the end of the reporting period, in RFC 3339 format. This end time is inclusive.
                The default value is the current time.
            limit: If a limit is provided, the endpoint returns the specified number of results (or fewer) per page. The
                maximum value is 100. The default value is 50. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. If a cursor is not provided, the endpoint returns the
                first page of the results. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            sort_order: The order in which the endpoint returns the activities, based on ``created_at``. - ``ASC`` -
                Oldest to newest. - ``DESC`` - Newest to oldest (default).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/gift-cards/activities"),
            query_params=[
                param[str | None]("gift_card_id", gift_card_id),
                param[str | None]("type", type_),
                param[str | None]("location_id", location_id),
                param[str | None]("begin_time", begin_time),
                param[str | None]("end_time", end_time),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("sort_order", sort_order),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListGiftCardActivitiesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
