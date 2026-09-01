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
from ..models.bulk_delete_order_custom_attributes_request import (
    BulkDeleteOrderCustomAttributesRequest,
    BulkDeleteOrderCustomAttributesRequestDict,
)
from ..models.bulk_delete_order_custom_attributes_response import BulkDeleteOrderCustomAttributesResponse
from ..models.bulk_upsert_order_custom_attributes_request import (
    BulkUpsertOrderCustomAttributesRequest,
    BulkUpsertOrderCustomAttributesRequestDict,
)
from ..models.bulk_upsert_order_custom_attributes_response import BulkUpsertOrderCustomAttributesResponse
from ..models.create_order_custom_attribute_definition_request import (
    CreateOrderCustomAttributeDefinitionRequest,
    CreateOrderCustomAttributeDefinitionRequestDict,
)
from ..models.create_order_custom_attribute_definition_response import CreateOrderCustomAttributeDefinitionResponse
from ..models.delete_order_custom_attribute_definition_response import DeleteOrderCustomAttributeDefinitionResponse
from ..models.delete_order_custom_attribute_response import DeleteOrderCustomAttributeResponse
from ..models.enums.visibility_filter import VisibilityFilterOrStr
from ..models.list_order_custom_attribute_definitions_response import ListOrderCustomAttributeDefinitionsResponse
from ..models.list_order_custom_attributes_response import ListOrderCustomAttributesResponse
from ..models.retrieve_order_custom_attribute_definition_response import RetrieveOrderCustomAttributeDefinitionResponse
from ..models.retrieve_order_custom_attribute_response import RetrieveOrderCustomAttributeResponse
from ..models.update_order_custom_attribute_definition_request import (
    UpdateOrderCustomAttributeDefinitionRequest,
    UpdateOrderCustomAttributeDefinitionRequestDict,
)
from ..models.update_order_custom_attribute_definition_response import UpdateOrderCustomAttributeDefinitionResponse
from ..models.upsert_order_custom_attribute_request import (
    UpsertOrderCustomAttributeRequest,
    UpsertOrderCustomAttributeRequestDict,
)
from ..models.upsert_order_custom_attribute_response import UpsertOrderCustomAttributeResponse
from ..server.server import Server


class OrderCustomAttributes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OrderCustomAttributesWithRawResponse(client, server, auth)

    def bulk_delete_order_custom_attributes(
        self,
        body: BulkDeleteOrderCustomAttributesRequest | BulkDeleteOrderCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkDeleteOrderCustomAttributesResponse:
        """Deletes order `custom attributes <entity:CustomAttribute>`__ as a bulk operation.

        Use this endpoint to delete one or more custom attributes from one or more orders. A custom attribute is based
        on a custom attribute definition in a Square seller account. (To create a custom attribute definition, use the
        `CreateOrderCustomAttributeDefinition
        <api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition>`__ endpoint.)

        This ``BulkDeleteOrderCustomAttributes`` endpoint accepts a map of 1 to 25 individual delete requests and
        returns a map of individual delete responses. Each delete request has a unique ID and provides an order ID and
        custom attribute. Each delete response is returned with the ID of the corresponding request.

        To delete a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_delete_order_custom_attributes(
            body, request_options=request_options
        ).unwrap()

    def bulk_upsert_order_custom_attributes(
        self,
        body: BulkUpsertOrderCustomAttributesRequest | BulkUpsertOrderCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpsertOrderCustomAttributesResponse:
        """Creates or updates order `custom attributes <entity:CustomAttribute>`__ as a bulk operation.

        Use this endpoint to delete one or more custom attributes from one or more orders. A custom attribute is based
        on a custom attribute definition in a Square seller account. (To create a custom attribute definition, use the
        `CreateOrderCustomAttributeDefinition
        <api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition>`__ endpoint.)

        This ``BulkUpsertOrderCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and
        returns a map of individual upsert responses. Each upsert request has a unique ID and provides an order ID and
        custom attribute. Each upsert response is returned with the ID of the corresponding request.

        To create or update a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_upsert_order_custom_attributes(
            body, request_options=request_options
        ).unwrap()

    def create_order_custom_attribute_definition(
        self,
        body: CreateOrderCustomAttributeDefinitionRequest | CreateOrderCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateOrderCustomAttributeDefinitionResponse:
        """Creates an order-related custom attribute definition. Use this endpoint to define a custom attribute that can
        be associated with orders.

        After creating a custom attribute definition, you can set the custom attribute for orders in the Square seller
        account.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_order_custom_attribute_definition(
            body, request_options=request_options
        ).unwrap()

    def delete_order_custom_attribute(
        self, order_id: str, custom_attribute_key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteOrderCustomAttributeResponse:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a customer profile.

        To delete a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            custom_attribute_key: The key of the custom attribute to delete. This key must match the key of an existing
                custom attribute definition.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_order_custom_attribute(
            order_id, custom_attribute_key, request_options=request_options
        ).unwrap()

    def delete_order_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteOrderCustomAttributeDefinitionResponse:
        """Deletes an order-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_order_custom_attribute_definition(
            key, request_options=request_options
        ).unwrap()

    def list_order_custom_attribute_definitions(
        self,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListOrderCustomAttributeDefinitionsResponse:
        """Lists the order-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to a
        Square seller account.

        When all response pages are retrieved, the results include all custom attribute definitions that are visible to
        the requesting application, including those that are created by other applications and set to
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            visibility_filter: Requests that all of the custom attributes be returned, or only those that are read-only
                or read-write.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_order_custom_attribute_definitions(
            visibility_filter=visibility_filter, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def list_order_custom_attributes(
        self,
        order_id: str,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListOrderCustomAttributesResponse:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with an order.

        You can use the ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same
        call.

        When all response pages are retrieved, the results include all custom attributes that are visible to the
        requesting application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY``
        or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            visibility_filter: Requests that all of the custom attributes be returned, or only those that are read-only
                or read-write.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            with_definitions: Indicates whether to return the `custom attribute definition
                <entity:CustomAttributeDefinition>`__ in the ``definition`` field of each custom attribute. Set this
                parameter to ``true`` to get the name and description of each custom attribute, information about the
                data type, or other definition details. The default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_order_custom_attributes(
            order_id,
            visibility_filter=visibility_filter,
            cursor=cursor,
            limit=limit,
            with_definitions=with_definitions,
            request_options=request_options,
        ).unwrap()

    def retrieve_order_custom_attribute(
        self,
        order_id: str,
        custom_attribute_key: str,
        *,
        version: int | None = None,
        with_definition: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveOrderCustomAttributeResponse:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with an order.

        You can use the ``with_definition`` query parameter to also retrieve the custom attribute definition in the same
        call.

        To retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            custom_attribute_key: The key of the custom attribute to retrieve. This key must match the key of an
                existing custom attribute definition.
            version: To enable `optimistic concurrency
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__
                control, include this optional field and specify the current version of the custom attribute.
            with_definition: Indicates whether to return the `custom attribute definition
                <entity:CustomAttributeDefinition>`__ in the ``definition`` field of each custom attribute. Set this
                parameter to ``true`` to get the name and description of each custom attribute, information about the
                data type, or other definition details. The default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_order_custom_attribute(
            order_id,
            custom_attribute_key,
            version=version,
            with_definition=with_definition,
            request_options=request_options,
        ).unwrap()

    def retrieve_order_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveOrderCustomAttributeDefinitionResponse:
        """Retrieves an order-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        To retrieve a custom attribute definition created by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            key: The key of the custom attribute definition to retrieve.
            version: To enable `optimistic concurrency
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__
                control, include this optional field and specify the current version of the custom attribute.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_order_custom_attribute_definition(
            key, version=version, request_options=request_options
        ).unwrap()

    def update_order_custom_attribute_definition(
        self,
        key: str,
        body: UpdateOrderCustomAttributeDefinitionRequest | UpdateOrderCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateOrderCustomAttributeDefinitionResponse:
        """Updates an order-related custom attribute definition for a Square seller account.

        Only the definition owner can update a custom attribute definition. Note that sellers can view all custom
        attributes in exported customer data, including those set to ``VISIBILITY_HIDDEN``.

        Args:
            key: The key of the custom attribute definition to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_order_custom_attribute_definition(
            key, body, request_options=request_options
        ).unwrap()

    def upsert_order_custom_attribute(
        self,
        order_id: str,
        custom_attribute_key: str,
        body: UpsertOrderCustomAttributeRequest | UpsertOrderCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpsertOrderCustomAttributeResponse:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for an order.

        Use this endpoint to set the value of a custom attribute for a specific order. A custom attribute is based on a
        custom attribute definition in a Square seller account. (To create a custom attribute definition, use the
        `CreateOrderCustomAttributeDefinition
        <api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition>`__ endpoint.)

        To create or update a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            custom_attribute_key: The key of the custom attribute to create or update. This key must match the key of an
                existing custom attribute definition.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.upsert_order_custom_attribute(
            order_id, custom_attribute_key, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> OrderCustomAttributesWithRawResponse:
        return self._with_raw_response


class AsyncOrderCustomAttributes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOrderCustomAttributesWithRawResponse(client, server, auth)

    async def bulk_delete_order_custom_attributes(
        self,
        body: BulkDeleteOrderCustomAttributesRequest | BulkDeleteOrderCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkDeleteOrderCustomAttributesResponse:
        """Deletes order `custom attributes <entity:CustomAttribute>`__ as a bulk operation.

        Use this endpoint to delete one or more custom attributes from one or more orders. A custom attribute is based
        on a custom attribute definition in a Square seller account. (To create a custom attribute definition, use the
        `CreateOrderCustomAttributeDefinition
        <api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition>`__ endpoint.)

        This ``BulkDeleteOrderCustomAttributes`` endpoint accepts a map of 1 to 25 individual delete requests and
        returns a map of individual delete responses. Each delete request has a unique ID and provides an order ID and
        custom attribute. Each delete response is returned with the ID of the corresponding request.

        To delete a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.bulk_delete_order_custom_attributes(body, request_options=request_options)
        ).unwrap()

    async def bulk_upsert_order_custom_attributes(
        self,
        body: BulkUpsertOrderCustomAttributesRequest | BulkUpsertOrderCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpsertOrderCustomAttributesResponse:
        """Creates or updates order `custom attributes <entity:CustomAttribute>`__ as a bulk operation.

        Use this endpoint to delete one or more custom attributes from one or more orders. A custom attribute is based
        on a custom attribute definition in a Square seller account. (To create a custom attribute definition, use the
        `CreateOrderCustomAttributeDefinition
        <api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition>`__ endpoint.)

        This ``BulkUpsertOrderCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and
        returns a map of individual upsert responses. Each upsert request has a unique ID and provides an order ID and
        custom attribute. Each upsert response is returned with the ID of the corresponding request.

        To create or update a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.bulk_upsert_order_custom_attributes(body, request_options=request_options)
        ).unwrap()

    async def create_order_custom_attribute_definition(
        self,
        body: CreateOrderCustomAttributeDefinitionRequest | CreateOrderCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateOrderCustomAttributeDefinitionResponse:
        """Creates an order-related custom attribute definition. Use this endpoint to define a custom attribute that can
        be associated with orders.

        After creating a custom attribute definition, you can set the custom attribute for orders in the Square seller
        account.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_order_custom_attribute_definition(
                body, request_options=request_options
            )
        ).unwrap()

    async def delete_order_custom_attribute(
        self, order_id: str, custom_attribute_key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteOrderCustomAttributeResponse:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a customer profile.

        To delete a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            custom_attribute_key: The key of the custom attribute to delete. This key must match the key of an existing
                custom attribute definition.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_order_custom_attribute(
                order_id, custom_attribute_key, request_options=request_options
            )
        ).unwrap()

    async def delete_order_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteOrderCustomAttributeDefinitionResponse:
        """Deletes an order-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_order_custom_attribute_definition(key, request_options=request_options)
        ).unwrap()

    async def list_order_custom_attribute_definitions(
        self,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListOrderCustomAttributeDefinitionsResponse:
        """Lists the order-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to a
        Square seller account.

        When all response pages are retrieved, the results include all custom attribute definitions that are visible to
        the requesting application, including those that are created by other applications and set to
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            visibility_filter: Requests that all of the custom attributes be returned, or only those that are read-only
                or read-write.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_order_custom_attribute_definitions(
                visibility_filter=visibility_filter, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def list_order_custom_attributes(
        self,
        order_id: str,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListOrderCustomAttributesResponse:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with an order.

        You can use the ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same
        call.

        When all response pages are retrieved, the results include all custom attributes that are visible to the
        requesting application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY``
        or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            visibility_filter: Requests that all of the custom attributes be returned, or only those that are read-only
                or read-write.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
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
            await self._with_raw_response.list_order_custom_attributes(
                order_id,
                visibility_filter=visibility_filter,
                cursor=cursor,
                limit=limit,
                with_definitions=with_definitions,
                request_options=request_options,
            )
        ).unwrap()

    async def retrieve_order_custom_attribute(
        self,
        order_id: str,
        custom_attribute_key: str,
        *,
        version: int | None = None,
        with_definition: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveOrderCustomAttributeResponse:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with an order.

        You can use the ``with_definition`` query parameter to also retrieve the custom attribute definition in the same
        call.

        To retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            custom_attribute_key: The key of the custom attribute to retrieve. This key must match the key of an
                existing custom attribute definition.
            version: To enable `optimistic concurrency
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__
                control, include this optional field and specify the current version of the custom attribute.
            with_definition: Indicates whether to return the `custom attribute definition
                <entity:CustomAttributeDefinition>`__ in the ``definition`` field of each custom attribute. Set this
                parameter to ``true`` to get the name and description of each custom attribute, information about the
                data type, or other definition details. The default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_order_custom_attribute(
                order_id,
                custom_attribute_key,
                version=version,
                with_definition=with_definition,
                request_options=request_options,
            )
        ).unwrap()

    async def retrieve_order_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveOrderCustomAttributeDefinitionResponse:
        """Retrieves an order-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        To retrieve a custom attribute definition created by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            key: The key of the custom attribute definition to retrieve.
            version: To enable `optimistic concurrency
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__
                control, include this optional field and specify the current version of the custom attribute.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_order_custom_attribute_definition(
                key, version=version, request_options=request_options
            )
        ).unwrap()

    async def update_order_custom_attribute_definition(
        self,
        key: str,
        body: UpdateOrderCustomAttributeDefinitionRequest | UpdateOrderCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateOrderCustomAttributeDefinitionResponse:
        """Updates an order-related custom attribute definition for a Square seller account.

        Only the definition owner can update a custom attribute definition. Note that sellers can view all custom
        attributes in exported customer data, including those set to ``VISIBILITY_HIDDEN``.

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
            await self._with_raw_response.update_order_custom_attribute_definition(
                key, body, request_options=request_options
            )
        ).unwrap()

    async def upsert_order_custom_attribute(
        self,
        order_id: str,
        custom_attribute_key: str,
        body: UpsertOrderCustomAttributeRequest | UpsertOrderCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpsertOrderCustomAttributeResponse:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for an order.

        Use this endpoint to set the value of a custom attribute for a specific order. A custom attribute is based on a
        custom attribute definition in a Square seller account. (To create a custom attribute definition, use the
        `CreateOrderCustomAttributeDefinition
        <api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition>`__ endpoint.)

        To create or update a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            custom_attribute_key: The key of the custom attribute to create or update. This key must match the key of an
                existing custom attribute definition.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.upsert_order_custom_attribute(
                order_id, custom_attribute_key, body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncOrderCustomAttributesWithRawResponse:
        return self._with_raw_response


class OrderCustomAttributesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bulk_delete_order_custom_attributes(
        self,
        body: BulkDeleteOrderCustomAttributesRequest | BulkDeleteOrderCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkDeleteOrderCustomAttributesResponse, RawError]:
        """Deletes order `custom attributes <entity:CustomAttribute>`__ as a bulk operation.

        Use this endpoint to delete one or more custom attributes from one or more orders. A custom attribute is based
        on a custom attribute definition in a Square seller account. (To create a custom attribute definition, use the
        `CreateOrderCustomAttributeDefinition
        <api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition>`__ endpoint.)

        This ``BulkDeleteOrderCustomAttributes`` endpoint accepts a map of 1 to 25 individual delete requests and
        returns a map of individual delete responses. Each delete request has a unique ID and provides an order ID and
        custom attribute. Each delete response is returned with the ID of the corresponding request.

        To delete a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/custom-attributes/bulk-delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkDeleteOrderCustomAttributesRequest | BulkDeleteOrderCustomAttributesRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkDeleteOrderCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bulk_upsert_order_custom_attributes(
        self,
        body: BulkUpsertOrderCustomAttributesRequest | BulkUpsertOrderCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpsertOrderCustomAttributesResponse, RawError]:
        """Creates or updates order `custom attributes <entity:CustomAttribute>`__ as a bulk operation.

        Use this endpoint to delete one or more custom attributes from one or more orders. A custom attribute is based
        on a custom attribute definition in a Square seller account. (To create a custom attribute definition, use the
        `CreateOrderCustomAttributeDefinition
        <api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition>`__ endpoint.)

        This ``BulkUpsertOrderCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and
        returns a map of individual upsert responses. Each upsert request has a unique ID and provides an order ID and
        custom attribute. Each upsert response is returned with the ID of the corresponding request.

        To create or update a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/custom-attributes/bulk-upsert"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkUpsertOrderCustomAttributesRequest | BulkUpsertOrderCustomAttributesRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkUpsertOrderCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_order_custom_attribute_definition(
        self,
        body: CreateOrderCustomAttributeDefinitionRequest | CreateOrderCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateOrderCustomAttributeDefinitionResponse, RawError]:
        """Creates an order-related custom attribute definition. Use this endpoint to define a custom attribute that can
        be associated with orders.

        After creating a custom attribute definition, you can set the custom attribute for orders in the Square seller
        account.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/custom-attribute-definitions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                CreateOrderCustomAttributeDefinitionRequest | CreateOrderCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateOrderCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_order_custom_attribute(
        self, order_id: str, custom_attribute_key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteOrderCustomAttributeResponse, RawError]:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a customer profile.

        To delete a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            custom_attribute_key: The key of the custom attribute to delete. This key must match the key of an existing
                custom attribute definition.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/orders/{order_id}/custom-attributes/{custom_attribute_key}"),
            path_params=[param[str]("order_id", order_id), param[str]("custom_attribute_key", custom_attribute_key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteOrderCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_order_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteOrderCustomAttributeDefinitionResponse, RawError]:
        """Deletes an order-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/orders/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteOrderCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_order_custom_attribute_definitions(
        self,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListOrderCustomAttributeDefinitionsResponse, RawError]:
        """Lists the order-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to a
        Square seller account.

        When all response pages are retrieved, the results include all custom attribute definitions that are visible to
        the requesting application, including those that are created by other applications and set to
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            visibility_filter: Requests that all of the custom attributes be returned, or only those that are read-only
                or read-write.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/orders/custom-attribute-definitions"),
            query_params=[
                param[VisibilityFilterOrStr | None]("visibility_filter", visibility_filter),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListOrderCustomAttributeDefinitionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_order_custom_attributes(
        self,
        order_id: str,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListOrderCustomAttributesResponse, RawError]:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with an order.

        You can use the ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same
        call.

        When all response pages are retrieved, the results include all custom attributes that are visible to the
        requesting application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY``
        or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            visibility_filter: Requests that all of the custom attributes be returned, or only those that are read-only
                or read-write.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            with_definitions: Indicates whether to return the `custom attribute definition
                <entity:CustomAttributeDefinition>`__ in the ``definition`` field of each custom attribute. Set this
                parameter to ``true`` to get the name and description of each custom attribute, information about the
                data type, or other definition details. The default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/orders/{order_id}/custom-attributes"),
            path_params=[param[str]("order_id", order_id)],
            query_params=[
                param[VisibilityFilterOrStr | None]("visibility_filter", visibility_filter),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
                param[bool | None]("with_definitions", with_definitions),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListOrderCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_order_custom_attribute(
        self,
        order_id: str,
        custom_attribute_key: str,
        *,
        version: int | None = None,
        with_definition: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveOrderCustomAttributeResponse, RawError]:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with an order.

        You can use the ``with_definition`` query parameter to also retrieve the custom attribute definition in the same
        call.

        To retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            custom_attribute_key: The key of the custom attribute to retrieve. This key must match the key of an
                existing custom attribute definition.
            version: To enable `optimistic concurrency
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__
                control, include this optional field and specify the current version of the custom attribute.
            with_definition: Indicates whether to return the `custom attribute definition
                <entity:CustomAttributeDefinition>`__ in the ``definition`` field of each custom attribute. Set this
                parameter to ``true`` to get the name and description of each custom attribute, information about the
                data type, or other definition details. The default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/orders/{order_id}/custom-attributes/{custom_attribute_key}"),
            path_params=[param[str]("order_id", order_id), param[str]("custom_attribute_key", custom_attribute_key)],
            query_params=[
                param[int | None]("version", version), param[bool | None]("with_definition", with_definition)
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveOrderCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_order_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveOrderCustomAttributeDefinitionResponse, RawError]:
        """Retrieves an order-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        To retrieve a custom attribute definition created by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            key: The key of the custom attribute definition to retrieve.
            version: To enable `optimistic concurrency
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__
                control, include this optional field and specify the current version of the custom attribute.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/orders/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            query_params=[param[int | None]("version", version)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveOrderCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_order_custom_attribute_definition(
        self,
        key: str,
        body: UpdateOrderCustomAttributeDefinitionRequest | UpdateOrderCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateOrderCustomAttributeDefinitionResponse, RawError]:
        """Updates an order-related custom attribute definition for a Square seller account.

        Only the definition owner can update a custom attribute definition. Note that sellers can view all custom
        attributes in exported customer data, including those set to ``VISIBILITY_HIDDEN``.

        Args:
            key: The key of the custom attribute definition to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/orders/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                UpdateOrderCustomAttributeDefinitionRequest | UpdateOrderCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateOrderCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def upsert_order_custom_attribute(
        self,
        order_id: str,
        custom_attribute_key: str,
        body: UpsertOrderCustomAttributeRequest | UpsertOrderCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpsertOrderCustomAttributeResponse, RawError]:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for an order.

        Use this endpoint to set the value of a custom attribute for a specific order. A custom attribute is based on a
        custom attribute definition in a Square seller account. (To create a custom attribute definition, use the
        `CreateOrderCustomAttributeDefinition
        <api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition>`__ endpoint.)

        To create or update a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            custom_attribute_key: The key of the custom attribute to create or update. This key must match the key of an
                existing custom attribute definition.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/{order_id}/custom-attributes/{custom_attribute_key}"),
            path_params=[param[str]("order_id", order_id), param[str]("custom_attribute_key", custom_attribute_key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpsertOrderCustomAttributeRequest | UpsertOrderCustomAttributeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpsertOrderCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncOrderCustomAttributesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bulk_delete_order_custom_attributes(
        self,
        body: BulkDeleteOrderCustomAttributesRequest | BulkDeleteOrderCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkDeleteOrderCustomAttributesResponse, RawError]:
        """Deletes order `custom attributes <entity:CustomAttribute>`__ as a bulk operation.

        Use this endpoint to delete one or more custom attributes from one or more orders. A custom attribute is based
        on a custom attribute definition in a Square seller account. (To create a custom attribute definition, use the
        `CreateOrderCustomAttributeDefinition
        <api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition>`__ endpoint.)

        This ``BulkDeleteOrderCustomAttributes`` endpoint accepts a map of 1 to 25 individual delete requests and
        returns a map of individual delete responses. Each delete request has a unique ID and provides an order ID and
        custom attribute. Each delete response is returned with the ID of the corresponding request.

        To delete a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/custom-attributes/bulk-delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkDeleteOrderCustomAttributesRequest | BulkDeleteOrderCustomAttributesRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkDeleteOrderCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bulk_upsert_order_custom_attributes(
        self,
        body: BulkUpsertOrderCustomAttributesRequest | BulkUpsertOrderCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpsertOrderCustomAttributesResponse, RawError]:
        """Creates or updates order `custom attributes <entity:CustomAttribute>`__ as a bulk operation.

        Use this endpoint to delete one or more custom attributes from one or more orders. A custom attribute is based
        on a custom attribute definition in a Square seller account. (To create a custom attribute definition, use the
        `CreateOrderCustomAttributeDefinition
        <api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition>`__ endpoint.)

        This ``BulkUpsertOrderCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and
        returns a map of individual upsert responses. Each upsert request has a unique ID and provides an order ID and
        custom attribute. Each upsert response is returned with the ID of the corresponding request.

        To create or update a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/custom-attributes/bulk-upsert"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkUpsertOrderCustomAttributesRequest | BulkUpsertOrderCustomAttributesRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkUpsertOrderCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_order_custom_attribute_definition(
        self,
        body: CreateOrderCustomAttributeDefinitionRequest | CreateOrderCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateOrderCustomAttributeDefinitionResponse, RawError]:
        """Creates an order-related custom attribute definition. Use this endpoint to define a custom attribute that can
        be associated with orders.

        After creating a custom attribute definition, you can set the custom attribute for orders in the Square seller
        account.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/custom-attribute-definitions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                CreateOrderCustomAttributeDefinitionRequest | CreateOrderCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateOrderCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_order_custom_attribute(
        self, order_id: str, custom_attribute_key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteOrderCustomAttributeResponse, RawError]:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a customer profile.

        To delete a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            custom_attribute_key: The key of the custom attribute to delete. This key must match the key of an existing
                custom attribute definition.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/orders/{order_id}/custom-attributes/{custom_attribute_key}"),
            path_params=[param[str]("order_id", order_id), param[str]("custom_attribute_key", custom_attribute_key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteOrderCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_order_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteOrderCustomAttributeDefinitionResponse, RawError]:
        """Deletes an order-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/orders/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteOrderCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_order_custom_attribute_definitions(
        self,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListOrderCustomAttributeDefinitionsResponse, RawError]:
        """Lists the order-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to a
        Square seller account.

        When all response pages are retrieved, the results include all custom attribute definitions that are visible to
        the requesting application, including those that are created by other applications and set to
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            visibility_filter: Requests that all of the custom attributes be returned, or only those that are read-only
                or read-write.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/orders/custom-attribute-definitions"),
            query_params=[
                param[VisibilityFilterOrStr | None]("visibility_filter", visibility_filter),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListOrderCustomAttributeDefinitionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_order_custom_attributes(
        self,
        order_id: str,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListOrderCustomAttributesResponse, RawError]:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with an order.

        You can use the ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same
        call.

        When all response pages are retrieved, the results include all custom attributes that are visible to the
        requesting application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY``
        or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            visibility_filter: Requests that all of the custom attributes be returned, or only those that are read-only
                or read-write.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            limit: The maximum number of results to return in a single paged response. This limit is advisory. The
                response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. The
                default value is 20. For more information, see `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__.
            with_definitions: Indicates whether to return the `custom attribute definition
                <entity:CustomAttributeDefinition>`__ in the ``definition`` field of each custom attribute. Set this
                parameter to ``true`` to get the name and description of each custom attribute, information about the
                data type, or other definition details. The default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/orders/{order_id}/custom-attributes"),
            path_params=[param[str]("order_id", order_id)],
            query_params=[
                param[VisibilityFilterOrStr | None]("visibility_filter", visibility_filter),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
                param[bool | None]("with_definitions", with_definitions),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListOrderCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_order_custom_attribute(
        self,
        order_id: str,
        custom_attribute_key: str,
        *,
        version: int | None = None,
        with_definition: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveOrderCustomAttributeResponse, RawError]:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with an order.

        You can use the ``with_definition`` query parameter to also retrieve the custom attribute definition in the same
        call.

        To retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            custom_attribute_key: The key of the custom attribute to retrieve. This key must match the key of an
                existing custom attribute definition.
            version: To enable `optimistic concurrency
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__
                control, include this optional field and specify the current version of the custom attribute.
            with_definition: Indicates whether to return the `custom attribute definition
                <entity:CustomAttributeDefinition>`__ in the ``definition`` field of each custom attribute. Set this
                parameter to ``true`` to get the name and description of each custom attribute, information about the
                data type, or other definition details. The default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/orders/{order_id}/custom-attributes/{custom_attribute_key}"),
            path_params=[param[str]("order_id", order_id), param[str]("custom_attribute_key", custom_attribute_key)],
            query_params=[
                param[int | None]("version", version), param[bool | None]("with_definition", with_definition)
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveOrderCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_order_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveOrderCustomAttributeDefinitionResponse, RawError]:
        """Retrieves an order-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        To retrieve a custom attribute definition created by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            key: The key of the custom attribute definition to retrieve.
            version: To enable `optimistic concurrency
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__
                control, include this optional field and specify the current version of the custom attribute.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/orders/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            query_params=[param[int | None]("version", version)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveOrderCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_order_custom_attribute_definition(
        self,
        key: str,
        body: UpdateOrderCustomAttributeDefinitionRequest | UpdateOrderCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateOrderCustomAttributeDefinitionResponse, RawError]:
        """Updates an order-related custom attribute definition for a Square seller account.

        Only the definition owner can update a custom attribute definition. Note that sellers can view all custom
        attributes in exported customer data, including those set to ``VISIBILITY_HIDDEN``.

        Args:
            key: The key of the custom attribute definition to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/orders/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                UpdateOrderCustomAttributeDefinitionRequest | UpdateOrderCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateOrderCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def upsert_order_custom_attribute(
        self,
        order_id: str,
        custom_attribute_key: str,
        body: UpsertOrderCustomAttributeRequest | UpsertOrderCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpsertOrderCustomAttributeResponse, RawError]:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for an order.

        Use this endpoint to set the value of a custom attribute for a specific order. A custom attribute is based on a
        custom attribute definition in a Square seller account. (To create a custom attribute definition, use the
        `CreateOrderCustomAttributeDefinition
        <api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition>`__ endpoint.)

        To create or update a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            order_id: The ID of the target `order <entity:Order>`__.
            custom_attribute_key: The key of the custom attribute to create or update. This key must match the key of an
                existing custom attribute definition.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/{order_id}/custom-attributes/{custom_attribute_key}"),
            path_params=[param[str]("order_id", order_id), param[str]("custom_attribute_key", custom_attribute_key)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpsertOrderCustomAttributeRequest | UpsertOrderCustomAttributeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpsertOrderCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
