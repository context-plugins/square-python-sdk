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
    multipart_body,
    param,
    raw_error_response,
)
from ..models.batch_delete_catalog_objects_request import (
    BatchDeleteCatalogObjectsRequest,
    BatchDeleteCatalogObjectsRequestDict,
)
from ..models.batch_delete_catalog_objects_response import BatchDeleteCatalogObjectsResponse
from ..models.batch_retrieve_catalog_objects_request import (
    BatchRetrieveCatalogObjectsRequest,
    BatchRetrieveCatalogObjectsRequestDict,
)
from ..models.batch_retrieve_catalog_objects_response import BatchRetrieveCatalogObjectsResponse
from ..models.batch_upsert_catalog_objects_request import (
    BatchUpsertCatalogObjectsRequest,
    BatchUpsertCatalogObjectsRequestDict,
)
from ..models.batch_upsert_catalog_objects_response import BatchUpsertCatalogObjectsResponse
from ..models.catalog_info_response import CatalogInfoResponse
from ..models.create_catalog_image_request import CreateCatalogImageRequest, CreateCatalogImageRequestDict
from ..models.create_catalog_image_response import CreateCatalogImageResponse
from ..models.delete_catalog_object_response import DeleteCatalogObjectResponse
from ..models.list_catalog_response import ListCatalogResponse
from ..models.retrieve_catalog_object_response import RetrieveCatalogObjectResponse
from ..models.search_catalog_items_request import SearchCatalogItemsRequest, SearchCatalogItemsRequestDict
from ..models.search_catalog_items_response import SearchCatalogItemsResponse
from ..models.search_catalog_objects_request import SearchCatalogObjectsRequest, SearchCatalogObjectsRequestDict
from ..models.search_catalog_objects_response import SearchCatalogObjectsResponse
from ..models.update_catalog_image_request import UpdateCatalogImageRequest, UpdateCatalogImageRequestDict
from ..models.update_catalog_image_response import UpdateCatalogImageResponse
from ..models.update_item_modifier_lists_request import (
    UpdateItemModifierListsRequest,
    UpdateItemModifierListsRequestDict,
)
from ..models.update_item_modifier_lists_response import UpdateItemModifierListsResponse
from ..models.update_item_taxes_request import UpdateItemTaxesRequest, UpdateItemTaxesRequestDict
from ..models.update_item_taxes_response import UpdateItemTaxesResponse
from ..models.upsert_catalog_object_request import UpsertCatalogObjectRequest, UpsertCatalogObjectRequestDict
from ..models.upsert_catalog_object_response import UpsertCatalogObjectResponse
from ..server.server import Server


class Catalog:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CatalogWithRawResponse(client, server, auth)

    def batch_delete_catalog_objects(
        self,
        body: BatchDeleteCatalogObjectsRequest | BatchDeleteCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchDeleteCatalogObjectsResponse:
        """Deletes a set of `CatalogItem <entity:CatalogItem>`__s based on the provided list of target IDs and returns a
        set of successfully deleted IDs in the response. Deletion is a cascading event such that all children of the
        targeted object are also deleted. For example, deleting a CatalogItem will also delete all of its
        `CatalogItemVariation <entity:CatalogItemVariation>`__ children.

        ``BatchDeleteCatalogObjects`` succeeds even if only a portion of the targeted IDs can be deleted. The response
        will only include IDs that were actually deleted.

        To ensure consistency, only one delete request is processed at a time per seller account. While one (batch or
        non-batch) delete request is being processed, other (batched and non-batched) delete requests are rejected with
        the ``429`` error code.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.batch_delete_catalog_objects(body, request_options=request_options).unwrap()

    def batch_retrieve_catalog_objects(
        self,
        body: BatchRetrieveCatalogObjectsRequest | BatchRetrieveCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchRetrieveCatalogObjectsResponse:
        """Returns a set of objects based on the provided ID. Each `CatalogItem <entity:CatalogItem>`__ returned in the
        set includes all of its child information including: all of its `CatalogItemVariation
        <entity:CatalogItemVariation>`__ objects, references to its `CatalogModifierList <entity:CatalogModifierList>`__
        objects, and the ids of any `CatalogTax <entity:CatalogTax>`__ objects that apply to it.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.batch_retrieve_catalog_objects(body, request_options=request_options).unwrap()

    def batch_upsert_catalog_objects(
        self,
        body: BatchUpsertCatalogObjectsRequest | BatchUpsertCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchUpsertCatalogObjectsResponse:
        """Creates or updates up to 10,000 target objects based on the provided list of objects. The target objects are
        grouped into batches and each batch is inserted/updated in an all-or-nothing manner. If an object within a batch
        is malformed in some way, or violates a database constraint, the entire batch containing that item will be
        disregarded. However, other batches in the same request may still succeed. Each batch may contain up to 1,000
        objects, and batches will be processed in order as long as the total object count for the request (items,
        variations, modifier lists, discounts, and taxes) is no more than 10,000.

        This endpoint uses full-replacement semantics. The client must send the complete object, and any field absent
        from the request is interpreted as an intentional clear. This logic applies to nested objects as well. For
        example, omitting inlined children like variations will delete them.

        To ensure consistency, only one update request is processed at a time per seller account. While one (batch or
        non-batch) update request is being processed, other (batched and non-batched) update requests are rejected with
        the ``429`` error code. Prefer batching related changes into a single call rather than issuing many small
        writes, since each write acquires the lock separately and parallel writes to the same seller will contend with
        each other, producing ``429`` errors.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.batch_upsert_catalog_objects(body, request_options=request_options).unwrap()

    def catalog_info(self, *, request_options: RequestOptionsOrDict | None = None) -> CatalogInfoResponse:
        """Retrieves information about the Square Catalog API, such as batch size limits that can be used by the
        ``BatchUpsertCatalogObjects`` endpoint.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.catalog_info(request_options=request_options).unwrap()

    def create_catalog_image(
        self,
        *,
        request: CreateCatalogImageRequest | CreateCatalogImageRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCatalogImageResponse:
        """Uploads an image file to be represented by a `CatalogImage <entity:CatalogImage>`__ object that can be linked
        to an existing `CatalogObject <entity:CatalogObject>`__ instance. The resulting ``CatalogImage`` is unattached
        to any ``CatalogObject`` if the ``object_id`` is not specified.

        This ``CreateCatalogImage`` endpoint accepts HTTP multipart/form-data requests with a JSON part and an image
        file part in JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.

        Args:
            request: Value sent with the request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_catalog_image(
            request=request, image_file=image_file, request_options=request_options
        ).unwrap()

    def delete_catalog_object(
        self, object_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteCatalogObjectResponse:
        """Deletes a single `CatalogObject <entity:CatalogObject>`__ based on the provided ID and returns the set of
        successfully deleted IDs in the response. Deletion is a cascading event such that all children of the targeted
        object are also deleted. For example, deleting a `CatalogItem <entity:CatalogItem>`__ will also delete all of
        its `CatalogItemVariation <entity:CatalogItemVariation>`__ children.

        To ensure consistency, only one delete request is processed at a time per seller account. While one (batch or
        non-batch) delete request is being processed, other (batched and non-batched) delete requests are rejected with
        the ``429`` error code.

        Args:
            object_id: The ID of the catalog object to be deleted. When an object is deleted, other objects in the graph
                that depend on that object will be deleted as well (for example, deleting a catalog item will delete its
                catalog item variations).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_catalog_object(object_id, request_options=request_options).unwrap()

    def list_catalog(
        self,
        *,
        cursor: str | None = None,
        types: str | None = None,
        catalog_version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCatalogResponse:
        """Returns a list of all `CatalogObject <entity:CatalogObject>`__s of the specified types in the catalog.

        The ``types`` parameter is specified as a comma-separated list of the `CatalogObjectType
        <entity:CatalogObjectType>`__ values, for example, "``ITEM``, ``ITEM_VARIATION``, ``MODIFIER``,
        ``MODIFIER_LIST``, ``CATEGORY``, ``DISCOUNT``, ``TAX``, ``IMAGE``". Always specify ``types`` explicitly. When
        upgrading to a newer API version, omitting ``types`` may cause new object types to appear in results that were
        not returned under the previous version.

        __Important:__ ListCatalog does not return deleted catalog items. To retrieve deleted catalog items, use
        `SearchCatalogObjects <api-endpoint:Catalog-SearchCatalogObjects>`__ and set the ``include_deleted_objects``
        attribute value to ``true``.

        Args:
            cursor: The pagination cursor returned in the previous response. Leave unset for an initial request. The
                page size is currently set to be 100. See `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more
                information.
            types: An optional case-insensitive, comma-separated list of object types to retrieve. The valid values are
                defined in the `CatalogObjectType <entity:CatalogObjectType>`__ enum, for example, ``ITEM``,
                ``ITEM_VARIATION``, ``CATEGORY``, ``DISCOUNT``, ``TAX``, ``MODIFIER``, ``MODIFIER_LIST``, ``IMAGE``,
                etc. If this is unspecified, the operation returns objects of all the top level types at the version of
                the Square API used to make the request. Object types that are nested onto other object types are not
                included in the defaults. At the current API version the default object types are: ITEM, CATEGORY, TAX,
                DISCOUNT, MODIFIER_LIST, PRICING_RULE, PRODUCT_SET, TIME_PERIOD, MEASUREMENT_UNIT, SUBSCRIPTION_PLAN,
                ITEM_OPTION, CUSTOM_ATTRIBUTE_DEFINITION, QUICK_AMOUNT_SETTINGS.
            catalog_version: The specific version of the catalog objects to be included in the response. This allows you
                to retrieve historical versions of objects. The specified version value is matched against the
                `CatalogObject <entity:CatalogObject>`__s' ``version`` attribute. If not included, results will be from
                the current version of the catalog.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_catalog(
            cursor=cursor, types=types, catalog_version=catalog_version, request_options=request_options
        ).unwrap()

    def retrieve_catalog_object(
        self,
        object_id: str,
        *,
        include_related_objects: bool | None = False,
        catalog_version: int | None = None,
        include_category_path_to_root: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveCatalogObjectResponse:
        """Returns a single `CatalogItem <entity:CatalogItem>`__ as a `CatalogObject <entity:CatalogObject>`__ based on
        the provided ID. The returned object includes all of the relevant `CatalogItem <entity:CatalogItem>`__
        information including: `CatalogItemVariation <entity:CatalogItemVariation>`__ children, references to its
        `CatalogModifierList <entity:CatalogModifierList>`__ objects, and the ids of any `CatalogTax
        <entity:CatalogTax>`__ objects that apply to it.

        Args:
            object_id: The object ID of any type of catalog objects to be retrieved.
            include_related_objects: If ``true``, the response will include additional objects that are related to the
                requested objects. Related objects are defined as any objects referenced by ID by the results in the
                ``objects`` field of the response. These objects are put in the ``related_objects`` field. Setting this
                to ``true`` is helpful when the objects are needed for immediate display to a user. This process only
                goes one level deep. Objects referenced by the related objects will not be included. For example, if the
                ``objects`` field of the response contains a CatalogItem, its associated CatalogCategory objects,
                CatalogTax objects, CatalogImage objects and CatalogModifierLists will be returned in the
                ``related_objects`` field of the response. If the ``objects`` field of the response contains a
                CatalogItemVariation, its parent CatalogItem will be returned in the ``related_objects`` field of the
                response. Default value: ``false``
            catalog_version: Requests objects as of a specific version of the catalog. This allows you to retrieve
                historical versions of objects. The value to retrieve a specific version of an object can be found in
                the version field of `CatalogObject <entity:CatalogObject>`__s. If not included, results will be from
                the current version of the catalog.
            include_category_path_to_root: Specifies whether or not to include the ``path_to_root`` list for each
                returned category instance. The ``path_to_root`` list consists of ``CategoryPathToRootNode`` objects and
                specifies the path that starts with the immediate parent category of the returned category and ends with
                its root category. If the returned category is a top-level category, the ``path_to_root`` list is empty
                and is not returned in the response payload.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_catalog_object(
            object_id,
            include_related_objects=include_related_objects,
            catalog_version=catalog_version,
            include_category_path_to_root=include_category_path_to_root,
            request_options=request_options,
        ).unwrap()

    def search_catalog_items(
        self,
        body: SearchCatalogItemsRequest | SearchCatalogItemsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchCatalogItemsResponse:
        """Searches for catalog items or item variations by matching supported search attribute values, including custom
        attribute values, against one or more of the specified query filters.

        This (``SearchCatalogItems``) endpoint differs from the `SearchCatalogObjects
        <api-endpoint:Catalog-SearchCatalogObjects>`__ endpoint in the following aspects:

        - ``SearchCatalogItems`` can only search for items or item variations, whereas ``SearchCatalogObjects`` can
            search for any type of catalog objects.
        - ``SearchCatalogItems`` supports the custom attribute query filters to return items or item variations that
            contain custom attribute values, where ``SearchCatalogObjects`` does not.
        - ``SearchCatalogItems`` does not support the ``include_deleted_objects`` filter to search for deleted items or
            item variations, whereas ``SearchCatalogObjects`` does.
        - The both endpoints use different call conventions, including the query filter formats.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_catalog_items(body, request_options=request_options).unwrap()

    def search_catalog_objects(
        self,
        body: SearchCatalogObjectsRequest | SearchCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchCatalogObjectsResponse:
        """Searches for `CatalogObject <entity:CatalogObject>`__ of any type by matching supported search attribute
        values, excluding custom attribute values on items or item variations, against one or more of the specified
        query filters.

        This (``SearchCatalogObjects``) endpoint differs from the `SearchCatalogItems
        <api-endpoint:Catalog-SearchCatalogItems>`__ endpoint in the following aspects:

        - ``SearchCatalogItems`` can only search for items or item variations, whereas ``SearchCatalogObjects`` can
            search for any type of catalog objects.
        - ``SearchCatalogItems`` supports the custom attribute query filters to return items or item variations that
            contain custom attribute values, where ``SearchCatalogObjects`` does not.
        - ``SearchCatalogItems`` does not support the ``include_deleted_objects`` filter to search for deleted items or
            item variations, whereas ``SearchCatalogObjects`` does.
        - The both endpoints have different call conventions, including the query filter formats.

        The ``object_types`` parameter is specified as a list of `CatalogObjectType <entity:CatalogObjectType>`__
        values. Always specify ``object_types`` explicitly. When upgrading to a newer API version, omitting
        ``object_types`` may cause new object types to appear in results that were not returned under the previous
        version.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_catalog_objects(body, request_options=request_options).unwrap()

    def update_catalog_image(
        self,
        image_id: str,
        *,
        request: UpdateCatalogImageRequest | UpdateCatalogImageRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateCatalogImageResponse:
        """Uploads a new image file to replace the existing one in the specified `CatalogImage <entity:CatalogImage>`__
        object.

        This ``UpdateCatalogImage`` endpoint accepts HTTP multipart/form-data requests with a JSON part and an image
        file part in JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.

        Args:
            image_id: The ID of the ``CatalogImage`` object to update the encapsulated image file.
            request: Value sent with the request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_catalog_image(
            image_id, request=request, image_file=image_file, request_options=request_options
        ).unwrap()

    def update_item_modifier_lists(
        self,
        body: UpdateItemModifierListsRequest | UpdateItemModifierListsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateItemModifierListsResponse:
        """Updates the `CatalogModifierList <entity:CatalogModifierList>`__ objects that apply to the targeted
        `CatalogItem <entity:CatalogItem>`__ without having to perform an upsert on the entire item.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_item_modifier_lists(body, request_options=request_options).unwrap()

    def update_item_taxes(
        self,
        body: UpdateItemTaxesRequest | UpdateItemTaxesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateItemTaxesResponse:
        """Updates the `CatalogTax <entity:CatalogTax>`__ objects that apply to the targeted `CatalogItem
        <entity:CatalogItem>`__ without having to perform an upsert on the entire item.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_item_taxes(body, request_options=request_options).unwrap()

    def upsert_catalog_object(
        self,
        body: UpsertCatalogObjectRequest | UpsertCatalogObjectRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpsertCatalogObjectResponse:
        """Creates a new or updates the specified `CatalogObject <entity:CatalogObject>`__.

        This endpoint uses full-replacement semantics. The client must send the complete object, and any field absent
        from the request is interpreted as an intentional clear. This logic applies to nested objects as well. For
        example, omitting inlined children like variations will delete them.

        To ensure consistency, only one update request is processed at a time per seller account. While one (batch or
        non-batch) update request is being processed, other (batched and non-batched) update requests are rejected with
        the ``429`` error code.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.upsert_catalog_object(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CatalogWithRawResponse:
        return self._with_raw_response


class AsyncCatalog:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCatalogWithRawResponse(client, server, auth)

    async def batch_delete_catalog_objects(
        self,
        body: BatchDeleteCatalogObjectsRequest | BatchDeleteCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchDeleteCatalogObjectsResponse:
        """Deletes a set of `CatalogItem <entity:CatalogItem>`__s based on the provided list of target IDs and returns a
        set of successfully deleted IDs in the response. Deletion is a cascading event such that all children of the
        targeted object are also deleted. For example, deleting a CatalogItem will also delete all of its
        `CatalogItemVariation <entity:CatalogItemVariation>`__ children.

        ``BatchDeleteCatalogObjects`` succeeds even if only a portion of the targeted IDs can be deleted. The response
        will only include IDs that were actually deleted.

        To ensure consistency, only one delete request is processed at a time per seller account. While one (batch or
        non-batch) delete request is being processed, other (batched and non-batched) delete requests are rejected with
        the ``429`` error code.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.batch_delete_catalog_objects(body, request_options=request_options)
        ).unwrap()

    async def batch_retrieve_catalog_objects(
        self,
        body: BatchRetrieveCatalogObjectsRequest | BatchRetrieveCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchRetrieveCatalogObjectsResponse:
        """Returns a set of objects based on the provided ID. Each `CatalogItem <entity:CatalogItem>`__ returned in the
        set includes all of its child information including: all of its `CatalogItemVariation
        <entity:CatalogItemVariation>`__ objects, references to its `CatalogModifierList <entity:CatalogModifierList>`__
        objects, and the ids of any `CatalogTax <entity:CatalogTax>`__ objects that apply to it.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.batch_retrieve_catalog_objects(body, request_options=request_options)
        ).unwrap()

    async def batch_upsert_catalog_objects(
        self,
        body: BatchUpsertCatalogObjectsRequest | BatchUpsertCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchUpsertCatalogObjectsResponse:
        """Creates or updates up to 10,000 target objects based on the provided list of objects. The target objects are
        grouped into batches and each batch is inserted/updated in an all-or-nothing manner. If an object within a batch
        is malformed in some way, or violates a database constraint, the entire batch containing that item will be
        disregarded. However, other batches in the same request may still succeed. Each batch may contain up to 1,000
        objects, and batches will be processed in order as long as the total object count for the request (items,
        variations, modifier lists, discounts, and taxes) is no more than 10,000.

        This endpoint uses full-replacement semantics. The client must send the complete object, and any field absent
        from the request is interpreted as an intentional clear. This logic applies to nested objects as well. For
        example, omitting inlined children like variations will delete them.

        To ensure consistency, only one update request is processed at a time per seller account. While one (batch or
        non-batch) update request is being processed, other (batched and non-batched) update requests are rejected with
        the ``429`` error code. Prefer batching related changes into a single call rather than issuing many small
        writes, since each write acquires the lock separately and parallel writes to the same seller will contend with
        each other, producing ``429`` errors.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.batch_upsert_catalog_objects(body, request_options=request_options)
        ).unwrap()

    async def catalog_info(self, *, request_options: RequestOptionsOrDict | None = None) -> CatalogInfoResponse:
        """Retrieves information about the Square Catalog API, such as batch size limits that can be used by the
        ``BatchUpsertCatalogObjects`` endpoint.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.catalog_info(request_options=request_options)).unwrap()

    async def create_catalog_image(
        self,
        *,
        request: CreateCatalogImageRequest | CreateCatalogImageRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCatalogImageResponse:
        """Uploads an image file to be represented by a `CatalogImage <entity:CatalogImage>`__ object that can be linked
        to an existing `CatalogObject <entity:CatalogObject>`__ instance. The resulting ``CatalogImage`` is unattached
        to any ``CatalogObject`` if the ``object_id`` is not specified.

        This ``CreateCatalogImage`` endpoint accepts HTTP multipart/form-data requests with a JSON part and an image
        file part in JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.

        Args:
            request: Value sent with the request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_catalog_image(
                request=request, image_file=image_file, request_options=request_options
            )
        ).unwrap()

    async def delete_catalog_object(
        self, object_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteCatalogObjectResponse:
        """Deletes a single `CatalogObject <entity:CatalogObject>`__ based on the provided ID and returns the set of
        successfully deleted IDs in the response. Deletion is a cascading event such that all children of the targeted
        object are also deleted. For example, deleting a `CatalogItem <entity:CatalogItem>`__ will also delete all of
        its `CatalogItemVariation <entity:CatalogItemVariation>`__ children.

        To ensure consistency, only one delete request is processed at a time per seller account. While one (batch or
        non-batch) delete request is being processed, other (batched and non-batched) delete requests are rejected with
        the ``429`` error code.

        Args:
            object_id: The ID of the catalog object to be deleted. When an object is deleted, other objects in the graph
                that depend on that object will be deleted as well (for example, deleting a catalog item will delete its
                catalog item variations).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_catalog_object(object_id, request_options=request_options)
        ).unwrap()

    async def list_catalog(
        self,
        *,
        cursor: str | None = None,
        types: str | None = None,
        catalog_version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCatalogResponse:
        """Returns a list of all `CatalogObject <entity:CatalogObject>`__s of the specified types in the catalog.

        The ``types`` parameter is specified as a comma-separated list of the `CatalogObjectType
        <entity:CatalogObjectType>`__ values, for example, "``ITEM``, ``ITEM_VARIATION``, ``MODIFIER``,
        ``MODIFIER_LIST``, ``CATEGORY``, ``DISCOUNT``, ``TAX``, ``IMAGE``". Always specify ``types`` explicitly. When
        upgrading to a newer API version, omitting ``types`` may cause new object types to appear in results that were
        not returned under the previous version.

        __Important:__ ListCatalog does not return deleted catalog items. To retrieve deleted catalog items, use
        `SearchCatalogObjects <api-endpoint:Catalog-SearchCatalogObjects>`__ and set the ``include_deleted_objects``
        attribute value to ``true``.

        Args:
            cursor: The pagination cursor returned in the previous response. Leave unset for an initial request. The
                page size is currently set to be 100. See `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more
                information.
            types: An optional case-insensitive, comma-separated list of object types to retrieve. The valid values are
                defined in the `CatalogObjectType <entity:CatalogObjectType>`__ enum, for example, ``ITEM``,
                ``ITEM_VARIATION``, ``CATEGORY``, ``DISCOUNT``, ``TAX``, ``MODIFIER``, ``MODIFIER_LIST``, ``IMAGE``,
                etc. If this is unspecified, the operation returns objects of all the top level types at the version of
                the Square API used to make the request. Object types that are nested onto other object types are not
                included in the defaults. At the current API version the default object types are: ITEM, CATEGORY, TAX,
                DISCOUNT, MODIFIER_LIST, PRICING_RULE, PRODUCT_SET, TIME_PERIOD, MEASUREMENT_UNIT, SUBSCRIPTION_PLAN,
                ITEM_OPTION, CUSTOM_ATTRIBUTE_DEFINITION, QUICK_AMOUNT_SETTINGS.
            catalog_version: The specific version of the catalog objects to be included in the response. This allows you
                to retrieve historical versions of objects. The specified version value is matched against the
                `CatalogObject <entity:CatalogObject>`__s' ``version`` attribute. If not included, results will be from
                the current version of the catalog.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_catalog(
                cursor=cursor, types=types, catalog_version=catalog_version, request_options=request_options
            )
        ).unwrap()

    async def retrieve_catalog_object(
        self,
        object_id: str,
        *,
        include_related_objects: bool | None = False,
        catalog_version: int | None = None,
        include_category_path_to_root: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveCatalogObjectResponse:
        """Returns a single `CatalogItem <entity:CatalogItem>`__ as a `CatalogObject <entity:CatalogObject>`__ based on
        the provided ID. The returned object includes all of the relevant `CatalogItem <entity:CatalogItem>`__
        information including: `CatalogItemVariation <entity:CatalogItemVariation>`__ children, references to its
        `CatalogModifierList <entity:CatalogModifierList>`__ objects, and the ids of any `CatalogTax
        <entity:CatalogTax>`__ objects that apply to it.

        Args:
            object_id: The object ID of any type of catalog objects to be retrieved.
            include_related_objects: If ``true``, the response will include additional objects that are related to the
                requested objects. Related objects are defined as any objects referenced by ID by the results in the
                ``objects`` field of the response. These objects are put in the ``related_objects`` field. Setting this
                to ``true`` is helpful when the objects are needed for immediate display to a user. This process only
                goes one level deep. Objects referenced by the related objects will not be included. For example, if the
                ``objects`` field of the response contains a CatalogItem, its associated CatalogCategory objects,
                CatalogTax objects, CatalogImage objects and CatalogModifierLists will be returned in the
                ``related_objects`` field of the response. If the ``objects`` field of the response contains a
                CatalogItemVariation, its parent CatalogItem will be returned in the ``related_objects`` field of the
                response. Default value: ``false``
            catalog_version: Requests objects as of a specific version of the catalog. This allows you to retrieve
                historical versions of objects. The value to retrieve a specific version of an object can be found in
                the version field of `CatalogObject <entity:CatalogObject>`__s. If not included, results will be from
                the current version of the catalog.
            include_category_path_to_root: Specifies whether or not to include the ``path_to_root`` list for each
                returned category instance. The ``path_to_root`` list consists of ``CategoryPathToRootNode`` objects and
                specifies the path that starts with the immediate parent category of the returned category and ends with
                its root category. If the returned category is a top-level category, the ``path_to_root`` list is empty
                and is not returned in the response payload.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_catalog_object(
                object_id,
                include_related_objects=include_related_objects,
                catalog_version=catalog_version,
                include_category_path_to_root=include_category_path_to_root,
                request_options=request_options,
            )
        ).unwrap()

    async def search_catalog_items(
        self,
        body: SearchCatalogItemsRequest | SearchCatalogItemsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchCatalogItemsResponse:
        """Searches for catalog items or item variations by matching supported search attribute values, including custom
        attribute values, against one or more of the specified query filters.

        This (``SearchCatalogItems``) endpoint differs from the `SearchCatalogObjects
        <api-endpoint:Catalog-SearchCatalogObjects>`__ endpoint in the following aspects:

        - ``SearchCatalogItems`` can only search for items or item variations, whereas ``SearchCatalogObjects`` can
            search for any type of catalog objects.
        - ``SearchCatalogItems`` supports the custom attribute query filters to return items or item variations that
            contain custom attribute values, where ``SearchCatalogObjects`` does not.
        - ``SearchCatalogItems`` does not support the ``include_deleted_objects`` filter to search for deleted items or
            item variations, whereas ``SearchCatalogObjects`` does.
        - The both endpoints use different call conventions, including the query filter formats.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search_catalog_items(body, request_options=request_options)).unwrap()

    async def search_catalog_objects(
        self,
        body: SearchCatalogObjectsRequest | SearchCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchCatalogObjectsResponse:
        """Searches for `CatalogObject <entity:CatalogObject>`__ of any type by matching supported search attribute
        values, excluding custom attribute values on items or item variations, against one or more of the specified
        query filters.

        This (``SearchCatalogObjects``) endpoint differs from the `SearchCatalogItems
        <api-endpoint:Catalog-SearchCatalogItems>`__ endpoint in the following aspects:

        - ``SearchCatalogItems`` can only search for items or item variations, whereas ``SearchCatalogObjects`` can
            search for any type of catalog objects.
        - ``SearchCatalogItems`` supports the custom attribute query filters to return items or item variations that
            contain custom attribute values, where ``SearchCatalogObjects`` does not.
        - ``SearchCatalogItems`` does not support the ``include_deleted_objects`` filter to search for deleted items or
            item variations, whereas ``SearchCatalogObjects`` does.
        - The both endpoints have different call conventions, including the query filter formats.

        The ``object_types`` parameter is specified as a list of `CatalogObjectType <entity:CatalogObjectType>`__
        values. Always specify ``object_types`` explicitly. When upgrading to a newer API version, omitting
        ``object_types`` may cause new object types to appear in results that were not returned under the previous
        version.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search_catalog_objects(body, request_options=request_options)).unwrap()

    async def update_catalog_image(
        self,
        image_id: str,
        *,
        request: UpdateCatalogImageRequest | UpdateCatalogImageRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateCatalogImageResponse:
        """Uploads a new image file to replace the existing one in the specified `CatalogImage <entity:CatalogImage>`__
        object.

        This ``UpdateCatalogImage`` endpoint accepts HTTP multipart/form-data requests with a JSON part and an image
        file part in JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.

        Args:
            image_id: The ID of the ``CatalogImage`` object to update the encapsulated image file.
            request: Value sent with the request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_catalog_image(
                image_id, request=request, image_file=image_file, request_options=request_options
            )
        ).unwrap()

    async def update_item_modifier_lists(
        self,
        body: UpdateItemModifierListsRequest | UpdateItemModifierListsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateItemModifierListsResponse:
        """Updates the `CatalogModifierList <entity:CatalogModifierList>`__ objects that apply to the targeted
        `CatalogItem <entity:CatalogItem>`__ without having to perform an upsert on the entire item.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_item_modifier_lists(body, request_options=request_options)
        ).unwrap()

    async def update_item_taxes(
        self,
        body: UpdateItemTaxesRequest | UpdateItemTaxesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateItemTaxesResponse:
        """Updates the `CatalogTax <entity:CatalogTax>`__ objects that apply to the targeted `CatalogItem
        <entity:CatalogItem>`__ without having to perform an upsert on the entire item.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.update_item_taxes(body, request_options=request_options)).unwrap()

    async def upsert_catalog_object(
        self,
        body: UpsertCatalogObjectRequest | UpsertCatalogObjectRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpsertCatalogObjectResponse:
        """Creates a new or updates the specified `CatalogObject <entity:CatalogObject>`__.

        This endpoint uses full-replacement semantics. The client must send the complete object, and any field absent
        from the request is interpreted as an intentional clear. This logic applies to nested objects as well. For
        example, omitting inlined children like variations will delete them.

        To ensure consistency, only one update request is processed at a time per seller account. While one (batch or
        non-batch) update request is being processed, other (batched and non-batched) update requests are rejected with
        the ``429`` error code.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.upsert_catalog_object(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncCatalogWithRawResponse:
        return self._with_raw_response


class CatalogWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def batch_delete_catalog_objects(
        self,
        body: BatchDeleteCatalogObjectsRequest | BatchDeleteCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchDeleteCatalogObjectsResponse, RawError]:
        """Deletes a set of `CatalogItem <entity:CatalogItem>`__s based on the provided list of target IDs and returns a
        set of successfully deleted IDs in the response. Deletion is a cascading event such that all children of the
        targeted object are also deleted. For example, deleting a CatalogItem will also delete all of its
        `CatalogItemVariation <entity:CatalogItemVariation>`__ children.

        ``BatchDeleteCatalogObjects`` succeeds even if only a portion of the targeted IDs can be deleted. The response
        will only include IDs that were actually deleted.

        To ensure consistency, only one delete request is processed at a time per seller account. While one (batch or
        non-batch) delete request is being processed, other (batched and non-batched) delete requests are rejected with
        the ``429`` error code.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/batch-delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BatchDeleteCatalogObjectsRequest | BatchDeleteCatalogObjectsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchDeleteCatalogObjectsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def batch_retrieve_catalog_objects(
        self,
        body: BatchRetrieveCatalogObjectsRequest | BatchRetrieveCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchRetrieveCatalogObjectsResponse, RawError]:
        """Returns a set of objects based on the provided ID. Each `CatalogItem <entity:CatalogItem>`__ returned in the
        set includes all of its child information including: all of its `CatalogItemVariation
        <entity:CatalogItemVariation>`__ objects, references to its `CatalogModifierList <entity:CatalogModifierList>`__
        objects, and the ids of any `CatalogTax <entity:CatalogTax>`__ objects that apply to it.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/batch-retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BatchRetrieveCatalogObjectsRequest | BatchRetrieveCatalogObjectsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchRetrieveCatalogObjectsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def batch_upsert_catalog_objects(
        self,
        body: BatchUpsertCatalogObjectsRequest | BatchUpsertCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchUpsertCatalogObjectsResponse, RawError]:
        """Creates or updates up to 10,000 target objects based on the provided list of objects. The target objects are
        grouped into batches and each batch is inserted/updated in an all-or-nothing manner. If an object within a batch
        is malformed in some way, or violates a database constraint, the entire batch containing that item will be
        disregarded. However, other batches in the same request may still succeed. Each batch may contain up to 1,000
        objects, and batches will be processed in order as long as the total object count for the request (items,
        variations, modifier lists, discounts, and taxes) is no more than 10,000.

        This endpoint uses full-replacement semantics. The client must send the complete object, and any field absent
        from the request is interpreted as an intentional clear. This logic applies to nested objects as well. For
        example, omitting inlined children like variations will delete them.

        To ensure consistency, only one update request is processed at a time per seller account. While one (batch or
        non-batch) update request is being processed, other (batched and non-batched) update requests are rejected with
        the ``429`` error code. Prefer batching related changes into a single call rather than issuing many small
        writes, since each write acquires the lock separately and parallel writes to the same seller will contend with
        each other, producing ``429`` errors.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/batch-upsert"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BatchUpsertCatalogObjectsRequest | BatchUpsertCatalogObjectsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchUpsertCatalogObjectsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def catalog_info(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CatalogInfoResponse, RawError]:
        """Retrieves information about the Square Catalog API, such as batch size limits that can be used by the
        ``BatchUpsertCatalogObjects`` endpoint.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/catalog/info"),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CatalogInfoResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_catalog_image(
        self,
        *,
        request: CreateCatalogImageRequest | CreateCatalogImageRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCatalogImageResponse, RawError]:
        """Uploads an image file to be represented by a `CatalogImage <entity:CatalogImage>`__ object that can be linked
        to an existing `CatalogObject <entity:CatalogObject>`__ instance. The resulting ``CatalogImage`` is unattached
        to any ``CatalogObject`` if the ``object_id`` is not specified.

        This ``CreateCatalogImage`` endpoint accepts HTTP multipart/form-data requests with a JSON part and an image
        file part in JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.

        Args:
            request: Value sent with the request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/images"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                [param[CreateCatalogImageRequest | CreateCatalogImageRequestDict | None]("request", request)],
                {"image_file": image_file},
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateCatalogImageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_catalog_object(
        self, object_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteCatalogObjectResponse, RawError]:
        """Deletes a single `CatalogObject <entity:CatalogObject>`__ based on the provided ID and returns the set of
        successfully deleted IDs in the response. Deletion is a cascading event such that all children of the targeted
        object are also deleted. For example, deleting a `CatalogItem <entity:CatalogItem>`__ will also delete all of
        its `CatalogItemVariation <entity:CatalogItemVariation>`__ children.

        To ensure consistency, only one delete request is processed at a time per seller account. While one (batch or
        non-batch) delete request is being processed, other (batched and non-batched) delete requests are rejected with
        the ``429`` error code.

        Args:
            object_id: The ID of the catalog object to be deleted. When an object is deleted, other objects in the graph
                that depend on that object will be deleted as well (for example, deleting a catalog item will delete its
                catalog item variations).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/catalog/object/{object_id}"),
            path_params=[param[str]("object_id", object_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteCatalogObjectResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_catalog(
        self,
        *,
        cursor: str | None = None,
        types: str | None = None,
        catalog_version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCatalogResponse, RawError]:
        """Returns a list of all `CatalogObject <entity:CatalogObject>`__s of the specified types in the catalog.

        The ``types`` parameter is specified as a comma-separated list of the `CatalogObjectType
        <entity:CatalogObjectType>`__ values, for example, "``ITEM``, ``ITEM_VARIATION``, ``MODIFIER``,
        ``MODIFIER_LIST``, ``CATEGORY``, ``DISCOUNT``, ``TAX``, ``IMAGE``". Always specify ``types`` explicitly. When
        upgrading to a newer API version, omitting ``types`` may cause new object types to appear in results that were
        not returned under the previous version.

        __Important:__ ListCatalog does not return deleted catalog items. To retrieve deleted catalog items, use
        `SearchCatalogObjects <api-endpoint:Catalog-SearchCatalogObjects>`__ and set the ``include_deleted_objects``
        attribute value to ``true``.

        Args:
            cursor: The pagination cursor returned in the previous response. Leave unset for an initial request. The
                page size is currently set to be 100. See `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more
                information.
            types: An optional case-insensitive, comma-separated list of object types to retrieve. The valid values are
                defined in the `CatalogObjectType <entity:CatalogObjectType>`__ enum, for example, ``ITEM``,
                ``ITEM_VARIATION``, ``CATEGORY``, ``DISCOUNT``, ``TAX``, ``MODIFIER``, ``MODIFIER_LIST``, ``IMAGE``,
                etc. If this is unspecified, the operation returns objects of all the top level types at the version of
                the Square API used to make the request. Object types that are nested onto other object types are not
                included in the defaults. At the current API version the default object types are: ITEM, CATEGORY, TAX,
                DISCOUNT, MODIFIER_LIST, PRICING_RULE, PRODUCT_SET, TIME_PERIOD, MEASUREMENT_UNIT, SUBSCRIPTION_PLAN,
                ITEM_OPTION, CUSTOM_ATTRIBUTE_DEFINITION, QUICK_AMOUNT_SETTINGS.
            catalog_version: The specific version of the catalog objects to be included in the response. This allows you
                to retrieve historical versions of objects. The specified version value is matched against the
                `CatalogObject <entity:CatalogObject>`__s' ``version`` attribute. If not included, results will be from
                the current version of the catalog.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/catalog/list"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[str | None]("types", types),
                param[int | None]("catalog_version", catalog_version),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCatalogResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_catalog_object(
        self,
        object_id: str,
        *,
        include_related_objects: bool | None = False,
        catalog_version: int | None = None,
        include_category_path_to_root: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveCatalogObjectResponse, RawError]:
        """Returns a single `CatalogItem <entity:CatalogItem>`__ as a `CatalogObject <entity:CatalogObject>`__ based on
        the provided ID. The returned object includes all of the relevant `CatalogItem <entity:CatalogItem>`__
        information including: `CatalogItemVariation <entity:CatalogItemVariation>`__ children, references to its
        `CatalogModifierList <entity:CatalogModifierList>`__ objects, and the ids of any `CatalogTax
        <entity:CatalogTax>`__ objects that apply to it.

        Args:
            object_id: The object ID of any type of catalog objects to be retrieved.
            include_related_objects: If ``true``, the response will include additional objects that are related to the
                requested objects. Related objects are defined as any objects referenced by ID by the results in the
                ``objects`` field of the response. These objects are put in the ``related_objects`` field. Setting this
                to ``true`` is helpful when the objects are needed for immediate display to a user. This process only
                goes one level deep. Objects referenced by the related objects will not be included. For example, if the
                ``objects`` field of the response contains a CatalogItem, its associated CatalogCategory objects,
                CatalogTax objects, CatalogImage objects and CatalogModifierLists will be returned in the
                ``related_objects`` field of the response. If the ``objects`` field of the response contains a
                CatalogItemVariation, its parent CatalogItem will be returned in the ``related_objects`` field of the
                response. Default value: ``false``
            catalog_version: Requests objects as of a specific version of the catalog. This allows you to retrieve
                historical versions of objects. The value to retrieve a specific version of an object can be found in
                the version field of `CatalogObject <entity:CatalogObject>`__s. If not included, results will be from
                the current version of the catalog.
            include_category_path_to_root: Specifies whether or not to include the ``path_to_root`` list for each
                returned category instance. The ``path_to_root`` list consists of ``CategoryPathToRootNode`` objects and
                specifies the path that starts with the immediate parent category of the returned category and ends with
                its root category. If the returned category is a top-level category, the ``path_to_root`` list is empty
                and is not returned in the response payload.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/catalog/object/{object_id}"),
            path_params=[param[str]("object_id", object_id)],
            query_params=[
                param[bool | None]("include_related_objects", include_related_objects),
                param[int | None]("catalog_version", catalog_version),
                param[bool | None]("include_category_path_to_root", include_category_path_to_root),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveCatalogObjectResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_catalog_items(
        self,
        body: SearchCatalogItemsRequest | SearchCatalogItemsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchCatalogItemsResponse, RawError]:
        """Searches for catalog items or item variations by matching supported search attribute values, including custom
        attribute values, against one or more of the specified query filters.

        This (``SearchCatalogItems``) endpoint differs from the `SearchCatalogObjects
        <api-endpoint:Catalog-SearchCatalogObjects>`__ endpoint in the following aspects:

        - ``SearchCatalogItems`` can only search for items or item variations, whereas ``SearchCatalogObjects`` can
            search for any type of catalog objects.
        - ``SearchCatalogItems`` supports the custom attribute query filters to return items or item variations that
            contain custom attribute values, where ``SearchCatalogObjects`` does not.
        - ``SearchCatalogItems`` does not support the ``include_deleted_objects`` filter to search for deleted items or
            item variations, whereas ``SearchCatalogObjects`` does.
        - The both endpoints use different call conventions, including the query filter formats.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/search-catalog-items"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchCatalogItemsRequest | SearchCatalogItemsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchCatalogItemsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_catalog_objects(
        self,
        body: SearchCatalogObjectsRequest | SearchCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchCatalogObjectsResponse, RawError]:
        """Searches for `CatalogObject <entity:CatalogObject>`__ of any type by matching supported search attribute
        values, excluding custom attribute values on items or item variations, against one or more of the specified
        query filters.

        This (``SearchCatalogObjects``) endpoint differs from the `SearchCatalogItems
        <api-endpoint:Catalog-SearchCatalogItems>`__ endpoint in the following aspects:

        - ``SearchCatalogItems`` can only search for items or item variations, whereas ``SearchCatalogObjects`` can
            search for any type of catalog objects.
        - ``SearchCatalogItems`` supports the custom attribute query filters to return items or item variations that
            contain custom attribute values, where ``SearchCatalogObjects`` does not.
        - ``SearchCatalogItems`` does not support the ``include_deleted_objects`` filter to search for deleted items or
            item variations, whereas ``SearchCatalogObjects`` does.
        - The both endpoints have different call conventions, including the query filter formats.

        The ``object_types`` parameter is specified as a list of `CatalogObjectType <entity:CatalogObjectType>`__
        values. Always specify ``object_types`` explicitly. When upgrading to a newer API version, omitting
        ``object_types`` may cause new object types to appear in results that were not returned under the previous
        version.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchCatalogObjectsRequest | SearchCatalogObjectsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchCatalogObjectsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_catalog_image(
        self,
        image_id: str,
        *,
        request: UpdateCatalogImageRequest | UpdateCatalogImageRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateCatalogImageResponse, RawError]:
        """Uploads a new image file to replace the existing one in the specified `CatalogImage <entity:CatalogImage>`__
        object.

        This ``UpdateCatalogImage`` endpoint accepts HTTP multipart/form-data requests with a JSON part and an image
        file part in JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.

        Args:
            image_id: The ID of the ``CatalogImage`` object to update the encapsulated image file.
            request: Value sent with the request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/catalog/images/{image_id}"),
            path_params=[param[str]("image_id", image_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                [param[UpdateCatalogImageRequest | UpdateCatalogImageRequestDict | None]("request", request)],
                {"image_file": image_file},
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateCatalogImageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_item_modifier_lists(
        self,
        body: UpdateItemModifierListsRequest | UpdateItemModifierListsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateItemModifierListsResponse, RawError]:
        """Updates the `CatalogModifierList <entity:CatalogModifierList>`__ objects that apply to the targeted
        `CatalogItem <entity:CatalogItem>`__ without having to perform an upsert on the entire item.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/update-item-modifier-lists"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateItemModifierListsRequest | UpdateItemModifierListsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateItemModifierListsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_item_taxes(
        self,
        body: UpdateItemTaxesRequest | UpdateItemTaxesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateItemTaxesResponse, RawError]:
        """Updates the `CatalogTax <entity:CatalogTax>`__ objects that apply to the targeted `CatalogItem
        <entity:CatalogItem>`__ without having to perform an upsert on the entire item.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/update-item-taxes"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateItemTaxesRequest | UpdateItemTaxesRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateItemTaxesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def upsert_catalog_object(
        self,
        body: UpsertCatalogObjectRequest | UpsertCatalogObjectRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpsertCatalogObjectResponse, RawError]:
        """Creates a new or updates the specified `CatalogObject <entity:CatalogObject>`__.

        This endpoint uses full-replacement semantics. The client must send the complete object, and any field absent
        from the request is interpreted as an intentional clear. This logic applies to nested objects as well. For
        example, omitting inlined children like variations will delete them.

        To ensure consistency, only one update request is processed at a time per seller account. While one (batch or
        non-batch) update request is being processed, other (batched and non-batched) update requests are rejected with
        the ``429`` error code.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/object"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpsertCatalogObjectRequest | UpsertCatalogObjectRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpsertCatalogObjectResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCatalogWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def batch_delete_catalog_objects(
        self,
        body: BatchDeleteCatalogObjectsRequest | BatchDeleteCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchDeleteCatalogObjectsResponse, RawError]:
        """Deletes a set of `CatalogItem <entity:CatalogItem>`__s based on the provided list of target IDs and returns a
        set of successfully deleted IDs in the response. Deletion is a cascading event such that all children of the
        targeted object are also deleted. For example, deleting a CatalogItem will also delete all of its
        `CatalogItemVariation <entity:CatalogItemVariation>`__ children.

        ``BatchDeleteCatalogObjects`` succeeds even if only a portion of the targeted IDs can be deleted. The response
        will only include IDs that were actually deleted.

        To ensure consistency, only one delete request is processed at a time per seller account. While one (batch or
        non-batch) delete request is being processed, other (batched and non-batched) delete requests are rejected with
        the ``429`` error code.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/batch-delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BatchDeleteCatalogObjectsRequest | BatchDeleteCatalogObjectsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchDeleteCatalogObjectsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def batch_retrieve_catalog_objects(
        self,
        body: BatchRetrieveCatalogObjectsRequest | BatchRetrieveCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchRetrieveCatalogObjectsResponse, RawError]:
        """Returns a set of objects based on the provided ID. Each `CatalogItem <entity:CatalogItem>`__ returned in the
        set includes all of its child information including: all of its `CatalogItemVariation
        <entity:CatalogItemVariation>`__ objects, references to its `CatalogModifierList <entity:CatalogModifierList>`__
        objects, and the ids of any `CatalogTax <entity:CatalogTax>`__ objects that apply to it.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/batch-retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BatchRetrieveCatalogObjectsRequest | BatchRetrieveCatalogObjectsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchRetrieveCatalogObjectsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def batch_upsert_catalog_objects(
        self,
        body: BatchUpsertCatalogObjectsRequest | BatchUpsertCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchUpsertCatalogObjectsResponse, RawError]:
        """Creates or updates up to 10,000 target objects based on the provided list of objects. The target objects are
        grouped into batches and each batch is inserted/updated in an all-or-nothing manner. If an object within a batch
        is malformed in some way, or violates a database constraint, the entire batch containing that item will be
        disregarded. However, other batches in the same request may still succeed. Each batch may contain up to 1,000
        objects, and batches will be processed in order as long as the total object count for the request (items,
        variations, modifier lists, discounts, and taxes) is no more than 10,000.

        This endpoint uses full-replacement semantics. The client must send the complete object, and any field absent
        from the request is interpreted as an intentional clear. This logic applies to nested objects as well. For
        example, omitting inlined children like variations will delete them.

        To ensure consistency, only one update request is processed at a time per seller account. While one (batch or
        non-batch) update request is being processed, other (batched and non-batched) update requests are rejected with
        the ``429`` error code. Prefer batching related changes into a single call rather than issuing many small
        writes, since each write acquires the lock separately and parallel writes to the same seller will contend with
        each other, producing ``429`` errors.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/batch-upsert"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BatchUpsertCatalogObjectsRequest | BatchUpsertCatalogObjectsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchUpsertCatalogObjectsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def catalog_info(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CatalogInfoResponse, RawError]:
        """Retrieves information about the Square Catalog API, such as batch size limits that can be used by the
        ``BatchUpsertCatalogObjects`` endpoint.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/catalog/info"),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CatalogInfoResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_catalog_image(
        self,
        *,
        request: CreateCatalogImageRequest | CreateCatalogImageRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCatalogImageResponse, RawError]:
        """Uploads an image file to be represented by a `CatalogImage <entity:CatalogImage>`__ object that can be linked
        to an existing `CatalogObject <entity:CatalogObject>`__ instance. The resulting ``CatalogImage`` is unattached
        to any ``CatalogObject`` if the ``object_id`` is not specified.

        This ``CreateCatalogImage`` endpoint accepts HTTP multipart/form-data requests with a JSON part and an image
        file part in JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.

        Args:
            request: Value sent with the request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/images"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                [param[CreateCatalogImageRequest | CreateCatalogImageRequestDict | None]("request", request)],
                {"image_file": image_file},
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateCatalogImageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_catalog_object(
        self, object_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteCatalogObjectResponse, RawError]:
        """Deletes a single `CatalogObject <entity:CatalogObject>`__ based on the provided ID and returns the set of
        successfully deleted IDs in the response. Deletion is a cascading event such that all children of the targeted
        object are also deleted. For example, deleting a `CatalogItem <entity:CatalogItem>`__ will also delete all of
        its `CatalogItemVariation <entity:CatalogItemVariation>`__ children.

        To ensure consistency, only one delete request is processed at a time per seller account. While one (batch or
        non-batch) delete request is being processed, other (batched and non-batched) delete requests are rejected with
        the ``429`` error code.

        Args:
            object_id: The ID of the catalog object to be deleted. When an object is deleted, other objects in the graph
                that depend on that object will be deleted as well (for example, deleting a catalog item will delete its
                catalog item variations).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/catalog/object/{object_id}"),
            path_params=[param[str]("object_id", object_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteCatalogObjectResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_catalog(
        self,
        *,
        cursor: str | None = None,
        types: str | None = None,
        catalog_version: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCatalogResponse, RawError]:
        """Returns a list of all `CatalogObject <entity:CatalogObject>`__s of the specified types in the catalog.

        The ``types`` parameter is specified as a comma-separated list of the `CatalogObjectType
        <entity:CatalogObjectType>`__ values, for example, "``ITEM``, ``ITEM_VARIATION``, ``MODIFIER``,
        ``MODIFIER_LIST``, ``CATEGORY``, ``DISCOUNT``, ``TAX``, ``IMAGE``". Always specify ``types`` explicitly. When
        upgrading to a newer API version, omitting ``types`` may cause new object types to appear in results that were
        not returned under the previous version.

        __Important:__ ListCatalog does not return deleted catalog items. To retrieve deleted catalog items, use
        `SearchCatalogObjects <api-endpoint:Catalog-SearchCatalogObjects>`__ and set the ``include_deleted_objects``
        attribute value to ``true``.

        Args:
            cursor: The pagination cursor returned in the previous response. Leave unset for an initial request. The
                page size is currently set to be 100. See `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more
                information.
            types: An optional case-insensitive, comma-separated list of object types to retrieve. The valid values are
                defined in the `CatalogObjectType <entity:CatalogObjectType>`__ enum, for example, ``ITEM``,
                ``ITEM_VARIATION``, ``CATEGORY``, ``DISCOUNT``, ``TAX``, ``MODIFIER``, ``MODIFIER_LIST``, ``IMAGE``,
                etc. If this is unspecified, the operation returns objects of all the top level types at the version of
                the Square API used to make the request. Object types that are nested onto other object types are not
                included in the defaults. At the current API version the default object types are: ITEM, CATEGORY, TAX,
                DISCOUNT, MODIFIER_LIST, PRICING_RULE, PRODUCT_SET, TIME_PERIOD, MEASUREMENT_UNIT, SUBSCRIPTION_PLAN,
                ITEM_OPTION, CUSTOM_ATTRIBUTE_DEFINITION, QUICK_AMOUNT_SETTINGS.
            catalog_version: The specific version of the catalog objects to be included in the response. This allows you
                to retrieve historical versions of objects. The specified version value is matched against the
                `CatalogObject <entity:CatalogObject>`__s' ``version`` attribute. If not included, results will be from
                the current version of the catalog.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/catalog/list"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[str | None]("types", types),
                param[int | None]("catalog_version", catalog_version),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCatalogResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_catalog_object(
        self,
        object_id: str,
        *,
        include_related_objects: bool | None = False,
        catalog_version: int | None = None,
        include_category_path_to_root: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveCatalogObjectResponse, RawError]:
        """Returns a single `CatalogItem <entity:CatalogItem>`__ as a `CatalogObject <entity:CatalogObject>`__ based on
        the provided ID. The returned object includes all of the relevant `CatalogItem <entity:CatalogItem>`__
        information including: `CatalogItemVariation <entity:CatalogItemVariation>`__ children, references to its
        `CatalogModifierList <entity:CatalogModifierList>`__ objects, and the ids of any `CatalogTax
        <entity:CatalogTax>`__ objects that apply to it.

        Args:
            object_id: The object ID of any type of catalog objects to be retrieved.
            include_related_objects: If ``true``, the response will include additional objects that are related to the
                requested objects. Related objects are defined as any objects referenced by ID by the results in the
                ``objects`` field of the response. These objects are put in the ``related_objects`` field. Setting this
                to ``true`` is helpful when the objects are needed for immediate display to a user. This process only
                goes one level deep. Objects referenced by the related objects will not be included. For example, if the
                ``objects`` field of the response contains a CatalogItem, its associated CatalogCategory objects,
                CatalogTax objects, CatalogImage objects and CatalogModifierLists will be returned in the
                ``related_objects`` field of the response. If the ``objects`` field of the response contains a
                CatalogItemVariation, its parent CatalogItem will be returned in the ``related_objects`` field of the
                response. Default value: ``false``
            catalog_version: Requests objects as of a specific version of the catalog. This allows you to retrieve
                historical versions of objects. The value to retrieve a specific version of an object can be found in
                the version field of `CatalogObject <entity:CatalogObject>`__s. If not included, results will be from
                the current version of the catalog.
            include_category_path_to_root: Specifies whether or not to include the ``path_to_root`` list for each
                returned category instance. The ``path_to_root`` list consists of ``CategoryPathToRootNode`` objects and
                specifies the path that starts with the immediate parent category of the returned category and ends with
                its root category. If the returned category is a top-level category, the ``path_to_root`` list is empty
                and is not returned in the response payload.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/catalog/object/{object_id}"),
            path_params=[param[str]("object_id", object_id)],
            query_params=[
                param[bool | None]("include_related_objects", include_related_objects),
                param[int | None]("catalog_version", catalog_version),
                param[bool | None]("include_category_path_to_root", include_category_path_to_root),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveCatalogObjectResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_catalog_items(
        self,
        body: SearchCatalogItemsRequest | SearchCatalogItemsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchCatalogItemsResponse, RawError]:
        """Searches for catalog items or item variations by matching supported search attribute values, including custom
        attribute values, against one or more of the specified query filters.

        This (``SearchCatalogItems``) endpoint differs from the `SearchCatalogObjects
        <api-endpoint:Catalog-SearchCatalogObjects>`__ endpoint in the following aspects:

        - ``SearchCatalogItems`` can only search for items or item variations, whereas ``SearchCatalogObjects`` can
            search for any type of catalog objects.
        - ``SearchCatalogItems`` supports the custom attribute query filters to return items or item variations that
            contain custom attribute values, where ``SearchCatalogObjects`` does not.
        - ``SearchCatalogItems`` does not support the ``include_deleted_objects`` filter to search for deleted items or
            item variations, whereas ``SearchCatalogObjects`` does.
        - The both endpoints use different call conventions, including the query filter formats.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/search-catalog-items"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchCatalogItemsRequest | SearchCatalogItemsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchCatalogItemsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_catalog_objects(
        self,
        body: SearchCatalogObjectsRequest | SearchCatalogObjectsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchCatalogObjectsResponse, RawError]:
        """Searches for `CatalogObject <entity:CatalogObject>`__ of any type by matching supported search attribute
        values, excluding custom attribute values on items or item variations, against one or more of the specified
        query filters.

        This (``SearchCatalogObjects``) endpoint differs from the `SearchCatalogItems
        <api-endpoint:Catalog-SearchCatalogItems>`__ endpoint in the following aspects:

        - ``SearchCatalogItems`` can only search for items or item variations, whereas ``SearchCatalogObjects`` can
            search for any type of catalog objects.
        - ``SearchCatalogItems`` supports the custom attribute query filters to return items or item variations that
            contain custom attribute values, where ``SearchCatalogObjects`` does not.
        - ``SearchCatalogItems`` does not support the ``include_deleted_objects`` filter to search for deleted items or
            item variations, whereas ``SearchCatalogObjects`` does.
        - The both endpoints have different call conventions, including the query filter formats.

        The ``object_types`` parameter is specified as a list of `CatalogObjectType <entity:CatalogObjectType>`__
        values. Always specify ``object_types`` explicitly. When upgrading to a newer API version, omitting
        ``object_types`` may cause new object types to appear in results that were not returned under the previous
        version.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchCatalogObjectsRequest | SearchCatalogObjectsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchCatalogObjectsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_catalog_image(
        self,
        image_id: str,
        *,
        request: UpdateCatalogImageRequest | UpdateCatalogImageRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateCatalogImageResponse, RawError]:
        """Uploads a new image file to replace the existing one in the specified `CatalogImage <entity:CatalogImage>`__
        object.

        This ``UpdateCatalogImage`` endpoint accepts HTTP multipart/form-data requests with a JSON part and an image
        file part in JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.

        Args:
            image_id: The ID of the ``CatalogImage`` object to update the encapsulated image file.
            request: Value sent with the request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/catalog/images/{image_id}"),
            path_params=[param[str]("image_id", image_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                [param[UpdateCatalogImageRequest | UpdateCatalogImageRequestDict | None]("request", request)],
                {"image_file": image_file},
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateCatalogImageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_item_modifier_lists(
        self,
        body: UpdateItemModifierListsRequest | UpdateItemModifierListsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateItemModifierListsResponse, RawError]:
        """Updates the `CatalogModifierList <entity:CatalogModifierList>`__ objects that apply to the targeted
        `CatalogItem <entity:CatalogItem>`__ without having to perform an upsert on the entire item.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/update-item-modifier-lists"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateItemModifierListsRequest | UpdateItemModifierListsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateItemModifierListsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_item_taxes(
        self,
        body: UpdateItemTaxesRequest | UpdateItemTaxesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateItemTaxesResponse, RawError]:
        """Updates the `CatalogTax <entity:CatalogTax>`__ objects that apply to the targeted `CatalogItem
        <entity:CatalogItem>`__ without having to perform an upsert on the entire item.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/update-item-taxes"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateItemTaxesRequest | UpdateItemTaxesRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateItemTaxesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def upsert_catalog_object(
        self,
        body: UpsertCatalogObjectRequest | UpsertCatalogObjectRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpsertCatalogObjectResponse, RawError]:
        """Creates a new or updates the specified `CatalogObject <entity:CatalogObject>`__.

        This endpoint uses full-replacement semantics. The client must send the complete object, and any field absent
        from the request is interpreted as an intentional clear. This logic applies to nested objects as well. For
        example, omitting inlined children like variations will delete them.

        To ensure consistency, only one update request is processed at a time per seller account. While one (batch or
        non-batch) update request is being processed, other (batched and non-batched) update requests are rejected with
        the ``429`` error code.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/catalog/object"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpsertCatalogObjectRequest | UpsertCatalogObjectRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpsertCatalogObjectResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
