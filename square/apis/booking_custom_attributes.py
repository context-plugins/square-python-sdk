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
from ..models.bulk_delete_booking_custom_attributes_request import (
    BulkDeleteBookingCustomAttributesRequest,
    BulkDeleteBookingCustomAttributesRequestDict,
)
from ..models.bulk_delete_booking_custom_attributes_response import BulkDeleteBookingCustomAttributesResponse
from ..models.bulk_upsert_booking_custom_attributes_request import (
    BulkUpsertBookingCustomAttributesRequest,
    BulkUpsertBookingCustomAttributesRequestDict,
)
from ..models.bulk_upsert_booking_custom_attributes_response import BulkUpsertBookingCustomAttributesResponse
from ..models.create_booking_custom_attribute_definition_request import (
    CreateBookingCustomAttributeDefinitionRequest,
    CreateBookingCustomAttributeDefinitionRequestDict,
)
from ..models.create_booking_custom_attribute_definition_response import CreateBookingCustomAttributeDefinitionResponse
from ..models.delete_booking_custom_attribute_definition_response import DeleteBookingCustomAttributeDefinitionResponse
from ..models.delete_booking_custom_attribute_response import DeleteBookingCustomAttributeResponse
from ..models.list_booking_custom_attribute_definitions_response import ListBookingCustomAttributeDefinitionsResponse
from ..models.list_booking_custom_attributes_response import ListBookingCustomAttributesResponse
from ..models.retrieve_booking_custom_attribute_definition_response import (
    RetrieveBookingCustomAttributeDefinitionResponse,
)
from ..models.retrieve_booking_custom_attribute_response import RetrieveBookingCustomAttributeResponse
from ..models.update_booking_custom_attribute_definition_request import (
    UpdateBookingCustomAttributeDefinitionRequest,
    UpdateBookingCustomAttributeDefinitionRequestDict,
)
from ..models.update_booking_custom_attribute_definition_response import UpdateBookingCustomAttributeDefinitionResponse
from ..models.upsert_booking_custom_attribute_request import (
    UpsertBookingCustomAttributeRequest,
    UpsertBookingCustomAttributeRequestDict,
)
from ..models.upsert_booking_custom_attribute_response import UpsertBookingCustomAttributeResponse
from ..server.server import Server


class BookingCustomAttributes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BookingCustomAttributesWithRawResponse(client, server, auth)

    def bulk_delete_booking_custom_attributes(
        self,
        body: BulkDeleteBookingCustomAttributesRequest | BulkDeleteBookingCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkDeleteBookingCustomAttributesResponse:
        """Bulk deletes bookings custom attributes.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_delete_booking_custom_attributes(
            body, request_options=request_options
        ).unwrap()

    def bulk_upsert_booking_custom_attributes(
        self,
        body: BulkUpsertBookingCustomAttributesRequest | BulkUpsertBookingCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpsertBookingCustomAttributesResponse:
        """Bulk upserts bookings custom attributes.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_upsert_booking_custom_attributes(
            body, request_options=request_options
        ).unwrap()

    def create_booking_custom_attribute_definition(
        self,
        body: CreateBookingCustomAttributeDefinitionRequest | CreateBookingCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateBookingCustomAttributeDefinitionResponse:
        """Creates a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_booking_custom_attribute_definition(
            body, request_options=request_options
        ).unwrap()

    def delete_booking_custom_attribute(
        self, booking_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteBookingCustomAttributeResponse:
        """Deletes a bookings custom attribute.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_booking_custom_attribute(
            booking_id, key, request_options=request_options
        ).unwrap()

    def delete_booking_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteBookingCustomAttributeDefinitionResponse:
        """Deletes a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_booking_custom_attribute_definition(
            key, request_options=request_options
        ).unwrap()

    def list_booking_custom_attribute_definitions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBookingCustomAttributeDefinitionsResponse:
        """Get all bookings custom attribute definitions.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_booking_custom_attribute_definitions(
            limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    def list_booking_custom_attributes(
        self,
        booking_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBookingCustomAttributesResponse:
        """Lists a booking's custom attributes.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            with_definitions: Indicates whether to return the `custom attribute definition
                <entity:CustomAttributeDefinition>`__ in the ``definition`` field of each custom attribute. Set this
                parameter to ``true`` to get the name and description of each custom attribute, information about the
                data type, or other definition details. The default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_booking_custom_attributes(
            booking_id, limit=limit, cursor=cursor, with_definitions=with_definitions, request_options=request_options
        ).unwrap()

    def retrieve_booking_custom_attribute(
        self,
        booking_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveBookingCustomAttributeResponse:
        """Retrieves a bookings custom attribute.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            key: The key of the custom attribute to retrieve. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            with_definition: Indicates whether to return the `custom attribute definition
                <entity:CustomAttributeDefinition>`__ in the ``definition`` field of the custom attribute. Set this
                parameter to ``true`` to get the name and description of the custom attribute, information about the
                data type, or other definition details. The default value is ``false``.
            version: The current version of the custom attribute, which is used for strongly consistent reads to
                guarantee that you receive the most up-to-date data. When included in the request, Square returns the
                specified version or a higher version if one exists. If the specified version is higher than the current
                version, Square returns a ``BAD_REQUEST`` error.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_booking_custom_attribute(
            booking_id, key, with_definition=with_definition, version=version, request_options=request_options
        ).unwrap()

    def retrieve_booking_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveBookingCustomAttributeDefinitionResponse:
        """Retrieves a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            key: The key of the custom attribute definition to retrieve. If the requesting application is not the
                definition owner, you must use the qualified key.
            version: The current version of the custom attribute definition, which is used for strongly consistent reads
                to guarantee that you receive the most up-to-date data. When included in the request, Square returns the
                specified version or a higher version if one exists. If the specified version is higher than the current
                version, Square returns a ``BAD_REQUEST`` error.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_booking_custom_attribute_definition(
            key, version=version, request_options=request_options
        ).unwrap()

    def update_booking_custom_attribute_definition(
        self,
        key: str,
        body: UpdateBookingCustomAttributeDefinitionRequest | UpdateBookingCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateBookingCustomAttributeDefinitionResponse:
        """Updates a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            key: The key of the custom attribute definition to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_booking_custom_attribute_definition(
            key, body, request_options=request_options
        ).unwrap()

    def upsert_booking_custom_attribute(
        self,
        booking_id: str,
        key: str,
        body: UpsertBookingCustomAttributeRequest | UpsertBookingCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpsertBookingCustomAttributeResponse:
        """Upserts a bookings custom attribute.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            key: The key of the custom attribute to create or update. This key must match the ``key`` of a custom
                attribute definition in the Square seller account. If the requesting application is not the definition
                owner, you must use the qualified key.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.upsert_booking_custom_attribute(
            booking_id, key, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> BookingCustomAttributesWithRawResponse:
        return self._with_raw_response


class AsyncBookingCustomAttributes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBookingCustomAttributesWithRawResponse(client, server, auth)

    async def bulk_delete_booking_custom_attributes(
        self,
        body: BulkDeleteBookingCustomAttributesRequest | BulkDeleteBookingCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkDeleteBookingCustomAttributesResponse:
        """Bulk deletes bookings custom attributes.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.bulk_delete_booking_custom_attributes(body, request_options=request_options)
        ).unwrap()

    async def bulk_upsert_booking_custom_attributes(
        self,
        body: BulkUpsertBookingCustomAttributesRequest | BulkUpsertBookingCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpsertBookingCustomAttributesResponse:
        """Bulk upserts bookings custom attributes.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.bulk_upsert_booking_custom_attributes(body, request_options=request_options)
        ).unwrap()

    async def create_booking_custom_attribute_definition(
        self,
        body: CreateBookingCustomAttributeDefinitionRequest | CreateBookingCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateBookingCustomAttributeDefinitionResponse:
        """Creates a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_booking_custom_attribute_definition(
                body, request_options=request_options
            )
        ).unwrap()

    async def delete_booking_custom_attribute(
        self, booking_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteBookingCustomAttributeResponse:
        """Deletes a bookings custom attribute.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_booking_custom_attribute(
                booking_id, key, request_options=request_options
            )
        ).unwrap()

    async def delete_booking_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteBookingCustomAttributeDefinitionResponse:
        """Deletes a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_booking_custom_attribute_definition(
                key, request_options=request_options
            )
        ).unwrap()

    async def list_booking_custom_attribute_definitions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBookingCustomAttributeDefinitionsResponse:
        """Get all bookings custom attribute definitions.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_booking_custom_attribute_definitions(
                limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def list_booking_custom_attributes(
        self,
        booking_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBookingCustomAttributesResponse:
        """Lists a booking's custom attributes.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            with_definitions: Indicates whether to return the `custom attribute definition
                <entity:CustomAttributeDefinition>`__ in the ``definition`` field of each custom attribute. Set this
                parameter to ``true`` to get the name and description of each custom attribute, information about the
                data type, or other definition details. The default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_booking_custom_attributes(
                booking_id,
                limit=limit,
                cursor=cursor,
                with_definitions=with_definitions,
                request_options=request_options,
            )
        ).unwrap()

    async def retrieve_booking_custom_attribute(
        self,
        booking_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveBookingCustomAttributeResponse:
        """Retrieves a bookings custom attribute.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            key: The key of the custom attribute to retrieve. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            with_definition: Indicates whether to return the `custom attribute definition
                <entity:CustomAttributeDefinition>`__ in the ``definition`` field of the custom attribute. Set this
                parameter to ``true`` to get the name and description of the custom attribute, information about the
                data type, or other definition details. The default value is ``false``.
            version: The current version of the custom attribute, which is used for strongly consistent reads to
                guarantee that you receive the most up-to-date data. When included in the request, Square returns the
                specified version or a higher version if one exists. If the specified version is higher than the current
                version, Square returns a ``BAD_REQUEST`` error.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_booking_custom_attribute(
                booking_id, key, with_definition=with_definition, version=version, request_options=request_options
            )
        ).unwrap()

    async def retrieve_booking_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveBookingCustomAttributeDefinitionResponse:
        """Retrieves a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            key: The key of the custom attribute definition to retrieve. If the requesting application is not the
                definition owner, you must use the qualified key.
            version: The current version of the custom attribute definition, which is used for strongly consistent reads
                to guarantee that you receive the most up-to-date data. When included in the request, Square returns the
                specified version or a higher version if one exists. If the specified version is higher than the current
                version, Square returns a ``BAD_REQUEST`` error.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_booking_custom_attribute_definition(
                key, version=version, request_options=request_options
            )
        ).unwrap()

    async def update_booking_custom_attribute_definition(
        self,
        key: str,
        body: UpdateBookingCustomAttributeDefinitionRequest | UpdateBookingCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateBookingCustomAttributeDefinitionResponse:
        """Updates a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            key: The key of the custom attribute definition to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_booking_custom_attribute_definition(
                key, body, request_options=request_options
            )
        ).unwrap()

    async def upsert_booking_custom_attribute(
        self,
        booking_id: str,
        key: str,
        body: UpsertBookingCustomAttributeRequest | UpsertBookingCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpsertBookingCustomAttributeResponse:
        """Upserts a bookings custom attribute.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            key: The key of the custom attribute to create or update. This key must match the ``key`` of a custom
                attribute definition in the Square seller account. If the requesting application is not the definition
                owner, you must use the qualified key.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.upsert_booking_custom_attribute(
                booking_id, key, body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncBookingCustomAttributesWithRawResponse:
        return self._with_raw_response


class BookingCustomAttributesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bulk_delete_booking_custom_attributes(
        self,
        body: BulkDeleteBookingCustomAttributesRequest | BulkDeleteBookingCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkDeleteBookingCustomAttributesResponse, RawError]:
        """Bulk deletes bookings custom attributes.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings/custom-attributes/bulk-delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkDeleteBookingCustomAttributesRequest | BulkDeleteBookingCustomAttributesRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkDeleteBookingCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bulk_upsert_booking_custom_attributes(
        self,
        body: BulkUpsertBookingCustomAttributesRequest | BulkUpsertBookingCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpsertBookingCustomAttributesResponse, RawError]:
        """Bulk upserts bookings custom attributes.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings/custom-attributes/bulk-upsert"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkUpsertBookingCustomAttributesRequest | BulkUpsertBookingCustomAttributesRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkUpsertBookingCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_booking_custom_attribute_definition(
        self,
        body: CreateBookingCustomAttributeDefinitionRequest | CreateBookingCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateBookingCustomAttributeDefinitionResponse, RawError]:
        """Creates a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings/custom-attribute-definitions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                CreateBookingCustomAttributeDefinitionRequest | CreateBookingCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateBookingCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_booking_custom_attribute(
        self, booking_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteBookingCustomAttributeResponse, RawError]:
        """Deletes a bookings custom attribute.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/bookings/{booking_id}/custom-attributes/{key}"),
            path_params=[param[str]("booking_id", booking_id), param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteBookingCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_booking_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteBookingCustomAttributeDefinitionResponse, RawError]:
        """Deletes a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/bookings/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteBookingCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_booking_custom_attribute_definitions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBookingCustomAttributeDefinitionsResponse, RawError]:
        """Get all bookings custom attribute definitions.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/custom-attribute-definitions"),
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListBookingCustomAttributeDefinitionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_booking_custom_attributes(
        self,
        booking_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBookingCustomAttributesResponse, RawError]:
        """Lists a booking's custom attributes.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            with_definitions: Indicates whether to return the `custom attribute definition
                <entity:CustomAttributeDefinition>`__ in the ``definition`` field of each custom attribute. Set this
                parameter to ``true`` to get the name and description of each custom attribute, information about the
                data type, or other definition details. The default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/{booking_id}/custom-attributes"),
            path_params=[param[str]("booking_id", booking_id)],
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("with_definitions", with_definitions),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListBookingCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_booking_custom_attribute(
        self,
        booking_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveBookingCustomAttributeResponse, RawError]:
        """Retrieves a bookings custom attribute.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            key: The key of the custom attribute to retrieve. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            with_definition: Indicates whether to return the `custom attribute definition
                <entity:CustomAttributeDefinition>`__ in the ``definition`` field of the custom attribute. Set this
                parameter to ``true`` to get the name and description of the custom attribute, information about the
                data type, or other definition details. The default value is ``false``.
            version: The current version of the custom attribute, which is used for strongly consistent reads to
                guarantee that you receive the most up-to-date data. When included in the request, Square returns the
                specified version or a higher version if one exists. If the specified version is higher than the current
                version, Square returns a ``BAD_REQUEST`` error.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/{booking_id}/custom-attributes/{key}"),
            path_params=[param[str]("booking_id", booking_id), param[str]("key", key)],
            query_params=[
                param[bool | None]("with_definition", with_definition), param[int | None]("version", version)
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveBookingCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_booking_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveBookingCustomAttributeDefinitionResponse, RawError]:
        """Retrieves a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            key: The key of the custom attribute definition to retrieve. If the requesting application is not the
                definition owner, you must use the qualified key.
            version: The current version of the custom attribute definition, which is used for strongly consistent reads
                to guarantee that you receive the most up-to-date data. When included in the request, Square returns the
                specified version or a higher version if one exists. If the specified version is higher than the current
                version, Square returns a ``BAD_REQUEST`` error.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            query_params=[param[int | None]("version", version)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveBookingCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_booking_custom_attribute_definition(
        self,
        key: str,
        body: UpdateBookingCustomAttributeDefinitionRequest | UpdateBookingCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateBookingCustomAttributeDefinitionResponse, RawError]:
        """Updates a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            key: The key of the custom attribute definition to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/bookings/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                UpdateBookingCustomAttributeDefinitionRequest | UpdateBookingCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateBookingCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def upsert_booking_custom_attribute(
        self,
        booking_id: str,
        key: str,
        body: UpsertBookingCustomAttributeRequest | UpsertBookingCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpsertBookingCustomAttributeResponse, RawError]:
        """Upserts a bookings custom attribute.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            key: The key of the custom attribute to create or update. This key must match the ``key`` of a custom
                attribute definition in the Square seller account. If the requesting application is not the definition
                owner, you must use the qualified key.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/bookings/{booking_id}/custom-attributes/{key}"),
            path_params=[param[str]("booking_id", booking_id), param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpsertBookingCustomAttributeRequest | UpsertBookingCustomAttributeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpsertBookingCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncBookingCustomAttributesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bulk_delete_booking_custom_attributes(
        self,
        body: BulkDeleteBookingCustomAttributesRequest | BulkDeleteBookingCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkDeleteBookingCustomAttributesResponse, RawError]:
        """Bulk deletes bookings custom attributes.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings/custom-attributes/bulk-delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkDeleteBookingCustomAttributesRequest | BulkDeleteBookingCustomAttributesRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkDeleteBookingCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bulk_upsert_booking_custom_attributes(
        self,
        body: BulkUpsertBookingCustomAttributesRequest | BulkUpsertBookingCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpsertBookingCustomAttributesResponse, RawError]:
        """Bulk upserts bookings custom attributes.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings/custom-attributes/bulk-upsert"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkUpsertBookingCustomAttributesRequest | BulkUpsertBookingCustomAttributesRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkUpsertBookingCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_booking_custom_attribute_definition(
        self,
        body: CreateBookingCustomAttributeDefinitionRequest | CreateBookingCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateBookingCustomAttributeDefinitionResponse, RawError]:
        """Creates a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings/custom-attribute-definitions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                CreateBookingCustomAttributeDefinitionRequest | CreateBookingCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateBookingCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_booking_custom_attribute(
        self, booking_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteBookingCustomAttributeResponse, RawError]:
        """Deletes a bookings custom attribute.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/bookings/{booking_id}/custom-attributes/{key}"),
            path_params=[param[str]("booking_id", booking_id), param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteBookingCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_booking_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteBookingCustomAttributeDefinitionResponse, RawError]:
        """Deletes a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/bookings/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteBookingCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_booking_custom_attribute_definitions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBookingCustomAttributeDefinitionsResponse, RawError]:
        """Get all bookings custom attribute definitions.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/custom-attribute-definitions"),
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListBookingCustomAttributeDefinitionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_booking_custom_attributes(
        self,
        booking_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBookingCustomAttributesResponse, RawError]:
        """Lists a booking's custom attributes.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            with_definitions: Indicates whether to return the `custom attribute definition
                <entity:CustomAttributeDefinition>`__ in the ``definition`` field of each custom attribute. Set this
                parameter to ``true`` to get the name and description of each custom attribute, information about the
                data type, or other definition details. The default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/{booking_id}/custom-attributes"),
            path_params=[param[str]("booking_id", booking_id)],
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("with_definitions", with_definitions),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListBookingCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_booking_custom_attribute(
        self,
        booking_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveBookingCustomAttributeResponse, RawError]:
        """Retrieves a bookings custom attribute.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            key: The key of the custom attribute to retrieve. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            with_definition: Indicates whether to return the `custom attribute definition
                <entity:CustomAttributeDefinition>`__ in the ``definition`` field of the custom attribute. Set this
                parameter to ``true`` to get the name and description of the custom attribute, information about the
                data type, or other definition details. The default value is ``false``.
            version: The current version of the custom attribute, which is used for strongly consistent reads to
                guarantee that you receive the most up-to-date data. When included in the request, Square returns the
                specified version or a higher version if one exists. If the specified version is higher than the current
                version, Square returns a ``BAD_REQUEST`` error.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/{booking_id}/custom-attributes/{key}"),
            path_params=[param[str]("booking_id", booking_id), param[str]("key", key)],
            query_params=[
                param[bool | None]("with_definition", with_definition), param[int | None]("version", version)
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveBookingCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_booking_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveBookingCustomAttributeDefinitionResponse, RawError]:
        """Retrieves a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            key: The key of the custom attribute definition to retrieve. If the requesting application is not the
                definition owner, you must use the qualified key.
            version: The current version of the custom attribute definition, which is used for strongly consistent reads
                to guarantee that you receive the most up-to-date data. When included in the request, Square returns the
                specified version or a higher version if one exists. If the specified version is higher than the current
                version, Square returns a ``BAD_REQUEST`` error.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            query_params=[param[int | None]("version", version)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveBookingCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_booking_custom_attribute_definition(
        self,
        key: str,
        body: UpdateBookingCustomAttributeDefinitionRequest | UpdateBookingCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateBookingCustomAttributeDefinitionResponse, RawError]:
        """Updates a bookings custom attribute definition.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            key: The key of the custom attribute definition to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/bookings/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                UpdateBookingCustomAttributeDefinitionRequest | UpdateBookingCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateBookingCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def upsert_booking_custom_attribute(
        self,
        booking_id: str,
        key: str,
        body: UpsertBookingCustomAttributeRequest | UpsertBookingCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpsertBookingCustomAttributeResponse, RawError]:
        """Upserts a bookings custom attribute.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the target `booking <entity:Booking>`__.
            key: The key of the custom attribute to create or update. This key must match the ``key`` of a custom
                attribute definition in the Square seller account. If the requesting application is not the definition
                owner, you must use the qualified key.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/bookings/{booking_id}/custom-attributes/{key}"),
            path_params=[param[str]("booking_id", booking_id), param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpsertBookingCustomAttributeRequest | UpsertBookingCustomAttributeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpsertBookingCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
