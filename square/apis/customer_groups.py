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
from ..models.create_customer_group_request import CreateCustomerGroupRequest, CreateCustomerGroupRequestDict
from ..models.create_customer_group_response import CreateCustomerGroupResponse
from ..models.delete_customer_group_response import DeleteCustomerGroupResponse
from ..models.list_customer_groups_response import ListCustomerGroupsResponse
from ..models.retrieve_customer_group_response import RetrieveCustomerGroupResponse
from ..models.update_customer_group_request import UpdateCustomerGroupRequest, UpdateCustomerGroupRequestDict
from ..models.update_customer_group_response import UpdateCustomerGroupResponse
from ..server.server import Server


class CustomerGroups:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CustomerGroupsWithRawResponse(client, server, auth)

    def create_customer_group(
        self,
        body: CreateCustomerGroupRequest | CreateCustomerGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCustomerGroupResponse:
        """Creates a new customer group for a business.

        The request must include the ``name`` value of the group.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_customer_group(body, request_options=request_options).unwrap()

    def delete_customer_group(
        self, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteCustomerGroupResponse:
        """Deletes a customer group as identified by the ``group_id`` value.

        Args:
            group_id: The ID of the customer group to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_customer_group(group_id, request_options=request_options).unwrap()

    def list_customer_groups(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomerGroupsResponse:
        """Retrieves the list of customer groups of a business.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single page. This limit is advisory. The response might
                contain more or fewer results. If the limit is less than 1 or greater than 50, Square returns a ``400
                VALUE_TOO_LOW`` or ``400 VALUE_TOO_HIGH`` error. The default value is 50. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_customer_groups(
            cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def retrieve_customer_group(
        self, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveCustomerGroupResponse:
        """Retrieves a specific customer group as identified by the ``group_id`` value.

        Args:
            group_id: The ID of the customer group to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_customer_group(group_id, request_options=request_options).unwrap()

    def update_customer_group(
        self,
        group_id: str,
        body: UpdateCustomerGroupRequest | UpdateCustomerGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateCustomerGroupResponse:
        """Updates a customer group as identified by the ``group_id`` value.

        Args:
            group_id: The ID of the customer group to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_customer_group(group_id, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CustomerGroupsWithRawResponse:
        return self._with_raw_response


class AsyncCustomerGroups:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCustomerGroupsWithRawResponse(client, server, auth)

    async def create_customer_group(
        self,
        body: CreateCustomerGroupRequest | CreateCustomerGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCustomerGroupResponse:
        """Creates a new customer group for a business.

        The request must include the ``name`` value of the group.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_customer_group(body, request_options=request_options)).unwrap()

    async def delete_customer_group(
        self, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteCustomerGroupResponse:
        """Deletes a customer group as identified by the ``group_id`` value.

        Args:
            group_id: The ID of the customer group to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_customer_group(group_id, request_options=request_options)).unwrap()

    async def list_customer_groups(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomerGroupsResponse:
        """Retrieves the list of customer groups of a business.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single page. This limit is advisory. The response might
                contain more or fewer results. If the limit is less than 1 or greater than 50, Square returns a ``400
                VALUE_TOO_LOW`` or ``400 VALUE_TOO_HIGH`` error. The default value is 50. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_customer_groups(
                cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def retrieve_customer_group(
        self, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveCustomerGroupResponse:
        """Retrieves a specific customer group as identified by the ``group_id`` value.

        Args:
            group_id: The ID of the customer group to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_customer_group(group_id, request_options=request_options)
        ).unwrap()

    async def update_customer_group(
        self,
        group_id: str,
        body: UpdateCustomerGroupRequest | UpdateCustomerGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateCustomerGroupResponse:
        """Updates a customer group as identified by the ``group_id`` value.

        Args:
            group_id: The ID of the customer group to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_customer_group(group_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCustomerGroupsWithRawResponse:
        return self._with_raw_response


class CustomerGroupsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_customer_group(
        self,
        body: CreateCustomerGroupRequest | CreateCustomerGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCustomerGroupResponse, RawError]:
        """Creates a new customer group for a business.

        The request must include the ``name`` value of the group.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/groups"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCustomerGroupRequest | CreateCustomerGroupRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateCustomerGroupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_customer_group(
        self, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteCustomerGroupResponse, RawError]:
        """Deletes a customer group as identified by the ``group_id`` value.

        Args:
            group_id: The ID of the customer group to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/customers/groups/{group_id}"),
            path_params=[param[str]("group_id", group_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteCustomerGroupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_customer_groups(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomerGroupsResponse, RawError]:
        """Retrieves the list of customer groups of a business.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single page. This limit is advisory. The response might
                contain more or fewer results. If the limit is less than 1 or greater than 50, Square returns a ``400
                VALUE_TOO_LOW`` or ``400 VALUE_TOO_HIGH`` error. The default value is 50. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/customers/groups"),
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCustomerGroupsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_customer_group(
        self, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveCustomerGroupResponse, RawError]:
        """Retrieves a specific customer group as identified by the ``group_id`` value.

        Args:
            group_id: The ID of the customer group to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/customers/groups/{group_id}"),
            path_params=[param[str]("group_id", group_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveCustomerGroupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_customer_group(
        self,
        group_id: str,
        body: UpdateCustomerGroupRequest | UpdateCustomerGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateCustomerGroupResponse, RawError]:
        """Updates a customer group as identified by the ``group_id`` value.

        Args:
            group_id: The ID of the customer group to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/customers/groups/{group_id}"),
            path_params=[param[str]("group_id", group_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCustomerGroupRequest | UpdateCustomerGroupRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateCustomerGroupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCustomerGroupsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_customer_group(
        self,
        body: CreateCustomerGroupRequest | CreateCustomerGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCustomerGroupResponse, RawError]:
        """Creates a new customer group for a business.

        The request must include the ``name`` value of the group.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/groups"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCustomerGroupRequest | CreateCustomerGroupRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateCustomerGroupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_customer_group(
        self, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteCustomerGroupResponse, RawError]:
        """Deletes a customer group as identified by the ``group_id`` value.

        Args:
            group_id: The ID of the customer group to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/customers/groups/{group_id}"),
            path_params=[param[str]("group_id", group_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteCustomerGroupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_customer_groups(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomerGroupsResponse, RawError]:
        """Retrieves the list of customer groups of a business.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single page. This limit is advisory. The response might
                contain more or fewer results. If the limit is less than 1 or greater than 50, Square returns a ``400
                VALUE_TOO_LOW`` or ``400 VALUE_TOO_HIGH`` error. The default value is 50. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/customers/groups"),
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCustomerGroupsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_customer_group(
        self, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveCustomerGroupResponse, RawError]:
        """Retrieves a specific customer group as identified by the ``group_id`` value.

        Args:
            group_id: The ID of the customer group to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/customers/groups/{group_id}"),
            path_params=[param[str]("group_id", group_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveCustomerGroupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_customer_group(
        self,
        group_id: str,
        body: UpdateCustomerGroupRequest | UpdateCustomerGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateCustomerGroupResponse, RawError]:
        """Updates a customer group as identified by the ``group_id`` value.

        Args:
            group_id: The ID of the customer group to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/customers/groups/{group_id}"),
            path_params=[param[str]("group_id", group_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCustomerGroupRequest | UpdateCustomerGroupRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateCustomerGroupResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
