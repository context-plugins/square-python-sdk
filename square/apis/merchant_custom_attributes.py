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
from ..models.bulk_delete_merchant_custom_attributes_request import (
    BulkDeleteMerchantCustomAttributesRequest,
    BulkDeleteMerchantCustomAttributesRequestDict,
)
from ..models.bulk_delete_merchant_custom_attributes_response import BulkDeleteMerchantCustomAttributesResponse
from ..models.bulk_upsert_merchant_custom_attributes_request import (
    BulkUpsertMerchantCustomAttributesRequest,
    BulkUpsertMerchantCustomAttributesRequestDict,
)
from ..models.bulk_upsert_merchant_custom_attributes_response import BulkUpsertMerchantCustomAttributesResponse
from ..models.create_merchant_custom_attribute_definition_request import (
    CreateMerchantCustomAttributeDefinitionRequest,
    CreateMerchantCustomAttributeDefinitionRequestDict,
)
from ..models.create_merchant_custom_attribute_definition_response import (
    CreateMerchantCustomAttributeDefinitionResponse,
)
from ..models.delete_merchant_custom_attribute_definition_response import (
    DeleteMerchantCustomAttributeDefinitionResponse,
)
from ..models.delete_merchant_custom_attribute_response import DeleteMerchantCustomAttributeResponse
from ..models.enums.visibility_filter import VisibilityFilterOrStr
from ..models.list_merchant_custom_attribute_definitions_response import ListMerchantCustomAttributeDefinitionsResponse
from ..models.list_merchant_custom_attributes_response import ListMerchantCustomAttributesResponse
from ..models.retrieve_merchant_custom_attribute_definition_response import (
    RetrieveMerchantCustomAttributeDefinitionResponse,
)
from ..models.retrieve_merchant_custom_attribute_response import RetrieveMerchantCustomAttributeResponse
from ..models.update_merchant_custom_attribute_definition_request import (
    UpdateMerchantCustomAttributeDefinitionRequest,
    UpdateMerchantCustomAttributeDefinitionRequestDict,
)
from ..models.update_merchant_custom_attribute_definition_response import (
    UpdateMerchantCustomAttributeDefinitionResponse,
)
from ..models.upsert_merchant_custom_attribute_request import (
    UpsertMerchantCustomAttributeRequest,
    UpsertMerchantCustomAttributeRequestDict,
)
from ..models.upsert_merchant_custom_attribute_response import UpsertMerchantCustomAttributeResponse
from ..server.server import Server


class MerchantCustomAttributes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MerchantCustomAttributesWithRawResponse(client, server, auth)

    def bulk_delete_merchant_custom_attributes(
        self,
        body: BulkDeleteMerchantCustomAttributesRequest | BulkDeleteMerchantCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkDeleteMerchantCustomAttributesResponse:
        """Deletes `custom attributes <entity:CustomAttribute>`__ for a merchant as a bulk operation. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_delete_merchant_custom_attributes(
            body, request_options=request_options
        ).unwrap()

    def bulk_upsert_merchant_custom_attributes(
        self,
        body: BulkUpsertMerchantCustomAttributesRequest | BulkUpsertMerchantCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpsertMerchantCustomAttributesResponse:
        """Creates or updates `custom attributes <entity:CustomAttribute>`__ for a merchant as a bulk operation. Use
        this endpoint to set the value of one or more custom attributes for a merchant. A custom attribute is based on a
        custom attribute definition in a Square seller account, which is created using the
        `CreateMerchantCustomAttributeDefinition
        <api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition>`__ endpoint. This
        ``BulkUpsertMerchantCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and returns
        a map of individual upsert responses. Each upsert request has a unique ID and provides a merchant ID and custom
        attribute. Each upsert response is returned with the ID of the corresponding request. To create or update a
        custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_upsert_merchant_custom_attributes(
            body, request_options=request_options
        ).unwrap()

    def create_merchant_custom_attribute_definition(
        self,
        body: CreateMerchantCustomAttributeDefinitionRequest | CreateMerchantCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateMerchantCustomAttributeDefinitionResponse:
        """Creates a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to define a custom attribute that can be associated with a merchant connecting
        to your application. A custom attribute definition specifies the ``key``, ``visibility``, ``schema``, and other
        properties for a custom attribute. After the definition is created, you can call `UpsertMerchantCustomAttribute
        <api-endpoint:MerchantCustomAttributes-UpsertMerchantCustomAttribute>`__ or `BulkUpsertMerchantCustomAttributes
        <api-endpoint:MerchantCustomAttributes-BulkUpsertMerchantCustomAttributes>`__ to set the custom attribute for a
        merchant.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_merchant_custom_attribute_definition(
            body, request_options=request_options
        ).unwrap()

    def delete_merchant_custom_attribute(
        self, merchant_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteMerchantCustomAttributeResponse:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a merchant. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_merchant_custom_attribute(
            merchant_id, key, request_options=request_options
        ).unwrap()

    def delete_merchant_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteMerchantCustomAttributeDefinitionResponse:
        """Deletes a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. Deleting a custom attribute definition also deletes the corresponding custom attribute from the
        merchant. Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_merchant_custom_attribute_definition(
            key, request_options=request_options
        ).unwrap()

    def list_merchant_custom_attribute_definitions(
        self,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMerchantCustomAttributeDefinitionsResponse:
        """Lists the merchant-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_merchant_custom_attribute_definitions(
            visibility_filter=visibility_filter, limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    def list_merchant_custom_attributes(
        self,
        merchant_id: str,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMerchantCustomAttributesResponse:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with a merchant. You can use the
        ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same call. When all
        response pages are retrieved, the results include all custom attributes that are visible to the requesting
        application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY`` or
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_merchant_custom_attributes(
            merchant_id,
            visibility_filter=visibility_filter,
            limit=limit,
            cursor=cursor,
            with_definitions=with_definitions,
            request_options=request_options,
        ).unwrap()

    def retrieve_merchant_custom_attribute(
        self,
        merchant_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveMerchantCustomAttributeResponse:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with a merchant. You can use the
        ``with_definition`` query parameter to also retrieve the custom attribute definition in the same call. To
        retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
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
        return self._with_raw_response.retrieve_merchant_custom_attribute(
            merchant_id, key, with_definition=with_definition, version=version, request_options=request_options
        ).unwrap()

    def retrieve_merchant_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveMerchantCustomAttributeDefinitionResponse:
        """Retrieves a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. To retrieve a custom attribute definition created by another application, the ``visibility``
        setting must be ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

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
        return self._with_raw_response.retrieve_merchant_custom_attribute_definition(
            key, version=version, request_options=request_options
        ).unwrap()

    def update_merchant_custom_attribute_definition(
        self,
        key: str,
        body: UpdateMerchantCustomAttributeDefinitionRequest | UpdateMerchantCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateMerchantCustomAttributeDefinitionResponse:
        """Updates a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to update the following fields: ``name``, ``description``, ``visibility``, or
        the ``schema`` for a ``Selection`` data type. Only the definition owner can update a custom attribute
        definition.

        Args:
            key: The key of the custom attribute definition to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_merchant_custom_attribute_definition(
            key, body, request_options=request_options
        ).unwrap()

    def upsert_merchant_custom_attribute(
        self,
        merchant_id: str,
        key: str,
        body: UpsertMerchantCustomAttributeRequest | UpsertMerchantCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpsertMerchantCustomAttributeResponse:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for a merchant. Use this endpoint to set
        the value of a custom attribute for a specified merchant. A custom attribute is based on a custom attribute
        definition in a Square seller account, which is created using the `CreateMerchantCustomAttributeDefinition
        <api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition>`__ endpoint. To create or update
        a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
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
        return self._with_raw_response.upsert_merchant_custom_attribute(
            merchant_id, key, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> MerchantCustomAttributesWithRawResponse:
        return self._with_raw_response


class AsyncMerchantCustomAttributes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMerchantCustomAttributesWithRawResponse(client, server, auth)

    async def bulk_delete_merchant_custom_attributes(
        self,
        body: BulkDeleteMerchantCustomAttributesRequest | BulkDeleteMerchantCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkDeleteMerchantCustomAttributesResponse:
        """Deletes `custom attributes <entity:CustomAttribute>`__ for a merchant as a bulk operation. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.bulk_delete_merchant_custom_attributes(body, request_options=request_options)
        ).unwrap()

    async def bulk_upsert_merchant_custom_attributes(
        self,
        body: BulkUpsertMerchantCustomAttributesRequest | BulkUpsertMerchantCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpsertMerchantCustomAttributesResponse:
        """Creates or updates `custom attributes <entity:CustomAttribute>`__ for a merchant as a bulk operation. Use
        this endpoint to set the value of one or more custom attributes for a merchant. A custom attribute is based on a
        custom attribute definition in a Square seller account, which is created using the
        `CreateMerchantCustomAttributeDefinition
        <api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition>`__ endpoint. This
        ``BulkUpsertMerchantCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and returns
        a map of individual upsert responses. Each upsert request has a unique ID and provides a merchant ID and custom
        attribute. Each upsert response is returned with the ID of the corresponding request. To create or update a
        custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.bulk_upsert_merchant_custom_attributes(body, request_options=request_options)
        ).unwrap()

    async def create_merchant_custom_attribute_definition(
        self,
        body: CreateMerchantCustomAttributeDefinitionRequest | CreateMerchantCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateMerchantCustomAttributeDefinitionResponse:
        """Creates a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to define a custom attribute that can be associated with a merchant connecting
        to your application. A custom attribute definition specifies the ``key``, ``visibility``, ``schema``, and other
        properties for a custom attribute. After the definition is created, you can call `UpsertMerchantCustomAttribute
        <api-endpoint:MerchantCustomAttributes-UpsertMerchantCustomAttribute>`__ or `BulkUpsertMerchantCustomAttributes
        <api-endpoint:MerchantCustomAttributes-BulkUpsertMerchantCustomAttributes>`__ to set the custom attribute for a
        merchant.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_merchant_custom_attribute_definition(
                body, request_options=request_options
            )
        ).unwrap()

    async def delete_merchant_custom_attribute(
        self, merchant_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteMerchantCustomAttributeResponse:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a merchant. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_merchant_custom_attribute(
                merchant_id, key, request_options=request_options
            )
        ).unwrap()

    async def delete_merchant_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteMerchantCustomAttributeDefinitionResponse:
        """Deletes a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. Deleting a custom attribute definition also deletes the corresponding custom attribute from the
        merchant. Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_merchant_custom_attribute_definition(
                key, request_options=request_options
            )
        ).unwrap()

    async def list_merchant_custom_attribute_definitions(
        self,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMerchantCustomAttributeDefinitionsResponse:
        """Lists the merchant-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_merchant_custom_attribute_definitions(
                visibility_filter=visibility_filter, limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def list_merchant_custom_attributes(
        self,
        merchant_id: str,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListMerchantCustomAttributesResponse:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with a merchant. You can use the
        ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same call. When all
        response pages are retrieved, the results include all custom attributes that are visible to the requesting
        application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY`` or
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_merchant_custom_attributes(
                merchant_id,
                visibility_filter=visibility_filter,
                limit=limit,
                cursor=cursor,
                with_definitions=with_definitions,
                request_options=request_options,
            )
        ).unwrap()

    async def retrieve_merchant_custom_attribute(
        self,
        merchant_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveMerchantCustomAttributeResponse:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with a merchant. You can use the
        ``with_definition`` query parameter to also retrieve the custom attribute definition in the same call. To
        retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
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
            await self._with_raw_response.retrieve_merchant_custom_attribute(
                merchant_id, key, with_definition=with_definition, version=version, request_options=request_options
            )
        ).unwrap()

    async def retrieve_merchant_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveMerchantCustomAttributeDefinitionResponse:
        """Retrieves a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. To retrieve a custom attribute definition created by another application, the ``visibility``
        setting must be ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

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
            await self._with_raw_response.retrieve_merchant_custom_attribute_definition(
                key, version=version, request_options=request_options
            )
        ).unwrap()

    async def update_merchant_custom_attribute_definition(
        self,
        key: str,
        body: UpdateMerchantCustomAttributeDefinitionRequest | UpdateMerchantCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateMerchantCustomAttributeDefinitionResponse:
        """Updates a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to update the following fields: ``name``, ``description``, ``visibility``, or
        the ``schema`` for a ``Selection`` data type. Only the definition owner can update a custom attribute
        definition.

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
            await self._with_raw_response.update_merchant_custom_attribute_definition(
                key, body, request_options=request_options
            )
        ).unwrap()

    async def upsert_merchant_custom_attribute(
        self,
        merchant_id: str,
        key: str,
        body: UpsertMerchantCustomAttributeRequest | UpsertMerchantCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpsertMerchantCustomAttributeResponse:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for a merchant. Use this endpoint to set
        the value of a custom attribute for a specified merchant. A custom attribute is based on a custom attribute
        definition in a Square seller account, which is created using the `CreateMerchantCustomAttributeDefinition
        <api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition>`__ endpoint. To create or update
        a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
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
            await self._with_raw_response.upsert_merchant_custom_attribute(
                merchant_id, key, body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMerchantCustomAttributesWithRawResponse:
        return self._with_raw_response


class MerchantCustomAttributesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bulk_delete_merchant_custom_attributes(
        self,
        body: BulkDeleteMerchantCustomAttributesRequest | BulkDeleteMerchantCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkDeleteMerchantCustomAttributesResponse, RawError]:
        """Deletes `custom attributes <entity:CustomAttribute>`__ for a merchant as a bulk operation. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/merchants/custom-attributes/bulk-delete"),
            body=json_body[BulkDeleteMerchantCustomAttributesRequest | BulkDeleteMerchantCustomAttributesRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkDeleteMerchantCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bulk_upsert_merchant_custom_attributes(
        self,
        body: BulkUpsertMerchantCustomAttributesRequest | BulkUpsertMerchantCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpsertMerchantCustomAttributesResponse, RawError]:
        """Creates or updates `custom attributes <entity:CustomAttribute>`__ for a merchant as a bulk operation. Use
        this endpoint to set the value of one or more custom attributes for a merchant. A custom attribute is based on a
        custom attribute definition in a Square seller account, which is created using the
        `CreateMerchantCustomAttributeDefinition
        <api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition>`__ endpoint. This
        ``BulkUpsertMerchantCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and returns
        a map of individual upsert responses. Each upsert request has a unique ID and provides a merchant ID and custom
        attribute. Each upsert response is returned with the ID of the corresponding request. To create or update a
        custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/merchants/custom-attributes/bulk-upsert"),
            body=json_body[BulkUpsertMerchantCustomAttributesRequest | BulkUpsertMerchantCustomAttributesRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkUpsertMerchantCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_merchant_custom_attribute_definition(
        self,
        body: CreateMerchantCustomAttributeDefinitionRequest | CreateMerchantCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateMerchantCustomAttributeDefinitionResponse, RawError]:
        """Creates a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to define a custom attribute that can be associated with a merchant connecting
        to your application. A custom attribute definition specifies the ``key``, ``visibility``, ``schema``, and other
        properties for a custom attribute. After the definition is created, you can call `UpsertMerchantCustomAttribute
        <api-endpoint:MerchantCustomAttributes-UpsertMerchantCustomAttribute>`__ or `BulkUpsertMerchantCustomAttributes
        <api-endpoint:MerchantCustomAttributes-BulkUpsertMerchantCustomAttributes>`__ to set the custom attribute for a
        merchant.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/merchants/custom-attribute-definitions"),
            body=json_body[
                CreateMerchantCustomAttributeDefinitionRequest | CreateMerchantCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateMerchantCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_merchant_custom_attribute(
        self, merchant_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteMerchantCustomAttributeResponse, RawError]:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a merchant. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/merchants/{merchant_id}/custom-attributes/{key}"),
            path_params=[param[str]("merchant_id", merchant_id), param[str]("key", key)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteMerchantCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_merchant_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteMerchantCustomAttributeDefinitionResponse, RawError]:
        """Deletes a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. Deleting a custom attribute definition also deletes the corresponding custom attribute from the
        merchant. Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/merchants/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteMerchantCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_merchant_custom_attribute_definitions(
        self,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMerchantCustomAttributeDefinitionsResponse, RawError]:
        """Lists the merchant-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/merchants/custom-attribute-definitions"),
            query_params=[
                param[VisibilityFilterOrStr | None]("visibility_filter", visibility_filter),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListMerchantCustomAttributeDefinitionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_merchant_custom_attributes(
        self,
        merchant_id: str,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMerchantCustomAttributesResponse, RawError]:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with a merchant. You can use the
        ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same call. When all
        response pages are retrieved, the results include all custom attributes that are visible to the requesting
        application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY`` or
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/merchants/{merchant_id}/custom-attributes"),
            path_params=[param[str]("merchant_id", merchant_id)],
            query_params=[
                param[VisibilityFilterOrStr | None]("visibility_filter", visibility_filter),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("with_definitions", with_definitions),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListMerchantCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_merchant_custom_attribute(
        self,
        merchant_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveMerchantCustomAttributeResponse, RawError]:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with a merchant. You can use the
        ``with_definition`` query parameter to also retrieve the custom attribute definition in the same call. To
        retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
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
            url_template=self._server.default("/v2/merchants/{merchant_id}/custom-attributes/{key}"),
            path_params=[param[str]("merchant_id", merchant_id), param[str]("key", key)],
            query_params=[
                param[bool | None]("with_definition", with_definition), param[int | None]("version", version)
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveMerchantCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_merchant_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveMerchantCustomAttributeDefinitionResponse, RawError]:
        """Retrieves a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. To retrieve a custom attribute definition created by another application, the ``visibility``
        setting must be ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

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
            url_template=self._server.default("/v2/merchants/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            query_params=[param[int | None]("version", version)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveMerchantCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_merchant_custom_attribute_definition(
        self,
        key: str,
        body: UpdateMerchantCustomAttributeDefinitionRequest | UpdateMerchantCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateMerchantCustomAttributeDefinitionResponse, RawError]:
        """Updates a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to update the following fields: ``name``, ``description``, ``visibility``, or
        the ``schema`` for a ``Selection`` data type. Only the definition owner can update a custom attribute
        definition.

        Args:
            key: The key of the custom attribute definition to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/merchants/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            body=json_body[
                UpdateMerchantCustomAttributeDefinitionRequest | UpdateMerchantCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateMerchantCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def upsert_merchant_custom_attribute(
        self,
        merchant_id: str,
        key: str,
        body: UpsertMerchantCustomAttributeRequest | UpsertMerchantCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpsertMerchantCustomAttributeResponse, RawError]:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for a merchant. Use this endpoint to set
        the value of a custom attribute for a specified merchant. A custom attribute is based on a custom attribute
        definition in a Square seller account, which is created using the `CreateMerchantCustomAttributeDefinition
        <api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition>`__ endpoint. To create or update
        a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
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
            url_template=self._server.default("/v2/merchants/{merchant_id}/custom-attributes/{key}"),
            path_params=[param[str]("merchant_id", merchant_id), param[str]("key", key)],
            body=json_body[UpsertMerchantCustomAttributeRequest | UpsertMerchantCustomAttributeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpsertMerchantCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncMerchantCustomAttributesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bulk_delete_merchant_custom_attributes(
        self,
        body: BulkDeleteMerchantCustomAttributesRequest | BulkDeleteMerchantCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkDeleteMerchantCustomAttributesResponse, RawError]:
        """Deletes `custom attributes <entity:CustomAttribute>`__ for a merchant as a bulk operation. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/merchants/custom-attributes/bulk-delete"),
            body=json_body[BulkDeleteMerchantCustomAttributesRequest | BulkDeleteMerchantCustomAttributesRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkDeleteMerchantCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bulk_upsert_merchant_custom_attributes(
        self,
        body: BulkUpsertMerchantCustomAttributesRequest | BulkUpsertMerchantCustomAttributesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpsertMerchantCustomAttributesResponse, RawError]:
        """Creates or updates `custom attributes <entity:CustomAttribute>`__ for a merchant as a bulk operation. Use
        this endpoint to set the value of one or more custom attributes for a merchant. A custom attribute is based on a
        custom attribute definition in a Square seller account, which is created using the
        `CreateMerchantCustomAttributeDefinition
        <api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition>`__ endpoint. This
        ``BulkUpsertMerchantCustomAttributes`` endpoint accepts a map of 1 to 25 individual upsert requests and returns
        a map of individual upsert responses. Each upsert request has a unique ID and provides a merchant ID and custom
        attribute. Each upsert response is returned with the ID of the corresponding request. To create or update a
        custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/merchants/custom-attributes/bulk-upsert"),
            body=json_body[BulkUpsertMerchantCustomAttributesRequest | BulkUpsertMerchantCustomAttributesRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkUpsertMerchantCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_merchant_custom_attribute_definition(
        self,
        body: CreateMerchantCustomAttributeDefinitionRequest | CreateMerchantCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateMerchantCustomAttributeDefinitionResponse, RawError]:
        """Creates a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to define a custom attribute that can be associated with a merchant connecting
        to your application. A custom attribute definition specifies the ``key``, ``visibility``, ``schema``, and other
        properties for a custom attribute. After the definition is created, you can call `UpsertMerchantCustomAttribute
        <api-endpoint:MerchantCustomAttributes-UpsertMerchantCustomAttribute>`__ or `BulkUpsertMerchantCustomAttributes
        <api-endpoint:MerchantCustomAttributes-BulkUpsertMerchantCustomAttributes>`__ to set the custom attribute for a
        merchant.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/merchants/custom-attribute-definitions"),
            body=json_body[
                CreateMerchantCustomAttributeDefinitionRequest | CreateMerchantCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateMerchantCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_merchant_custom_attribute(
        self, merchant_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteMerchantCustomAttributeResponse, RawError]:
        """Deletes a `custom attribute <entity:CustomAttribute>`__ associated with a merchant. To delete a custom
        attribute owned by another application, the ``visibility`` setting must be ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
            key: The key of the custom attribute to delete. This key must match the ``key`` of a custom attribute
                definition in the Square seller account. If the requesting application is not the definition owner, you
                must use the qualified key.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/merchants/{merchant_id}/custom-attributes/{key}"),
            path_params=[param[str]("merchant_id", merchant_id), param[str]("key", key)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteMerchantCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_merchant_custom_attribute_definition(
        self, key: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteMerchantCustomAttributeDefinitionResponse, RawError]:
        """Deletes a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. Deleting a custom attribute definition also deletes the corresponding custom attribute from the
        merchant. Only the definition owner can delete a custom attribute definition.

        Args:
            key: The key of the custom attribute definition to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/merchants/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteMerchantCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_merchant_custom_attribute_definitions(
        self,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMerchantCustomAttributeDefinitionsResponse, RawError]:
        """Lists the merchant-related `custom attribute definitions <entity:CustomAttributeDefinition>`__ that belong to
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/merchants/custom-attribute-definitions"),
            query_params=[
                param[VisibilityFilterOrStr | None]("visibility_filter", visibility_filter),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListMerchantCustomAttributeDefinitionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_merchant_custom_attributes(
        self,
        merchant_id: str,
        *,
        visibility_filter: VisibilityFilterOrStr | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        with_definitions: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListMerchantCustomAttributesResponse, RawError]:
        """Lists the `custom attributes <entity:CustomAttribute>`__ associated with a merchant. You can use the
        ``with_definitions`` query parameter to also retrieve custom attribute definitions in the same call. When all
        response pages are retrieved, the results include all custom attributes that are visible to the requesting
        application, including those that are owned by other applications and set to ``VISIBILITY_READ_ONLY`` or
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
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
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/merchants/{merchant_id}/custom-attributes"),
            path_params=[param[str]("merchant_id", merchant_id)],
            query_params=[
                param[VisibilityFilterOrStr | None]("visibility_filter", visibility_filter),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("with_definitions", with_definitions),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListMerchantCustomAttributesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_merchant_custom_attribute(
        self,
        merchant_id: str,
        key: str,
        *,
        with_definition: bool | None = False,
        version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveMerchantCustomAttributeResponse, RawError]:
        """Retrieves a `custom attribute <entity:CustomAttribute>`__ associated with a merchant. You can use the
        ``with_definition`` query parameter to also retrieve the custom attribute definition in the same call. To
        retrieve a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
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
            url_template=self._server.default("/v2/merchants/{merchant_id}/custom-attributes/{key}"),
            path_params=[param[str]("merchant_id", merchant_id), param[str]("key", key)],
            query_params=[
                param[bool | None]("with_definition", with_definition), param[int | None]("version", version)
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveMerchantCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_merchant_custom_attribute_definition(
        self, key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveMerchantCustomAttributeDefinitionResponse, RawError]:
        """Retrieves a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ from a Square
        seller account. To retrieve a custom attribute definition created by another application, the ``visibility``
        setting must be ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

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
            url_template=self._server.default("/v2/merchants/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            query_params=[param[int | None]("version", version)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveMerchantCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_merchant_custom_attribute_definition(
        self,
        key: str,
        body: UpdateMerchantCustomAttributeDefinitionRequest | UpdateMerchantCustomAttributeDefinitionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateMerchantCustomAttributeDefinitionResponse, RawError]:
        """Updates a merchant-related `custom attribute definition <entity:CustomAttributeDefinition>`__ for a Square
        seller account. Use this endpoint to update the following fields: ``name``, ``description``, ``visibility``, or
        the ``schema`` for a ``Selection`` data type. Only the definition owner can update a custom attribute
        definition.

        Args:
            key: The key of the custom attribute definition to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/merchants/custom-attribute-definitions/{key}"),
            path_params=[param[str]("key", key)],
            body=json_body[
                UpdateMerchantCustomAttributeDefinitionRequest | UpdateMerchantCustomAttributeDefinitionRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateMerchantCustomAttributeDefinitionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def upsert_merchant_custom_attribute(
        self,
        merchant_id: str,
        key: str,
        body: UpsertMerchantCustomAttributeRequest | UpsertMerchantCustomAttributeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpsertMerchantCustomAttributeResponse, RawError]:
        """Creates or updates a `custom attribute <entity:CustomAttribute>`__ for a merchant. Use this endpoint to set
        the value of a custom attribute for a specified merchant. A custom attribute is based on a custom attribute
        definition in a Square seller account, which is created using the `CreateMerchantCustomAttributeDefinition
        <api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition>`__ endpoint. To create or update
        a custom attribute owned by another application, the ``visibility`` setting must be
        ``VISIBILITY_READ_WRITE_VALUES``.

        Args:
            merchant_id: The ID of the target `merchant <entity:Merchant>`__.
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
            url_template=self._server.default("/v2/merchants/{merchant_id}/custom-attributes/{key}"),
            path_params=[param[str]("merchant_id", merchant_id), param[str]("key", key)],
            body=json_body[UpsertMerchantCustomAttributeRequest | UpsertMerchantCustomAttributeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpsertMerchantCustomAttributeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
