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
from ..models.bulk_delete_location_custom_attributes_request import (
    BulkDeleteLocationCustomAttributesRequest,
    BulkDeleteLocationCustomAttributesRequestDict,
)
from ..models.bulk_delete_location_custom_attributes_response import BulkDeleteLocationCustomAttributesResponse
from ..models.bulk_upsert_location_custom_attributes_request import (
    BulkUpsertLocationCustomAttributesRequest,
    BulkUpsertLocationCustomAttributesRequestDict,
)
from ..models.bulk_upsert_location_custom_attributes_response import BulkUpsertLocationCustomAttributesResponse
from ..models.create_location_custom_attribute_definition_request import (
    CreateLocationCustomAttributeDefinitionRequest,
    CreateLocationCustomAttributeDefinitionRequestDict,
)
from ..models.create_location_custom_attribute_definition_response import (
    CreateLocationCustomAttributeDefinitionResponse,
)
from ..models.delete_location_custom_attribute_definition_response import (
    DeleteLocationCustomAttributeDefinitionResponse,
)
from ..models.delete_location_custom_attribute_response import DeleteLocationCustomAttributeResponse
from ..models.enums.visibility_filter import VisibilityFilterOrStr
from ..models.list_location_custom_attribute_definitions_response import ListLocationCustomAttributeDefinitionsResponse
from ..models.list_location_custom_attributes_response import ListLocationCustomAttributesResponse
from ..models.retrieve_location_custom_attribute_definition_response import (
    RetrieveLocationCustomAttributeDefinitionResponse,
)
from ..models.retrieve_location_custom_attribute_response import RetrieveLocationCustomAttributeResponse
from ..models.update_location_custom_attribute_definition_request import (
    UpdateLocationCustomAttributeDefinitionRequest,
    UpdateLocationCustomAttributeDefinitionRequestDict,
)
from ..models.update_location_custom_attribute_definition_response import (
    UpdateLocationCustomAttributeDefinitionResponse,
)
from ..models.upsert_location_custom_attribute_request import (
    UpsertLocationCustomAttributeRequest,
    UpsertLocationCustomAttributeRequestDict,
)
from ..models.upsert_location_custom_attribute_response import UpsertLocationCustomAttributeResponse
from ..server.server import Server


class LocationCustomAttributes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LocationCustomAttributesWithRawResponse(client, server, auth)

    def bulk_delete_location_custom_attributes(
        self,
        body: BulkDeleteLocationCustomAttributesRequest | BulkDeleteLocationCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkDeleteLocationCustomAttributesResponse:
        """Deletes `custom attributes <entity:CustomAttribute>`__ for locations as a bulk operation. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

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
            self._with_raw_response.bulk_delete_location_custom_attributes(body, request_options=request_options)
        )

    def bulk_upsert_location_custom_attributes(
        self,
        body: BulkUpsertLocationCustomAttributesRequest | BulkUpsertLocationCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpsertLocationCustomAttributesResponse:
        """Creates or updates `custom attributes <entity:CustomAttribute>`__ for locations as a bulk operation. Use this
        endpoint to set the value of one or more custom attributes for one or more locations. A custom attribute is
        based on a custom attribute definition in a Square seller account, which is created using the
        `CreateLocationCustomAttributeDefinition
        <api-endpoint:LocationCustomAttributes-CreateLocationCustomAttributeDefinition>`__ endpoint. This
        ``BulkUpsertLocationCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and returns
        a map of individual upsert responses. Each upsert request has a unique ID and provides a location ID and custom
        attribute. Each upsert response is returned with the ID of the corresponding request. To create or update a
        custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

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
            self._with_raw_response.bulk_upsert_location_custom_attributes(body, request_options=request_options)
        )

    def create_location_custom_attribute_definition(
        self,
        body: CreateLocationCustomAttributeDefinitionRequest | CreateLocationCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateLocationCustomAttributeDefinitionResponse:
        """Creates a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to define a custom attribute that can be associated with locations. A custom
        attribute definition specifies the ``key``, ``visibility``, ``schema``, and other properties for a custom
        attribute. After the definition is created, you can call `UpsertLocationCustomAttribute
        <api-endpoint:LocationCustomAttributes-UpsertLocationCustomAttribute>`__ or `BulkUpsertLocationCustomAttributes
        <api-endpoint:LocationCustomAttributes-BulkUpsertLocationCustomAttributes>`__ to set the custom attribute for
        locations.

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
            self._with_raw_response.create_location_custom_attribute_definition(body, request_options=request_options)
        )

    def delete_location_custom_attribute(
        self, location_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteLocationCustomAttributeResponse:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a location. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.delete_location_custom_attribute(location_id, key, request_options=request_options)
        )

    def delete_location_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteLocationCustomAttributeDefinitionResponse:
        """Deletes a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. Deleting a custom attribute definition also deletes the corresponding custom attribute from all
        locations. Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.delete_location_custom_attribute_definition(key, request_options=request_options)
        )

    def list_location_custom_attribute_definitions(
        self,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListLocationCustomAttributeDefinitionsResponse:
        """Lists the location-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to
        a Square seller account. When all response pages are retrieved, the results include all custom attribute
        definitions that are visible to the requesting application, including those that are created by other
        applications and set to ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            visibility_filter: Filters the ``CustomAttributeDefinition`` results by their ``visibility`` values.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_location_custom_attribute_definitions(
                visibility_filter=visibility_filter, limit=limit, cursor=cursor, request_options=request_options
            ),
        )

    def list_location_custom_attributes(
        self,
        location_id: str,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListLocationCustomAttributesResponse:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with a location. You can use the
        ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same call. When all
        response pages are retrieved, the results include all custom attributes that are visible to the requesting
        application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY`` or
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
            visibility_filter: Filters the ``CustomAttributeDefinition`` results by their ``visibility`` values.
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_location_custom_attributes(
                location_id,
                visibility_filter=visibility_filter,
                limit=limit,
                cursor=cursor,
                with_definitions=with_definitions,
                request_options=request_options,
            ),
        )

    def retrieve_location_custom_attribute(
        self,
        location_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveLocationCustomAttributeResponse:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with a location. You can use the
        ``with_definition`` query parameter to also retrieve the custom attribute definition in the same call. To
        retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.retrieve_location_custom_attribute(
                location_id, key, with_definition=with_definition, version=version, request_options=request_options
            ),
        )

    def retrieve_location_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLocationCustomAttributeDefinitionResponse:
        """Retrieves a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. To retrieve a custom attribute definition created by another application, the ``visibility``
        setting must be ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            key: The key of the custom attribute definition to retrieve. If the requesting application is not the
                definition owner, you must use the qualified key.
            version: The current version of the custom attribute definition, which is used for strongly consistent reads
                to guarantee that you receive the most up-to-date data. When included in the request, Square returns the
                specified version or a higher version if one exists. If the specified version is higher than the current
                version, Square returns a ``BAD_REQUEST`` error.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.retrieve_location_custom_attribute_definition(
                key, version=version, request_options=request_options
            ),
        )

    def update_location_custom_attribute_definition(
        self,
        key: str,
        body: UpdateLocationCustomAttributeDefinitionRequest | UpdateLocationCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateLocationCustomAttributeDefinitionResponse:
        """Updates a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to update the following fields: ``name``, ``description``, ``visibility``, or
        the ``schema`` for a ``Selection`` data type. Only the definition owner can update a custom attribute
        definition.

        Args:
            key: The key of the custom attribute definition to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.update_location_custom_attribute_definition(
                key, body, request_options=request_options
            ),
        )

    def upsert_location_custom_attribute(
        self,
        location_id: str,
        key: str,
        body: UpsertLocationCustomAttributeRequest | UpsertLocationCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpsertLocationCustomAttributeResponse:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for a location. Use this endpoint to set
        the value of a custom attribute for a specified location. A custom attribute is based on a custom attribute
        definition in a Square seller account, which is created using the `CreateLocationCustomAttributeDefinition
        <api-endpoint:LocationCustomAttributes-CreateLocationCustomAttributeDefinition>`__ endpoint. To create or update
        a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
            key: The key of the custom attribute to create or update. This key must match the ``key`` of a custom
                attribute definition in the Square seller account. If the requesting application is not the definition
                owner, you must use the qualified key.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.upsert_location_custom_attribute(
                location_id, key, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> LocationCustomAttributesWithRawResponse:
        return self._with_raw_response


class AsyncLocationCustomAttributes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLocationCustomAttributesWithRawResponse(client, server, auth)

    async def bulk_delete_location_custom_attributes(
        self,
        body: BulkDeleteLocationCustomAttributesRequest | BulkDeleteLocationCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkDeleteLocationCustomAttributesResponse:
        """Deletes `custom attributes <entity:CustomAttribute>`__ for locations as a bulk operation. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

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
            await self._with_raw_response.bulk_delete_location_custom_attributes(body, request_options=request_options)
        )

    async def bulk_upsert_location_custom_attributes(
        self,
        body: BulkUpsertLocationCustomAttributesRequest | BulkUpsertLocationCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpsertLocationCustomAttributesResponse:
        """Creates or updates `custom attributes <entity:CustomAttribute>`__ for locations as a bulk operation. Use this
        endpoint to set the value of one or more custom attributes for one or more locations. A custom attribute is
        based on a custom attribute definition in a Square seller account, which is created using the
        `CreateLocationCustomAttributeDefinition
        <api-endpoint:LocationCustomAttributes-CreateLocationCustomAttributeDefinition>`__ endpoint. This
        ``BulkUpsertLocationCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and returns
        a map of individual upsert responses. Each upsert request has a unique ID and provides a location ID and custom
        attribute. Each upsert response is returned with the ID of the corresponding request. To create or update a
        custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

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
            await self._with_raw_response.bulk_upsert_location_custom_attributes(body, request_options=request_options)
        )

    async def create_location_custom_attribute_definition(
        self,
        body: CreateLocationCustomAttributeDefinitionRequest | CreateLocationCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateLocationCustomAttributeDefinitionResponse:
        """Creates a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to define a custom attribute that can be associated with locations. A custom
        attribute definition specifies the ``key``, ``visibility``, ``schema``, and other properties for a custom
        attribute. After the definition is created, you can call `UpsertLocationCustomAttribute
        <api-endpoint:LocationCustomAttributes-UpsertLocationCustomAttribute>`__ or `BulkUpsertLocationCustomAttributes
        <api-endpoint:LocationCustomAttributes-BulkUpsertLocationCustomAttributes>`__ to set the custom attribute for
        locations.

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
            await self._with_raw_response.create_location_custom_attribute_definition(
                body, request_options=request_options
            ),
        )

    async def delete_location_custom_attribute(
        self, location_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteLocationCustomAttributeResponse:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a location. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_location_custom_attribute(
                location_id, key, request_options=request_options
            ),
        )

    async def delete_location_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteLocationCustomAttributeDefinitionResponse:
        """Deletes a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. Deleting a custom attribute definition also deletes the corresponding custom attribute from all
        locations. Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_location_custom_attribute_definition(
                key, request_options=request_options
            ),
        )

    async def list_location_custom_attribute_definitions(
        self,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListLocationCustomAttributeDefinitionsResponse:
        """Lists the location-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to
        a Square seller account. When all response pages are retrieved, the results include all custom attribute
        definitions that are visible to the requesting application, including those that are created by other
        applications and set to ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            visibility_filter: Filters the ``CustomAttributeDefinition`` results by their ``visibility`` values.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_location_custom_attribute_definitions(
                visibility_filter=visibility_filter, limit=limit, cursor=cursor, request_options=request_options
            ),
        )

    async def list_location_custom_attributes(
        self,
        location_id: str,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListLocationCustomAttributesResponse:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with a location. You can use the
        ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same call. When all
        response pages are retrieved, the results include all custom attributes that are visible to the requesting
        application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY`` or
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
            visibility_filter: Filters the ``CustomAttributeDefinition`` results by their ``visibility`` values.
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_location_custom_attributes(
                location_id,
                visibility_filter=visibility_filter,
                limit=limit,
                cursor=cursor,
                with_definitions=with_definitions,
                request_options=request_options,
            ),
        )

    async def retrieve_location_custom_attribute(
        self,
        location_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveLocationCustomAttributeResponse:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with a location. You can use the
        ``with_definition`` query parameter to also retrieve the custom attribute definition in the same call. To
        retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.retrieve_location_custom_attribute(
                location_id, key, with_definition=with_definition, version=version, request_options=request_options
            ),
        )

    async def retrieve_location_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLocationCustomAttributeDefinitionResponse:
        """Retrieves a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. To retrieve a custom attribute definition created by another application, the ``visibility``
        setting must be ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            key: The key of the custom attribute definition to retrieve. If the requesting application is not the
                definition owner, you must use the qualified key.
            version: The current version of the custom attribute definition, which is used for strongly consistent reads
                to guarantee that you receive the most up-to-date data. When included in the request, Square returns the
                specified version or a higher version if one exists. If the specified version is higher than the current
                version, Square returns a ``BAD_REQUEST`` error.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.retrieve_location_custom_attribute_definition(
                key, version=version, request_options=request_options
            ),
        )

    async def update_location_custom_attribute_definition(
        self,
        key: str,
        body: UpdateLocationCustomAttributeDefinitionRequest | UpdateLocationCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateLocationCustomAttributeDefinitionResponse:
        """Updates a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to update the following fields: ``name``, ``description``, ``visibility``, or
        the ``schema`` for a ``Selection`` data type. Only the definition owner can update a custom attribute
        definition.

        Args:
            key: The key of the custom attribute definition to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.update_location_custom_attribute_definition(
                key, body, request_options=request_options
            ),
        )

    async def upsert_location_custom_attribute(
        self,
        location_id: str,
        key: str,
        body: UpsertLocationCustomAttributeRequest | UpsertLocationCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpsertLocationCustomAttributeResponse:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for a location. Use this endpoint to set
        the value of a custom attribute for a specified location. A custom attribute is based on a custom attribute
        definition in a Square seller account, which is created using the `CreateLocationCustomAttributeDefinition
        <api-endpoint:LocationCustomAttributes-CreateLocationCustomAttributeDefinition>`__ endpoint. To create or update
        a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
            key: The key of the custom attribute to create or update. This key must match the ``key`` of a custom
                attribute definition in the Square seller account. If the requesting application is not the definition
                owner, you must use the qualified key.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.upsert_location_custom_attribute(
                location_id, key, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncLocationCustomAttributesWithRawResponse:
        return self._with_raw_response


class LocationCustomAttributesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bulk_delete_location_custom_attributes(
        self,
        body: BulkDeleteLocationCustomAttributesRequest | BulkDeleteLocationCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkDeleteLocationCustomAttributesResponse, RawError]:
        """Deletes `custom attributes <entity:CustomAttribute>`__ for locations as a bulk operation. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations/custom-attributes/bulk-delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkDeleteLocationCustomAttributesRequest | BulkDeleteLocationCustomAttributesRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkDeleteLocationCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bulk_upsert_location_custom_attributes(
        self,
        body: BulkUpsertLocationCustomAttributesRequest | BulkUpsertLocationCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpsertLocationCustomAttributesResponse, RawError]:
        """Creates or updates `custom attributes <entity:CustomAttribute>`__ for locations as a bulk operation. Use this
        endpoint to set the value of one or more custom attributes for one or more locations. A custom attribute is
        based on a custom attribute definition in a Square seller account, which is created using the
        `CreateLocationCustomAttributeDefinition
        <api-endpoint:LocationCustomAttributes-CreateLocationCustomAttributeDefinition>`__ endpoint. This
        ``BulkUpsertLocationCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and returns
        a map of individual upsert responses. Each upsert request has a unique ID and provides a location ID and custom
        attribute. Each upsert response is returned with the ID of the corresponding request. To create or update a
        custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations/custom-attributes/bulk-upsert"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkUpsertLocationCustomAttributesRequest | BulkUpsertLocationCustomAttributesRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkUpsertLocationCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_location_custom_attribute_definition(
        self,
        body: CreateLocationCustomAttributeDefinitionRequest | CreateLocationCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateLocationCustomAttributeDefinitionResponse, RawError]:
        """Creates a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to define a custom attribute that can be associated with locations. A custom
        attribute definition specifies the ``key``, ``visibility``, ``schema``, and other properties for a custom
        attribute. After the definition is created, you can call `UpsertLocationCustomAttribute
        <api-endpoint:LocationCustomAttributes-UpsertLocationCustomAttribute>`__ or `BulkUpsertLocationCustomAttributes
        <api-endpoint:LocationCustomAttributes-BulkUpsertLocationCustomAttributes>`__ to set the custom attribute for
        locations.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations/custom-attribute-definitions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                CreateLocationCustomAttributeDefinitionRequest | CreateLocationCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateLocationCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_location_custom_attribute(
        self, location_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteLocationCustomAttributeResponse, RawError]:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a location. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/locations/{location_id}/custom-attributes/{key}"),
            path_params=[param[str]("location_id", location_id), param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteLocationCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_location_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteLocationCustomAttributeDefinitionResponse, RawError]:
        """Deletes a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. Deleting a custom attribute definition also deletes the corresponding custom attribute from all
        locations. Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/locations/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteLocationCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_location_custom_attribute_definitions(
        self,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListLocationCustomAttributeDefinitionsResponse, RawError]:
        """Lists the location-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to
        a Square seller account. When all response pages are retrieved, the results include all custom attribute
        definitions that are visible to the requesting application, including those that are created by other
        applications and set to ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            visibility_filter: Filters the ``CustomAttributeDefinition`` results by their ``visibility`` values.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations/custom-attribute-definitions"),
            query_params=[
                param[VisibilityFilterOrStr | None]("visibility_filter", visibility_filter),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListLocationCustomAttributeDefinitionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_location_custom_attributes(
        self,
        location_id: str,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListLocationCustomAttributesResponse, RawError]:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with a location. You can use the
        ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same call. When all
        response pages are retrieved, the results include all custom attributes that are visible to the requesting
        application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY`` or
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
            visibility_filter: Filters the ``CustomAttributeDefinition`` results by their ``visibility`` values.
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations/{location_id}/custom-attributes"),
            path_params=[param[str]("location_id", location_id)],
            query_params=[
                param[VisibilityFilterOrStr | None]("visibility_filter", visibility_filter),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("with_definitions", with_definitions),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListLocationCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_location_custom_attribute(
        self,
        location_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveLocationCustomAttributeResponse, RawError]:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with a location. You can use the
        ``with_definition`` query parameter to also retrieve the custom attribute definition in the same call. To
        retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations/{location_id}/custom-attributes/{key}"),
            path_params=[param[str]("location_id", location_id), param[str]("key", key)],
            query_params=[
                param[bool | None]("with_definition", with_definition), param[int | None]("version", version)
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveLocationCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_location_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLocationCustomAttributeDefinitionResponse, RawError]:
        """Retrieves a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. To retrieve a custom attribute definition created by another application, the ``visibility``
        setting must be ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            key: The key of the custom attribute definition to retrieve. If the requesting application is not the
                definition owner, you must use the qualified key.
            version: The current version of the custom attribute definition, which is used for strongly consistent reads
                to guarantee that you receive the most up-to-date data. When included in the request, Square returns the
                specified version or a higher version if one exists. If the specified version is higher than the current
                version, Square returns a ``BAD_REQUEST`` error.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            query_params=[param[int | None]("version", version)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveLocationCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_location_custom_attribute_definition(
        self,
        key: str,
        body: UpdateLocationCustomAttributeDefinitionRequest | UpdateLocationCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateLocationCustomAttributeDefinitionResponse, RawError]:
        """Updates a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to update the following fields: ``name``, ``description``, ``visibility``, or
        the ``schema`` for a ``Selection`` data type. Only the definition owner can update a custom attribute
        definition.

        Args:
            key: The key of the custom attribute definition to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/locations/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                UpdateLocationCustomAttributeDefinitionRequest | UpdateLocationCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateLocationCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def upsert_location_custom_attribute(
        self,
        location_id: str,
        key: str,
        body: UpsertLocationCustomAttributeRequest | UpsertLocationCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpsertLocationCustomAttributeResponse, RawError]:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for a location. Use this endpoint to set
        the value of a custom attribute for a specified location. A custom attribute is based on a custom attribute
        definition in a Square seller account, which is created using the `CreateLocationCustomAttributeDefinition
        <api-endpoint:LocationCustomAttributes-CreateLocationCustomAttributeDefinition>`__ endpoint. To create or update
        a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
            key: The key of the custom attribute to create or update. This key must match the ``key`` of a custom
                attribute definition in the Square seller account. If the requesting application is not the definition
                owner, you must use the qualified key.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations/{location_id}/custom-attributes/{key}"),
            path_params=[param[str]("location_id", location_id), param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpsertLocationCustomAttributeRequest | UpsertLocationCustomAttributeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpsertLocationCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncLocationCustomAttributesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bulk_delete_location_custom_attributes(
        self,
        body: BulkDeleteLocationCustomAttributesRequest | BulkDeleteLocationCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkDeleteLocationCustomAttributesResponse, RawError]:
        """Deletes `custom attributes <entity:CustomAttribute>`__ for locations as a bulk operation. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations/custom-attributes/bulk-delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkDeleteLocationCustomAttributesRequest | BulkDeleteLocationCustomAttributesRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[BulkDeleteLocationCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bulk_upsert_location_custom_attributes(
        self,
        body: BulkUpsertLocationCustomAttributesRequest | BulkUpsertLocationCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpsertLocationCustomAttributesResponse, RawError]:
        """Creates or updates `custom attributes <entity:CustomAttribute>`__ for locations as a bulk operation. Use this
        endpoint to set the value of one or more custom attributes for one or more locations. A custom attribute is
        based on a custom attribute definition in a Square seller account, which is created using the
        `CreateLocationCustomAttributeDefinition
        <api-endpoint:LocationCustomAttributes-CreateLocationCustomAttributeDefinition>`__ endpoint. This
        ``BulkUpsertLocationCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and returns
        a map of individual upsert responses. Each upsert request has a unique ID and provides a location ID and custom
        attribute. Each upsert response is returned with the ID of the corresponding request. To create or update a
        custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations/custom-attributes/bulk-upsert"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkUpsertLocationCustomAttributesRequest | BulkUpsertLocationCustomAttributesRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[BulkUpsertLocationCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_location_custom_attribute_definition(
        self,
        body: CreateLocationCustomAttributeDefinitionRequest | CreateLocationCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateLocationCustomAttributeDefinitionResponse, RawError]:
        """Creates a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to define a custom attribute that can be associated with locations. A custom
        attribute definition specifies the ``key``, ``visibility``, ``schema``, and other properties for a custom
        attribute. After the definition is created, you can call `UpsertLocationCustomAttribute
        <api-endpoint:LocationCustomAttributes-UpsertLocationCustomAttribute>`__ or `BulkUpsertLocationCustomAttributes
        <api-endpoint:LocationCustomAttributes-BulkUpsertLocationCustomAttributes>`__ to set the custom attribute for
        locations.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations/custom-attribute-definitions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                CreateLocationCustomAttributeDefinitionRequest | CreateLocationCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CreateLocationCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_location_custom_attribute(
        self, location_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteLocationCustomAttributeResponse, RawError]:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a location. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/locations/{location_id}/custom-attributes/{key}"),
            path_params=[param[str]("location_id", location_id), param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[DeleteLocationCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_location_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteLocationCustomAttributeDefinitionResponse, RawError]:
        """Deletes a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. Deleting a custom attribute definition also deletes the corresponding custom attribute from all
        locations. Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/locations/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[DeleteLocationCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_location_custom_attribute_definitions(
        self,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListLocationCustomAttributeDefinitionsResponse, RawError]:
        """Lists the location-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to
        a Square seller account. When all response pages are retrieved, the results include all custom attribute
        definitions that are visible to the requesting application, including those that are created by other
        applications and set to ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            visibility_filter: Filters the ``CustomAttributeDefinition`` results by their ``visibility`` values.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations/custom-attribute-definitions"),
            query_params=[
                param[VisibilityFilterOrStr | None]("visibility_filter", visibility_filter),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListLocationCustomAttributeDefinitionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_location_custom_attributes(
        self,
        location_id: str,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListLocationCustomAttributesResponse, RawError]:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with a location. You can use the
        ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same call. When all
        response pages are retrieved, the results include all custom attributes that are visible to the requesting
        application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY`` or
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
            visibility_filter: Filters the ``CustomAttributeDefinition`` results by their ``visibility`` values.
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations/{location_id}/custom-attributes"),
            path_params=[param[str]("location_id", location_id)],
            query_params=[
                param[VisibilityFilterOrStr | None]("visibility_filter", visibility_filter),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("with_definitions", with_definitions),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListLocationCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_location_custom_attribute(
        self,
        location_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveLocationCustomAttributeResponse, RawError]:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with a location. You can use the
        ``with_definition`` query parameter to also retrieve the custom attribute definition in the same call. To
        retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
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
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations/{location_id}/custom-attributes/{key}"),
            path_params=[param[str]("location_id", location_id), param[str]("key", key)],
            query_params=[
                param[bool | None]("with_definition", with_definition), param[int | None]("version", version)
            ],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveLocationCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_location_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLocationCustomAttributeDefinitionResponse, RawError]:
        """Retrieves a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. To retrieve a custom attribute definition created by another application, the ``visibility``
        setting must be ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            key: The key of the custom attribute definition to retrieve. If the requesting application is not the
                definition owner, you must use the qualified key.
            version: The current version of the custom attribute definition, which is used for strongly consistent reads
                to guarantee that you receive the most up-to-date data. When included in the request, Square returns the
                specified version or a higher version if one exists. If the specified version is higher than the current
                version, Square returns a ``BAD_REQUEST`` error.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            query_params=[param[int | None]("version", version)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveLocationCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_location_custom_attribute_definition(
        self,
        key: str,
        body: UpdateLocationCustomAttributeDefinitionRequest | UpdateLocationCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateLocationCustomAttributeDefinitionResponse, RawError]:
        """Updates a location-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to update the following fields: ``name``, ``description``, ``visibility``, or
        the ``schema`` for a ``Selection`` data type. Only the definition owner can update a custom attribute
        definition.

        Args:
            key: The key of the custom attribute definition to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/locations/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                UpdateLocationCustomAttributeDefinitionRequest | UpdateLocationCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[UpdateLocationCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def upsert_location_custom_attribute(
        self,
        location_id: str,
        key: str,
        body: UpsertLocationCustomAttributeRequest | UpsertLocationCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpsertLocationCustomAttributeResponse, RawError]:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for a location. Use this endpoint to set
        the value of a custom attribute for a specified location. A custom attribute is based on a custom attribute
        definition in a Square seller account, which is created using the `CreateLocationCustomAttributeDefinition
        <api-endpoint:LocationCustomAttributes-CreateLocationCustomAttributeDefinition>`__ endpoint. To create or update
        a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            location_id: The ID of the target `location <entity:Location>`__.
            key: The key of the custom attribute to create or update. This key must match the ``key`` of a custom
                attribute definition in the Square seller account. If the requesting application is not the definition
                owner, you must use the qualified key.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations/{location_id}/custom-attributes/{key}"),
            path_params=[param[str]("location_id", location_id), param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpsertLocationCustomAttributeRequest | UpsertLocationCustomAttributeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[UpsertLocationCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
