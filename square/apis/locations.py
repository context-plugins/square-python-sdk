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
from ..models.create_location_request import CreateLocationRequest, CreateLocationRequestDict
from ..models.create_location_response import CreateLocationResponse
from ..models.list_locations_response import ListLocationsResponse
from ..models.retrieve_location_response import RetrieveLocationResponse
from ..models.update_location_request import UpdateLocationRequest, UpdateLocationRequestDict
from ..models.update_location_response import UpdateLocationResponse
from ..server.server import Server


class Locations:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LocationsWithRawResponse(client, server, auth)

    def create_location(
        self,
        body: CreateLocationRequest | CreateLocationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateLocationResponse:
        """Creates a `location <https://developer.squareup.com/docs/locations-api>`__. Creating new locations allows for
        separate configuration of receipt layouts, item prices, and sales reports. Developers can use locations to
        separate sales activity through applications that integrate with Square from sales activity elsewhere in a
        seller's account. Locations created programmatically with the Locations API last forever and are visible to the
        seller for their own management. Therefore, ensure that each location has a sensible and unique name.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_location(body, request_options=request_options))

    def list_locations(self, *, request_options: RequestOptionsOrDict | None = None) -> ListLocationsResponse:
        """Provides details about all of the seller's `locations <https://developer.squareup.com/docs/locations-api>`__,
        including those with an inactive status. Locations are listed alphabetically by ``name``.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.list_locations(request_options=request_options))

    def retrieve_location(
        self, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLocationResponse:
        """Retrieves details of a single location. Specify "main" as the location ID to retrieve details of the `main
        location <https://developer.squareup.com/docs/locations-api#about-the-main-location>`__.

        Args:
            location_id: The ID of the location to retrieve. Specify the string "main" to return the main location.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_location(location_id, request_options=request_options))

    def update_location(
        self,
        location_id: str,
        body: UpdateLocationRequest | UpdateLocationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateLocationResponse:
        """Updates a `location <https://developer.squareup.com/docs/locations-api>`__.

        Args:
            location_id: The ID of the location to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.update_location(location_id, body, request_options=request_options))

    @property
    def with_raw_response(self) -> LocationsWithRawResponse:
        return self._with_raw_response


class AsyncLocations:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLocationsWithRawResponse(client, server, auth)

    async def create_location(
        self,
        body: CreateLocationRequest | CreateLocationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateLocationResponse:
        """Creates a `location <https://developer.squareup.com/docs/locations-api>`__. Creating new locations allows for
        separate configuration of receipt layouts, item prices, and sales reports. Developers can use locations to
        separate sales activity through applications that integrate with Square from sales activity elsewhere in a
        seller's account. Locations created programmatically with the Locations API last forever and are visible to the
        seller for their own management. Therefore, ensure that each location has a sensible and unique name.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_location(body, request_options=request_options))

    async def list_locations(self, *, request_options: RequestOptionsOrDict | None = None) -> ListLocationsResponse:
        """Provides details about all of the seller's `locations <https://developer.squareup.com/docs/locations-api>`__,
        including those with an inactive status. Locations are listed alphabetically by ``name``.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.list_locations(request_options=request_options))

    async def retrieve_location(
        self, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLocationResponse:
        """Retrieves details of a single location. Specify "main" as the location ID to retrieve details of the `main
        location <https://developer.squareup.com/docs/locations-api#about-the-main-location>`__.

        Args:
            location_id: The ID of the location to retrieve. Specify the string "main" to return the main location.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.retrieve_location(location_id, request_options=request_options))

    async def update_location(
        self,
        location_id: str,
        body: UpdateLocationRequest | UpdateLocationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateLocationResponse:
        """Updates a `location <https://developer.squareup.com/docs/locations-api>`__.

        Args:
            location_id: The ID of the location to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.update_location(location_id, body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncLocationsWithRawResponse:
        return self._with_raw_response


class LocationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_location(
        self,
        body: CreateLocationRequest | CreateLocationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateLocationResponse, RawError]:
        """Creates a `location <https://developer.squareup.com/docs/locations-api>`__. Creating new locations allows for
        separate configuration of receipt layouts, item prices, and sales reports. Developers can use locations to
        separate sales activity through applications that integrate with Square from sales activity elsewhere in a
        seller's account. Locations created programmatically with the Locations API last forever and are visible to the
        seller for their own management. Therefore, ensure that each location has a sensible and unique name.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateLocationRequest | CreateLocationRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateLocationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_locations(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListLocationsResponse, RawError]:
        """Provides details about all of the seller's `locations <https://developer.squareup.com/docs/locations-api>`__,
        including those with an inactive status. Locations are listed alphabetically by ``name``.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations"),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListLocationsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_location(
        self, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLocationResponse, RawError]:
        """Retrieves details of a single location. Specify "main" as the location ID to retrieve details of the `main
        location <https://developer.squareup.com/docs/locations-api#about-the-main-location>`__.

        Args:
            location_id: The ID of the location to retrieve. Specify the string "main" to return the main location.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations/{location_id}"),
            path_params=[param[str]("location_id", location_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveLocationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_location(
        self,
        location_id: str,
        body: UpdateLocationRequest | UpdateLocationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateLocationResponse, RawError]:
        """Updates a `location <https://developer.squareup.com/docs/locations-api>`__.

        Args:
            location_id: The ID of the location to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/locations/{location_id}"),
            path_params=[param[str]("location_id", location_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateLocationRequest | UpdateLocationRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateLocationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncLocationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_location(
        self,
        body: CreateLocationRequest | CreateLocationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateLocationResponse, RawError]:
        """Creates a `location <https://developer.squareup.com/docs/locations-api>`__. Creating new locations allows for
        separate configuration of receipt layouts, item prices, and sales reports. Developers can use locations to
        separate sales activity through applications that integrate with Square from sales activity elsewhere in a
        seller's account. Locations created programmatically with the Locations API last forever and are visible to the
        seller for their own management. Therefore, ensure that each location has a sensible and unique name.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateLocationRequest | CreateLocationRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CreateLocationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_locations(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListLocationsResponse, RawError]:
        """Provides details about all of the seller's `locations <https://developer.squareup.com/docs/locations-api>`__,
        including those with an inactive status. Locations are listed alphabetically by ``name``.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations"),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListLocationsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_location(
        self, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLocationResponse, RawError]:
        """Retrieves details of a single location. Specify "main" as the location ID to retrieve details of the `main
        location <https://developer.squareup.com/docs/locations-api#about-the-main-location>`__.

        Args:
            location_id: The ID of the location to retrieve. Specify the string "main" to return the main location.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations/{location_id}"),
            path_params=[param[str]("location_id", location_id)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveLocationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_location(
        self,
        location_id: str,
        body: UpdateLocationRequest | UpdateLocationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateLocationResponse, RawError]:
        """Updates a `location <https://developer.squareup.com/docs/locations-api>`__.

        Args:
            location_id: The ID of the location to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/locations/{location_id}"),
            path_params=[param[str]("location_id", location_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateLocationRequest | UpdateLocationRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[UpdateLocationResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
