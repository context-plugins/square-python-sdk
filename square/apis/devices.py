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
from ..models.create_device_code_request import CreateDeviceCodeRequest, CreateDeviceCodeRequestDict
from ..models.create_device_code_response import CreateDeviceCodeResponse
from ..models.enums.device_code_status import DeviceCodeStatusOrStr
from ..models.enums.product_type import ProductTypeOrStr
from ..models.enums.sort_order import SortOrderOrStr
from ..models.get_device_code_response import GetDeviceCodeResponse
from ..models.get_device_response import GetDeviceResponse
from ..models.list_device_codes_response import ListDeviceCodesResponse
from ..models.list_devices_response import ListDevicesResponse
from ..server.server import Server


class Devices:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DevicesWithRawResponse(client, server, auth)

    def create_device_code(
        self,
        body: CreateDeviceCodeRequest | CreateDeviceCodeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateDeviceCodeResponse:
        """Creates a DeviceCode that can be used to login to a Square Terminal device to enter the connected terminal
        mode.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_device_code(body, request_options=request_options))

    def get_device(self, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetDeviceResponse:
        """Retrieves Device with the associated ``device_id``.

        Args:
            device_id: The unique ID for the desired ``Device``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_device(device_id, request_options=request_options))

    def get_device_code(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetDeviceCodeResponse:
        """Retrieves DeviceCode with the associated ID.

        Args:
            id_: The unique identifier for the device code.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_device_code(id_, request_options=request_options))

    def list_device_codes(
        self,
        *,
        cursor: str | None = None,
        location_id: str | None = None,
        product_type: ProductTypeOrStr | None = None,
        status: DeviceCodeStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDeviceCodesResponse:
        """Lists all DeviceCodes associated with the merchant.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. See `Paginating results
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ for more information.
            location_id: If specified, only returns DeviceCodes of the specified location. Returns DeviceCodes of all
                locations if empty.
            product_type: If specified, only returns DeviceCodes targeting the specified product type. Returns
                DeviceCodes of all product types if empty.
            status: If specified, returns DeviceCodes with the specified statuses. Returns DeviceCodes of status
                ``PAIRED`` and ``UNPAIRED`` if empty.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_device_codes(
                cursor=cursor,
                location_id=location_id,
                product_type=product_type,
                status=status,
                request_options=request_options,
            ),
        )

    def list_devices(
        self,
        *,
        cursor: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        limit: int | None = None,
        location_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDevicesResponse:
        """List devices associated with the merchant. Currently, only Terminal API devices are supported.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. See `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more
                information.
            sort_order: The order in which results are listed. - ``ASC`` - Oldest to newest. - ``DESC`` - Newest to
                oldest (default).
            limit: The number of results to return in a single page.
            location_id: If present, only returns devices at the target location.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_devices(
                cursor=cursor,
                sort_order=sort_order,
                limit=limit,
                location_id=location_id,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> DevicesWithRawResponse:
        return self._with_raw_response


class AsyncDevices:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDevicesWithRawResponse(client, server, auth)

    async def create_device_code(
        self,
        body: CreateDeviceCodeRequest | CreateDeviceCodeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateDeviceCodeResponse:
        """Creates a DeviceCode that can be used to login to a Square Terminal device to enter the connected terminal
        mode.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_device_code(body, request_options=request_options))

    async def get_device(
        self, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetDeviceResponse:
        """Retrieves Device with the associated ``device_id``.

        Args:
            device_id: The unique ID for the desired ``Device``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_device(device_id, request_options=request_options))

    async def get_device_code(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetDeviceCodeResponse:
        """Retrieves DeviceCode with the associated ID.

        Args:
            id_: The unique identifier for the device code.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_device_code(id_, request_options=request_options))

    async def list_device_codes(
        self,
        *,
        cursor: str | None = None,
        location_id: str | None = None,
        product_type: ProductTypeOrStr | None = None,
        status: DeviceCodeStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDeviceCodesResponse:
        """Lists all DeviceCodes associated with the merchant.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. See `Paginating results
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ for more information.
            location_id: If specified, only returns DeviceCodes of the specified location. Returns DeviceCodes of all
                locations if empty.
            product_type: If specified, only returns DeviceCodes targeting the specified product type. Returns
                DeviceCodes of all product types if empty.
            status: If specified, returns DeviceCodes with the specified statuses. Returns DeviceCodes of status
                ``PAIRED`` and ``UNPAIRED`` if empty.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_device_codes(
                cursor=cursor,
                location_id=location_id,
                product_type=product_type,
                status=status,
                request_options=request_options,
            ),
        )

    async def list_devices(
        self,
        *,
        cursor: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        limit: int | None = None,
        location_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDevicesResponse:
        """List devices associated with the merchant. Currently, only Terminal API devices are supported.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. See `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more
                information.
            sort_order: The order in which results are listed. - ``ASC`` - Oldest to newest. - ``DESC`` - Newest to
                oldest (default).
            limit: The number of results to return in a single page.
            location_id: If present, only returns devices at the target location.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_devices(
                cursor=cursor,
                sort_order=sort_order,
                limit=limit,
                location_id=location_id,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncDevicesWithRawResponse:
        return self._with_raw_response


class DevicesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_device_code(
        self,
        body: CreateDeviceCodeRequest | CreateDeviceCodeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateDeviceCodeResponse, RawError]:
        """Creates a DeviceCode that can be used to login to a Square Terminal device to enter the connected terminal
        mode.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/devices/codes"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateDeviceCodeRequest | CreateDeviceCodeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateDeviceCodeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_device(
        self, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetDeviceResponse, RawError]:
        """Retrieves Device with the associated ``device_id``.

        Args:
            device_id: The unique ID for the desired ``Device``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/devices/{device_id}"),
            path_params=[param[str]("device_id", device_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetDeviceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_device_code(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetDeviceCodeResponse, RawError]:
        """Retrieves DeviceCode with the associated ID.

        Args:
            id_: The unique identifier for the device code.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/devices/codes/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetDeviceCodeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_device_codes(
        self,
        *,
        cursor: str | None = None,
        location_id: str | None = None,
        product_type: ProductTypeOrStr | None = None,
        status: DeviceCodeStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDeviceCodesResponse, RawError]:
        """Lists all DeviceCodes associated with the merchant.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. See `Paginating results
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ for more information.
            location_id: If specified, only returns DeviceCodes of the specified location. Returns DeviceCodes of all
                locations if empty.
            product_type: If specified, only returns DeviceCodes targeting the specified product type. Returns
                DeviceCodes of all product types if empty.
            status: If specified, returns DeviceCodes with the specified statuses. Returns DeviceCodes of status
                ``PAIRED`` and ``UNPAIRED`` if empty.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/devices/codes"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[str | None]("location_id", location_id),
                param[ProductTypeOrStr | None]("product_type", product_type),
                param[DeviceCodeStatusOrStr | None]("status", status),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListDeviceCodesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_devices(
        self,
        *,
        cursor: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        limit: int | None = None,
        location_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDevicesResponse, RawError]:
        """List devices associated with the merchant. Currently, only Terminal API devices are supported.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. See `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more
                information.
            sort_order: The order in which results are listed. - ``ASC`` - Oldest to newest. - ``DESC`` - Newest to
                oldest (default).
            limit: The number of results to return in a single page.
            location_id: If present, only returns devices at the target location.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/devices"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[int | None]("limit", limit),
                param[str | None]("location_id", location_id),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListDevicesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncDevicesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_device_code(
        self,
        body: CreateDeviceCodeRequest | CreateDeviceCodeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateDeviceCodeResponse, RawError]:
        """Creates a DeviceCode that can be used to login to a Square Terminal device to enter the connected terminal
        mode.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/devices/codes"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateDeviceCodeRequest | CreateDeviceCodeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CreateDeviceCodeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_device(
        self, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetDeviceResponse, RawError]:
        """Retrieves Device with the associated ``device_id``.

        Args:
            device_id: The unique ID for the desired ``Device``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/devices/{device_id}"),
            path_params=[param[str]("device_id", device_id)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[GetDeviceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_device_code(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetDeviceCodeResponse, RawError]:
        """Retrieves DeviceCode with the associated ID.

        Args:
            id_: The unique identifier for the device code.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/devices/codes/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[GetDeviceCodeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_device_codes(
        self,
        *,
        cursor: str | None = None,
        location_id: str | None = None,
        product_type: ProductTypeOrStr | None = None,
        status: DeviceCodeStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDeviceCodesResponse, RawError]:
        """Lists all DeviceCodes associated with the merchant.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. See `Paginating results
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ for more information.
            location_id: If specified, only returns DeviceCodes of the specified location. Returns DeviceCodes of all
                locations if empty.
            product_type: If specified, only returns DeviceCodes targeting the specified product type. Returns
                DeviceCodes of all product types if empty.
            status: If specified, returns DeviceCodes with the specified statuses. Returns DeviceCodes of status
                ``PAIRED`` and ``UNPAIRED`` if empty.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/devices/codes"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[str | None]("location_id", location_id),
                param[ProductTypeOrStr | None]("product_type", product_type),
                param[DeviceCodeStatusOrStr | None]("status", status),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListDeviceCodesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_devices(
        self,
        *,
        cursor: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        limit: int | None = None,
        location_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDevicesResponse, RawError]:
        """List devices associated with the merchant. Currently, only Terminal API devices are supported.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. See `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more
                information.
            sort_order: The order in which results are listed. - ``ASC`` - Oldest to newest. - ``DESC`` - Newest to
                oldest (default).
            limit: The number of results to return in a single page.
            location_id: If present, only returns devices at the target location.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/devices"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[int | None]("limit", limit),
                param[str | None]("location_id", location_id),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListDevicesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
