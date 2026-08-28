from __future__ import annotations

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
from ..models.bulk_upsert_customer_custom_attributes_request import (
    BulkUpsertCustomerCustomAttributesRequest,
    BulkUpsertCustomerCustomAttributesRequestDict,
)
from ..models.bulk_upsert_customer_custom_attributes_response import BulkUpsertCustomerCustomAttributesResponse
from ..models.create_customer_custom_attribute_definition_request import (
    CreateCustomerCustomAttributeDefinitionRequest,
    CreateCustomerCustomAttributeDefinitionRequestDict,
)
from ..models.create_customer_custom_attribute_definition_response import (
    CreateCustomerCustomAttributeDefinitionResponse,
)
from ..models.delete_customer_custom_attribute_definition_response import (
    DeleteCustomerCustomAttributeDefinitionResponse,
)
from ..models.delete_customer_custom_attribute_response import DeleteCustomerCustomAttributeResponse
from ..models.list_customer_custom_attribute_definitions_response import ListCustomerCustomAttributeDefinitionsResponse
from ..models.list_customer_custom_attributes_response import ListCustomerCustomAttributesResponse
from ..models.retrieve_customer_custom_attribute_definition_response import (
    RetrieveCustomerCustomAttributeDefinitionResponse,
)
from ..models.retrieve_customer_custom_attribute_response import RetrieveCustomerCustomAttributeResponse
from ..models.update_customer_custom_attribute_definition_request import (
    UpdateCustomerCustomAttributeDefinitionRequest,
    UpdateCustomerCustomAttributeDefinitionRequestDict,
)
from ..models.update_customer_custom_attribute_definition_response import (
    UpdateCustomerCustomAttributeDefinitionResponse,
)
from ..models.upsert_customer_custom_attribute_request import (
    UpsertCustomerCustomAttributeRequest,
    UpsertCustomerCustomAttributeRequestDict,
)
from ..models.upsert_customer_custom_attribute_response import UpsertCustomerCustomAttributeResponse
from ..server.server import Server


class CustomerCustomAttributes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CustomerCustomAttributesWithRawResponse(client, server, auth)

    def bulk_upsert_customer_custom_attributes(
        self,
        body: BulkUpsertCustomerCustomAttributesRequest | BulkUpsertCustomerCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpsertCustomerCustomAttributesResponse:
        """Creates or updates `custom attributes <entity:CustomAttribute>`__ for customer profiles as a bulk operation.

        Use this endpoint to set the value of one or more custom attributes for one or more customer profiles. A custom
        attribute is based on a custom attribute definition in a Square seller account, which is created using the
        `CreateCustomerCustomAttributeDefinition
        <api-endpoint:CustomerCustomAttributes-CreateCustomerCustomAttributeDefinition>`__ endpoint.

        This ``BulkUpsertCustomerCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and
        returns a map of individual upsert responses. Each upsert request has a unique ID and provides a customer ID and
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
        return self._with_raw_response.bulk_upsert_customer_custom_attributes(
            body, request_options=request_options
        ).unwrap()

    def create_customer_custom_attribute_definition(
        self,
        body: CreateCustomerCustomAttributeDefinitionRequest | CreateCustomerCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCustomerCustomAttributeDefinitionResponse:
        """Creates a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to define a custom attribute that can be associated with customer profiles.

        A custom attribute definition specifies the ``key``, ``visibility``, ``schema``, and other properties for a
        custom attribute. After the definition is created, you can call `UpsertCustomerCustomAttribute
        <api-endpoint:CustomerCustomAttributes-UpsertCustomerCustomAttribute>`__ or `BulkUpsertCustomerCustomAttributes
        <api-endpoint:CustomerCustomAttributes-BulkUpsertCustomerCustomAttributes>`__ to set the custom attribute for
        customer profiles in the seller's Customer Directory.

        Sellers can view all custom attributes in exported customer data, including those set to ``VISIBILITY_HIDDEN``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_customer_custom_attribute_definition(
            body, request_options=request_options
        ).unwrap()

    def delete_customer_custom_attribute(
        self, customer_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteCustomerCustomAttributeResponse:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a customer profile.

        To delete a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_customer_custom_attribute(
            customer_id, key, request_options=request_options
        ).unwrap()

    def delete_customer_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteCustomerCustomAttributeDefinitionResponse:
        """Deletes a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        Deleting a custom attribute definition also deletes the corresponding custom attribute from all customer
        profiles in the seller's Customer Directory.

        Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_customer_custom_attribute_definition(
            key, request_options=request_options
        ).unwrap()

    def list_customer_custom_attribute_definitions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomerCustomAttributeDefinitionsResponse:
        """Lists the customer-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to
        a Square seller account.

        When all response pages are retrieved, the results include all custom attribute definitions that are visible to
        the requesting application, including those that are created by other applications and set to
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

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
        return self._with_raw_response.list_customer_custom_attribute_definitions(
            limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    def list_customer_custom_attributes(
        self,
        customer_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomerCustomAttributesResponse:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with a customer profile.

        You can use the ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same
        call.

        When all response pages are retrieved, the results include all custom attributes that are visible to the
        requesting application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY``
        or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
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
        return self._with_raw_response.list_customer_custom_attributes(
            customer_id, limit=limit, cursor=cursor, with_definitions=with_definitions, request_options=request_options
        ).unwrap()

    def retrieve_customer_custom_attribute(
        self,
        customer_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveCustomerCustomAttributeResponse:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with a customer profile.

        You can use the ``with_definition`` query parameter to also retrieve the custom attribute definition in the same
        call.

        To retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
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
        return self._with_raw_response.retrieve_customer_custom_attribute(
            customer_id, key, with_definition=with_definition, version=version, request_options=request_options
        ).unwrap()

    def retrieve_customer_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveCustomerCustomAttributeDefinitionResponse:
        """Retrieves a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        To retrieve a custom attribute definition created by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

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
        return self._with_raw_response.retrieve_customer_custom_attribute_definition(
            key, version=version, request_options=request_options
        ).unwrap()

    def update_customer_custom_attribute_definition(
        self,
        key: str,
        body: UpdateCustomerCustomAttributeDefinitionRequest | UpdateCustomerCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateCustomerCustomAttributeDefinitionResponse:
        """Updates a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account.

        Use this endpoint to update the following fields: ``name``, ``description``, ``visibility``, or the ``schema``
        for a ``Selection`` data type.

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
        return self._with_raw_response.update_customer_custom_attribute_definition(
            key, body, request_options=request_options
        ).unwrap()

    def upsert_customer_custom_attribute(
        self,
        customer_id: str,
        key: str,
        body: UpsertCustomerCustomAttributeRequest | UpsertCustomerCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpsertCustomerCustomAttributeResponse:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for a customer profile.

        Use this endpoint to set the value of a custom attribute for a specified customer profile. A custom attribute is
        based on a custom attribute definition in a Square seller account, which is created using the
        `CreateCustomerCustomAttributeDefinition
        <api-endpoint:CustomerCustomAttributes-CreateCustomerCustomAttributeDefinition>`__ endpoint.

        To create or update a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
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
        return self._with_raw_response.upsert_customer_custom_attribute(
            customer_id, key, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> CustomerCustomAttributesWithRawResponse:
        return self._with_raw_response


class AsyncCustomerCustomAttributes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCustomerCustomAttributesWithRawResponse(client, server, auth)

    async def bulk_upsert_customer_custom_attributes(
        self,
        body: BulkUpsertCustomerCustomAttributesRequest | BulkUpsertCustomerCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpsertCustomerCustomAttributesResponse:
        """Creates or updates `custom attributes <entity:CustomAttribute>`__ for customer profiles as a bulk operation.

        Use this endpoint to set the value of one or more custom attributes for one or more customer profiles. A custom
        attribute is based on a custom attribute definition in a Square seller account, which is created using the
        `CreateCustomerCustomAttributeDefinition
        <api-endpoint:CustomerCustomAttributes-CreateCustomerCustomAttributeDefinition>`__ endpoint.

        This ``BulkUpsertCustomerCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and
        returns a map of individual upsert responses. Each upsert request has a unique ID and provides a customer ID and
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
            await self._with_raw_response.bulk_upsert_customer_custom_attributes(body, request_options=request_options)
        ).unwrap()

    async def create_customer_custom_attribute_definition(
        self,
        body: CreateCustomerCustomAttributeDefinitionRequest | CreateCustomerCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCustomerCustomAttributeDefinitionResponse:
        """Creates a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to define a custom attribute that can be associated with customer profiles.

        A custom attribute definition specifies the ``key``, ``visibility``, ``schema``, and other properties for a
        custom attribute. After the definition is created, you can call `UpsertCustomerCustomAttribute
        <api-endpoint:CustomerCustomAttributes-UpsertCustomerCustomAttribute>`__ or `BulkUpsertCustomerCustomAttributes
        <api-endpoint:CustomerCustomAttributes-BulkUpsertCustomerCustomAttributes>`__ to set the custom attribute for
        customer profiles in the seller's Customer Directory.

        Sellers can view all custom attributes in exported customer data, including those set to ``VISIBILITY_HIDDEN``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_customer_custom_attribute_definition(
                body, request_options=request_options
            )
        ).unwrap()

    async def delete_customer_custom_attribute(
        self, customer_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteCustomerCustomAttributeResponse:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a customer profile.

        To delete a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_customer_custom_attribute(
                customer_id, key, request_options=request_options
            )
        ).unwrap()

    async def delete_customer_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteCustomerCustomAttributeDefinitionResponse:
        """Deletes a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        Deleting a custom attribute definition also deletes the corresponding custom attribute from all customer
        profiles in the seller's Customer Directory.

        Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_customer_custom_attribute_definition(
                key, request_options=request_options
            )
        ).unwrap()

    async def list_customer_custom_attribute_definitions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomerCustomAttributeDefinitionsResponse:
        """Lists the customer-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to
        a Square seller account.

        When all response pages are retrieved, the results include all custom attribute definitions that are visible to
        the requesting application, including those that are created by other applications and set to
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

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
            await self._with_raw_response.list_customer_custom_attribute_definitions(
                limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def list_customer_custom_attributes(
        self,
        customer_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomerCustomAttributesResponse:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with a customer profile.

        You can use the ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same
        call.

        When all response pages are retrieved, the results include all custom attributes that are visible to the
        requesting application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY``
        or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
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
            await self._with_raw_response.list_customer_custom_attributes(
                customer_id,
                limit=limit,
                cursor=cursor,
                with_definitions=with_definitions,
                request_options=request_options,
            )
        ).unwrap()

    async def retrieve_customer_custom_attribute(
        self,
        customer_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveCustomerCustomAttributeResponse:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with a customer profile.

        You can use the ``with_definition`` query parameter to also retrieve the custom attribute definition in the same
        call.

        To retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
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
            await self._with_raw_response.retrieve_customer_custom_attribute(
                customer_id, key, with_definition=with_definition, version=version, request_options=request_options
            )
        ).unwrap()

    async def retrieve_customer_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveCustomerCustomAttributeDefinitionResponse:
        """Retrieves a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        To retrieve a custom attribute definition created by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

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
            await self._with_raw_response.retrieve_customer_custom_attribute_definition(
                key, version=version, request_options=request_options
            )
        ).unwrap()

    async def update_customer_custom_attribute_definition(
        self,
        key: str,
        body: UpdateCustomerCustomAttributeDefinitionRequest | UpdateCustomerCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateCustomerCustomAttributeDefinitionResponse:
        """Updates a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account.

        Use this endpoint to update the following fields: ``name``, ``description``, ``visibility``, or the ``schema``
        for a ``Selection`` data type.

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
            await self._with_raw_response.update_customer_custom_attribute_definition(
                key, body, request_options=request_options
            )
        ).unwrap()

    async def upsert_customer_custom_attribute(
        self,
        customer_id: str,
        key: str,
        body: UpsertCustomerCustomAttributeRequest | UpsertCustomerCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpsertCustomerCustomAttributeResponse:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for a customer profile.

        Use this endpoint to set the value of a custom attribute for a specified customer profile. A custom attribute is
        based on a custom attribute definition in a Square seller account, which is created using the
        `CreateCustomerCustomAttributeDefinition
        <api-endpoint:CustomerCustomAttributes-CreateCustomerCustomAttributeDefinition>`__ endpoint.

        To create or update a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
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
            await self._with_raw_response.upsert_customer_custom_attribute(
                customer_id, key, body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCustomerCustomAttributesWithRawResponse:
        return self._with_raw_response


class CustomerCustomAttributesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bulk_upsert_customer_custom_attributes(
        self,
        body: BulkUpsertCustomerCustomAttributesRequest | BulkUpsertCustomerCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpsertCustomerCustomAttributesResponse, RawError]:
        """Creates or updates `custom attributes <entity:CustomAttribute>`__ for customer profiles as a bulk operation.

        Use this endpoint to set the value of one or more custom attributes for one or more customer profiles. A custom
        attribute is based on a custom attribute definition in a Square seller account, which is created using the
        `CreateCustomerCustomAttributeDefinition
        <api-endpoint:CustomerCustomAttributes-CreateCustomerCustomAttributeDefinition>`__ endpoint.

        This ``BulkUpsertCustomerCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and
        returns a map of individual upsert responses. Each upsert request has a unique ID and provides a customer ID and
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
            url_template=self._server.default("/v2/customers/custom-attributes/bulk-upsert"),
            body=json_body[BulkUpsertCustomerCustomAttributesRequest | BulkUpsertCustomerCustomAttributesRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkUpsertCustomerCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_customer_custom_attribute_definition(
        self,
        body: CreateCustomerCustomAttributeDefinitionRequest | CreateCustomerCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCustomerCustomAttributeDefinitionResponse, RawError]:
        """Creates a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to define a custom attribute that can be associated with customer profiles.

        A custom attribute definition specifies the ``key``, ``visibility``, ``schema``, and other properties for a
        custom attribute. After the definition is created, you can call `UpsertCustomerCustomAttribute
        <api-endpoint:CustomerCustomAttributes-UpsertCustomerCustomAttribute>`__ or `BulkUpsertCustomerCustomAttributes
        <api-endpoint:CustomerCustomAttributes-BulkUpsertCustomerCustomAttributes>`__ to set the custom attribute for
        customer profiles in the seller's Customer Directory.

        Sellers can view all custom attributes in exported customer data, including those set to ``VISIBILITY_HIDDEN``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/custom-attribute-definitions"),
            body=json_body[
                CreateCustomerCustomAttributeDefinitionRequest | CreateCustomerCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateCustomerCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_customer_custom_attribute(
        self, customer_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteCustomerCustomAttributeResponse, RawError]:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a customer profile.

        To delete a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/customers/{customer_id}/custom-attributes/{key}"),
            path_params=[param[str]("customer_id", customer_id), param[str]("key", key)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteCustomerCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_customer_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteCustomerCustomAttributeDefinitionResponse, RawError]:
        """Deletes a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        Deleting a custom attribute definition also deletes the corresponding custom attribute from all customer
        profiles in the seller's Customer Directory.

        Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/customers/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteCustomerCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_customer_custom_attribute_definitions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomerCustomAttributeDefinitionsResponse, RawError]:
        """Lists the customer-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to
        a Square seller account.

        When all response pages are retrieved, the results include all custom attribute definitions that are visible to
        the requesting application, including those that are created by other applications and set to
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

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
            url_template=self._server.default("/v2/customers/custom-attribute-definitions"),
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCustomerCustomAttributeDefinitionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_customer_custom_attributes(
        self,
        customer_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomerCustomAttributesResponse, RawError]:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with a customer profile.

        You can use the ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same
        call.

        When all response pages are retrieved, the results include all custom attributes that are visible to the
        requesting application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY``
        or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
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
            url_template=self._server.default("/v2/customers/{customer_id}/custom-attributes"),
            path_params=[param[str]("customer_id", customer_id)],
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("with_definitions", with_definitions),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCustomerCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_customer_custom_attribute(
        self,
        customer_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveCustomerCustomAttributeResponse, RawError]:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with a customer profile.

        You can use the ``with_definition`` query parameter to also retrieve the custom attribute definition in the same
        call.

        To retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
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
            url_template=self._server.default("/v2/customers/{customer_id}/custom-attributes/{key}"),
            path_params=[param[str]("customer_id", customer_id), param[str]("key", key)],
            query_params=[
                param[bool | None]("with_definition", with_definition), param[int | None]("version", version)
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveCustomerCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_customer_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveCustomerCustomAttributeDefinitionResponse, RawError]:
        """Retrieves a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        To retrieve a custom attribute definition created by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

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
            url_template=self._server.default("/v2/customers/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            query_params=[param[int | None]("version", version)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveCustomerCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_customer_custom_attribute_definition(
        self,
        key: str,
        body: UpdateCustomerCustomAttributeDefinitionRequest | UpdateCustomerCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateCustomerCustomAttributeDefinitionResponse, RawError]:
        """Updates a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account.

        Use this endpoint to update the following fields: ``name``, ``description``, ``visibility``, or the ``schema``
        for a ``Selection`` data type.

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
            url_template=self._server.default("/v2/customers/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            body=json_body[
                UpdateCustomerCustomAttributeDefinitionRequest | UpdateCustomerCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateCustomerCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def upsert_customer_custom_attribute(
        self,
        customer_id: str,
        key: str,
        body: UpsertCustomerCustomAttributeRequest | UpsertCustomerCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpsertCustomerCustomAttributeResponse, RawError]:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for a customer profile.

        Use this endpoint to set the value of a custom attribute for a specified customer profile. A custom attribute is
        based on a custom attribute definition in a Square seller account, which is created using the
        `CreateCustomerCustomAttributeDefinition
        <api-endpoint:CustomerCustomAttributes-CreateCustomerCustomAttributeDefinition>`__ endpoint.

        To create or update a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
            key: The key of the custom attribute to create or update. This key must match the ``key`` of a custom
                attribute definition in the Square seller account. If the requesting application is not the definition
                owner, you must use the qualified key.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/{customer_id}/custom-attributes/{key}"),
            path_params=[param[str]("customer_id", customer_id), param[str]("key", key)],
            body=json_body[UpsertCustomerCustomAttributeRequest | UpsertCustomerCustomAttributeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpsertCustomerCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCustomerCustomAttributesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bulk_upsert_customer_custom_attributes(
        self,
        body: BulkUpsertCustomerCustomAttributesRequest | BulkUpsertCustomerCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpsertCustomerCustomAttributesResponse, RawError]:
        """Creates or updates `custom attributes <entity:CustomAttribute>`__ for customer profiles as a bulk operation.

        Use this endpoint to set the value of one or more custom attributes for one or more customer profiles. A custom
        attribute is based on a custom attribute definition in a Square seller account, which is created using the
        `CreateCustomerCustomAttributeDefinition
        <api-endpoint:CustomerCustomAttributes-CreateCustomerCustomAttributeDefinition>`__ endpoint.

        This ``BulkUpsertCustomerCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and
        returns a map of individual upsert responses. Each upsert request has a unique ID and provides a customer ID and
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
            url_template=self._server.default("/v2/customers/custom-attributes/bulk-upsert"),
            body=json_body[BulkUpsertCustomerCustomAttributesRequest | BulkUpsertCustomerCustomAttributesRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkUpsertCustomerCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_customer_custom_attribute_definition(
        self,
        body: CreateCustomerCustomAttributeDefinitionRequest | CreateCustomerCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCustomerCustomAttributeDefinitionResponse, RawError]:
        """Creates a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to define a custom attribute that can be associated with customer profiles.

        A custom attribute definition specifies the ``key``, ``visibility``, ``schema``, and other properties for a
        custom attribute. After the definition is created, you can call `UpsertCustomerCustomAttribute
        <api-endpoint:CustomerCustomAttributes-UpsertCustomerCustomAttribute>`__ or `BulkUpsertCustomerCustomAttributes
        <api-endpoint:CustomerCustomAttributes-BulkUpsertCustomerCustomAttributes>`__ to set the custom attribute for
        customer profiles in the seller's Customer Directory.

        Sellers can view all custom attributes in exported customer data, including those set to ``VISIBILITY_HIDDEN``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/custom-attribute-definitions"),
            body=json_body[
                CreateCustomerCustomAttributeDefinitionRequest | CreateCustomerCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateCustomerCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_customer_custom_attribute(
        self, customer_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteCustomerCustomAttributeResponse, RawError]:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a customer profile.

        To delete a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/customers/{customer_id}/custom-attributes/{key}"),
            path_params=[param[str]("customer_id", customer_id), param[str]("key", key)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteCustomerCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_customer_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteCustomerCustomAttributeDefinitionResponse, RawError]:
        """Deletes a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        Deleting a custom attribute definition also deletes the corresponding custom attribute from all customer
        profiles in the seller's Customer Directory.

        Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/customers/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteCustomerCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_customer_custom_attribute_definitions(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomerCustomAttributeDefinitionsResponse, RawError]:
        """Lists the customer-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to
        a Square seller account.

        When all response pages are retrieved, the results include all custom attribute definitions that are visible to
        the requesting application, including those that are created by other applications and set to
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

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
            url_template=self._server.default("/v2/customers/custom-attribute-definitions"),
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCustomerCustomAttributeDefinitionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_customer_custom_attributes(
        self,
        customer_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomerCustomAttributesResponse, RawError]:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with a customer profile.

        You can use the ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same
        call.

        When all response pages are retrieved, the results include all custom attributes that are visible to the
        requesting application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY``
        or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
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
            url_template=self._server.default("/v2/customers/{customer_id}/custom-attributes"),
            path_params=[param[str]("customer_id", customer_id)],
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("with_definitions", with_definitions),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCustomerCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_customer_custom_attribute(
        self,
        customer_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveCustomerCustomAttributeResponse, RawError]:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with a customer profile.

        You can use the ``with_definition`` query parameter to also retrieve the custom attribute definition in the same
        call.

        To retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
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
            url_template=self._server.default("/v2/customers/{customer_id}/custom-attributes/{key}"),
            path_params=[param[str]("customer_id", customer_id), param[str]("key", key)],
            query_params=[
                param[bool | None]("with_definition", with_definition), param[int | None]("version", version)
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveCustomerCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_customer_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveCustomerCustomAttributeDefinitionResponse, RawError]:
        """Retrieves a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account.

        To retrieve a custom attribute definition created by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also
        known as custom fields) are always set to ``VISIBILITY_READ_WRITE_VALUES``.

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
            url_template=self._server.default("/v2/customers/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            query_params=[param[int | None]("version", version)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveCustomerCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_customer_custom_attribute_definition(
        self,
        key: str,
        body: UpdateCustomerCustomAttributeDefinitionRequest | UpdateCustomerCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateCustomerCustomAttributeDefinitionResponse, RawError]:
        """Updates a customer-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account.

        Use this endpoint to update the following fields: ``name``, ``description``, ``visibility``, or the ``schema``
        for a ``Selection`` data type.

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
            url_template=self._server.default("/v2/customers/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            body=json_body[
                UpdateCustomerCustomAttributeDefinitionRequest | UpdateCustomerCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateCustomerCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def upsert_customer_custom_attribute(
        self,
        customer_id: str,
        key: str,
        body: UpsertCustomerCustomAttributeRequest | UpsertCustomerCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpsertCustomerCustomAttributeResponse, RawError]:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for a customer profile.

        Use this endpoint to set the value of a custom attribute for a specified customer profile. A custom attribute is
        based on a custom attribute definition in a Square seller account, which is created using the
        `CreateCustomerCustomAttributeDefinition
        <api-endpoint:CustomerCustomAttributes-CreateCustomerCustomAttributeDefinition>`__ endpoint.

        To create or update a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``. Note that seller-defined custom attributes (also known as custom fields) are
        always set to ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            customer_id: The ID of the target `customer profile <entity:Customer>`__.
            key: The key of the custom attribute to create or update. This key must match the ``key`` of a custom
                attribute definition in the Square seller account. If the requesting application is not the definition
                owner, you must use the qualified key.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/{customer_id}/custom-attributes/{key}"),
            path_params=[param[str]("customer_id", customer_id), param[str]("key", key)],
            body=json_body[UpsertCustomerCustomAttributeRequest | UpsertCustomerCustomAttributeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpsertCustomerCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
