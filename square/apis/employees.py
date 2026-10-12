from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.enums.employee_status import EmployeeStatusOrStr
from ..models.list_employees_response import ListEmployeesResponse
from ..models.retrieve_employee_response import RetrieveEmployeeResponse
from ..server.server import Server


class Employees:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EmployeesWithRawResponse(client, server, auth)

    def list_employees(
        self,
        *,
        location_id: str | None = None,
        status: EmployeeStatusOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEmployeesResponse:
        """Send a ``GET`` request.

        Args:
            location_id: Value sent with the request.
            status: Specifies the EmployeeStatus to filter the employee by.
            limit: The number of employees to be returned on each page.
            cursor: The token required to retrieve the specified page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_employees(
                location_id=location_id, status=status, limit=limit, cursor=cursor, request_options=request_options
            ),
        )

    def retrieve_employee(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveEmployeeResponse:
        """Send a ``GET`` request.

        Args:
            id_: UUID for the employee that was requested.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_employee(id_, request_options=request_options))

    @property
    def with_raw_response(self) -> EmployeesWithRawResponse:
        return self._with_raw_response


class AsyncEmployees:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEmployeesWithRawResponse(client, server, auth)

    async def list_employees(
        self,
        *,
        location_id: str | None = None,
        status: EmployeeStatusOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEmployeesResponse:
        """Send a ``GET`` request.

        Args:
            location_id: Value sent with the request.
            status: Specifies the EmployeeStatus to filter the employee by.
            limit: The number of employees to be returned on each page.
            cursor: The token required to retrieve the specified page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_employees(
                location_id=location_id, status=status, limit=limit, cursor=cursor, request_options=request_options
            ),
        )

    async def retrieve_employee(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveEmployeeResponse:
        """Send a ``GET`` request.

        Args:
            id_: UUID for the employee that was requested.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.retrieve_employee(id_, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncEmployeesWithRawResponse:
        return self._with_raw_response


class EmployeesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_employees(
        self,
        *,
        location_id: str | None = None,
        status: EmployeeStatusOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEmployeesResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            location_id: Value sent with the request.
            status: Specifies the EmployeeStatus to filter the employee by.
            limit: The number of employees to be returned on each page.
            cursor: The token required to retrieve the specified page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/employees"),
            query_params=[
                param[str | None]("location_id", location_id),
                param[EmployeeStatusOrStr | None]("status", status),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListEmployeesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_employee(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveEmployeeResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            id_: UUID for the employee that was requested.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/employees/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveEmployeeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncEmployeesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_employees(
        self,
        *,
        location_id: str | None = None,
        status: EmployeeStatusOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEmployeesResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            location_id: Value sent with the request.
            status: Specifies the EmployeeStatus to filter the employee by.
            limit: The number of employees to be returned on each page.
            cursor: The token required to retrieve the specified page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/employees"),
            query_params=[
                param[str | None]("location_id", location_id),
                param[EmployeeStatusOrStr | None]("status", status),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListEmployeesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_employee(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveEmployeeResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            id_: UUID for the employee that was requested.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/employees/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveEmployeeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
