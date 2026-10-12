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
from ..models.bulk_create_vendors_request import BulkCreateVendorsRequest, BulkCreateVendorsRequestDict
from ..models.bulk_create_vendors_response import BulkCreateVendorsResponse
from ..models.bulk_retrieve_vendors_request import BulkRetrieveVendorsRequest, BulkRetrieveVendorsRequestDict
from ..models.bulk_retrieve_vendors_response import BulkRetrieveVendorsResponse
from ..models.bulk_update_vendors_request import BulkUpdateVendorsRequest, BulkUpdateVendorsRequestDict
from ..models.bulk_update_vendors_response import BulkUpdateVendorsResponse
from ..models.create_vendor_request import CreateVendorRequest, CreateVendorRequestDict
from ..models.create_vendor_response import CreateVendorResponse
from ..models.retrieve_vendor_response import RetrieveVendorResponse
from ..models.search_vendors_request import SearchVendorsRequest, SearchVendorsRequestDict
from ..models.search_vendors_response import SearchVendorsResponse
from ..models.update_vendor_request import UpdateVendorRequest, UpdateVendorRequestDict
from ..models.update_vendor_response import UpdateVendorResponse
from ..server.server import Server


class Vendors:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VendorsWithRawResponse(client, server, auth)

    def bulk_create_vendors(
        self,
        body: BulkCreateVendorsRequest | BulkCreateVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkCreateVendorsResponse:
        """Creates one or more `Vendor <entity:Vendor>`__ objects to represent suppliers to a seller.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.bulk_create_vendors(body, request_options=request_options))

    def bulk_retrieve_vendors(
        self,
        body: BulkRetrieveVendorsRequest | BulkRetrieveVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkRetrieveVendorsResponse:
        """Retrieves one or more vendors of specified `Vendor <entity:Vendor>`__ IDs.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.bulk_retrieve_vendors(body, request_options=request_options))

    def bulk_update_vendors(
        self,
        body: BulkUpdateVendorsRequest | BulkUpdateVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpdateVendorsResponse:
        """Updates one or more of existing `Vendor <entity:Vendor>`__ objects as suppliers to a seller.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.bulk_update_vendors(body, request_options=request_options))

    def create_vendor(
        self,
        body: CreateVendorRequest | CreateVendorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateVendorResponse:
        """Creates a single `Vendor <entity:Vendor>`__ object to represent a supplier to a seller.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_vendor(body, request_options=request_options))

    def retrieve_vendor(
        self, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveVendorResponse:
        """Retrieves the vendor of a specified `Vendor <entity:Vendor>`__ ID.

        Args:
            vendor_id: ID of the `Vendor <entity:Vendor>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_vendor(vendor_id, request_options=request_options))

    def search_vendors(
        self,
        body: SearchVendorsRequest | SearchVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchVendorsResponse:
        """Searches for vendors using a filter against supported `Vendor <entity:Vendor>`__ properties and a supported
        sorter.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.search_vendors(body, request_options=request_options))

    def update_vendor(
        self,
        vendor_id: str,
        body: UpdateVendorRequest | UpdateVendorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateVendorResponse:
        """Updates an existing `Vendor <entity:Vendor>`__ object as a supplier to a seller.

        Args:
            vendor_id: Value sent with the request.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.update_vendor(vendor_id, body, request_options=request_options))

    @property
    def with_raw_response(self) -> VendorsWithRawResponse:
        return self._with_raw_response


class AsyncVendors:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVendorsWithRawResponse(client, server, auth)

    async def bulk_create_vendors(
        self,
        body: BulkCreateVendorsRequest | BulkCreateVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkCreateVendorsResponse:
        """Creates one or more `Vendor <entity:Vendor>`__ objects to represent suppliers to a seller.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.bulk_create_vendors(body, request_options=request_options))

    async def bulk_retrieve_vendors(
        self,
        body: BulkRetrieveVendorsRequest | BulkRetrieveVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkRetrieveVendorsResponse:
        """Retrieves one or more vendors of specified `Vendor <entity:Vendor>`__ IDs.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.bulk_retrieve_vendors(body, request_options=request_options))

    async def bulk_update_vendors(
        self,
        body: BulkUpdateVendorsRequest | BulkUpdateVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpdateVendorsResponse:
        """Updates one or more of existing `Vendor <entity:Vendor>`__ objects as suppliers to a seller.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.bulk_update_vendors(body, request_options=request_options))

    async def create_vendor(
        self,
        body: CreateVendorRequest | CreateVendorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateVendorResponse:
        """Creates a single `Vendor <entity:Vendor>`__ object to represent a supplier to a seller.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_vendor(body, request_options=request_options))

    async def retrieve_vendor(
        self, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveVendorResponse:
        """Retrieves the vendor of a specified `Vendor <entity:Vendor>`__ ID.

        Args:
            vendor_id: ID of the `Vendor <entity:Vendor>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.retrieve_vendor(vendor_id, request_options=request_options))

    async def search_vendors(
        self,
        body: SearchVendorsRequest | SearchVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchVendorsResponse:
        """Searches for vendors using a filter against supported `Vendor <entity:Vendor>`__ properties and a supported
        sorter.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.search_vendors(body, request_options=request_options))

    async def update_vendor(
        self,
        vendor_id: str,
        body: UpdateVendorRequest | UpdateVendorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateVendorResponse:
        """Updates an existing `Vendor <entity:Vendor>`__ object as a supplier to a seller.

        Args:
            vendor_id: Value sent with the request.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.update_vendor(vendor_id, body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncVendorsWithRawResponse:
        return self._with_raw_response


class VendorsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bulk_create_vendors(
        self,
        body: BulkCreateVendorsRequest | BulkCreateVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkCreateVendorsResponse, RawError]:
        """Creates one or more `Vendor <entity:Vendor>`__ objects to represent suppliers to a seller.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/vendors/bulk-create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkCreateVendorsRequest | BulkCreateVendorsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkCreateVendorsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bulk_retrieve_vendors(
        self,
        body: BulkRetrieveVendorsRequest | BulkRetrieveVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkRetrieveVendorsResponse, RawError]:
        """Retrieves one or more vendors of specified `Vendor <entity:Vendor>`__ IDs.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/vendors/bulk-retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkRetrieveVendorsRequest | BulkRetrieveVendorsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkRetrieveVendorsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bulk_update_vendors(
        self,
        body: BulkUpdateVendorsRequest | BulkUpdateVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpdateVendorsResponse, RawError]:
        """Updates one or more of existing `Vendor <entity:Vendor>`__ objects as suppliers to a seller.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/vendors/bulk-update"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkUpdateVendorsRequest | BulkUpdateVendorsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkUpdateVendorsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_vendor(
        self,
        body: CreateVendorRequest | CreateVendorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateVendorResponse, RawError]:
        """Creates a single `Vendor <entity:Vendor>`__ object to represent a supplier to a seller.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/vendors/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateVendorRequest | CreateVendorRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateVendorResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_vendor(
        self, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveVendorResponse, RawError]:
        """Retrieves the vendor of a specified `Vendor <entity:Vendor>`__ ID.

        Args:
            vendor_id: ID of the `Vendor <entity:Vendor>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/vendors/{vendor_id}"),
            path_params=[param[str]("vendor_id", vendor_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveVendorResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_vendors(
        self,
        body: SearchVendorsRequest | SearchVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchVendorsResponse, RawError]:
        """Searches for vendors using a filter against supported `Vendor <entity:Vendor>`__ properties and a supported
        sorter.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/vendors/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchVendorsRequest | SearchVendorsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchVendorsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_vendor(
        self,
        vendor_id: str,
        body: UpdateVendorRequest | UpdateVendorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateVendorResponse, RawError]:
        """Updates an existing `Vendor <entity:Vendor>`__ object as a supplier to a seller.

        Args:
            vendor_id: Value sent with the request.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/vendors/{vendor_id}"),
            path_params=[param[str]("vendor_id", vendor_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateVendorRequest | UpdateVendorRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateVendorResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncVendorsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bulk_create_vendors(
        self,
        body: BulkCreateVendorsRequest | BulkCreateVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkCreateVendorsResponse, RawError]:
        """Creates one or more `Vendor <entity:Vendor>`__ objects to represent suppliers to a seller.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/vendors/bulk-create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkCreateVendorsRequest | BulkCreateVendorsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[BulkCreateVendorsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bulk_retrieve_vendors(
        self,
        body: BulkRetrieveVendorsRequest | BulkRetrieveVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkRetrieveVendorsResponse, RawError]:
        """Retrieves one or more vendors of specified `Vendor <entity:Vendor>`__ IDs.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/vendors/bulk-retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkRetrieveVendorsRequest | BulkRetrieveVendorsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[BulkRetrieveVendorsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bulk_update_vendors(
        self,
        body: BulkUpdateVendorsRequest | BulkUpdateVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpdateVendorsResponse, RawError]:
        """Updates one or more of existing `Vendor <entity:Vendor>`__ objects as suppliers to a seller.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/vendors/bulk-update"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkUpdateVendorsRequest | BulkUpdateVendorsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[BulkUpdateVendorsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_vendor(
        self,
        body: CreateVendorRequest | CreateVendorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateVendorResponse, RawError]:
        """Creates a single `Vendor <entity:Vendor>`__ object to represent a supplier to a seller.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/vendors/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateVendorRequest | CreateVendorRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CreateVendorResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_vendor(
        self, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveVendorResponse, RawError]:
        """Retrieves the vendor of a specified `Vendor <entity:Vendor>`__ ID.

        Args:
            vendor_id: ID of the `Vendor <entity:Vendor>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/vendors/{vendor_id}"),
            path_params=[param[str]("vendor_id", vendor_id)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveVendorResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_vendors(
        self,
        body: SearchVendorsRequest | SearchVendorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchVendorsResponse, RawError]:
        """Searches for vendors using a filter against supported `Vendor <entity:Vendor>`__ properties and a supported
        sorter.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/vendors/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchVendorsRequest | SearchVendorsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[SearchVendorsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_vendor(
        self,
        vendor_id: str,
        body: UpdateVendorRequest | UpdateVendorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateVendorResponse, RawError]:
        """Updates an existing `Vendor <entity:Vendor>`__ object as a supplier to a seller.

        Args:
            vendor_id: Value sent with the request.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/vendors/{vendor_id}"),
            path_params=[param[str]("vendor_id", vendor_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateVendorRequest | UpdateVendorRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[UpdateVendorResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
