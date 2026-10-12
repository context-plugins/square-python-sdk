from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_query import CatalogQuery, CatalogQueryDict
from .enums.catalog_object_type import CatalogObjectTypeOrStr


class SearchCatalogObjectsRequest(SdkBaseModel):
    cursor: Optional[str] = UNSET
    """The pagination cursor returned in the previous response. Leave unset for an initial request. See `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more information."""

    object_types: Optional[list[CatalogObjectTypeOrStr]] = UNSET
    """The desired set of object types to appear in the search results.

    If this is unspecified, the operation returns objects of all the top level types at the version of the Square API
    used to make the request. Object types that are nested onto other object types are not included in the defaults.

    At the current API version the default object types are: ITEM, CATEGORY, TAX, DISCOUNT, MODIFIER_LIST, PRICING_RULE,
    PRODUCT_SET, TIME_PERIOD, MEASUREMENT_UNIT, SUBSCRIPTION_PLAN, ITEM_OPTION, CUSTOM_ATTRIBUTE_DEFINITION,
    QUICK_AMOUNT_SETTINGS.

    Note that if you wish for the query to return objects belonging to nested types (i.e., COMPONENT, IMAGE,
    ITEM_OPTION_VAL, ITEM_VARIATION, or MODIFIER), you must explicitly include all the types of interest in this
    field."""

    include_deleted_objects: Optional[bool] = UNSET
    """If ``true``, deleted objects will be included in the results. Defaults to ``false``. Deleted objects will have
    their ``is_deleted`` field set to ``true``. If ``include_deleted_objects`` is ``true``, then the
    ``include_category_path_to_root`` request parameter must be ``false``. Both properties cannot be ``true`` at the
    same time."""

    include_related_objects: Optional[bool] = UNSET
    """If ``true``, the response will include additional objects that are related to the requested objects. Related
    objects are objects that are referenced by object ID by the objects in the response. This is helpful if the objects
    are being fetched for immediate display to a user. This process only goes one level deep. Objects referenced by the
    related objects will not be included. For example:

    If the ``objects`` field of the response contains a CatalogItem, its associated CatalogCategory objects, CatalogTax
    objects, CatalogImage objects and CatalogModifierLists will be returned in the ``related_objects`` field of the
    response. If the ``objects`` field of the response contains a CatalogItemVariation, its parent CatalogItem will be
    returned in the ``related_objects`` field of the response.

    Default value: ``false``"""

    begin_time: Optional[str] = UNSET
    """Return objects modified after this `timestamp
    <https://developer.squareup.com/docs/build-basics/working-with-dates>`__, in RFC 3339 format, e.g.,
    ``2016-09-04T23:59:33.123Z``. The timestamp is exclusive - objects with a timestamp equal to ``begin_time`` will not
    be included in the response."""

    query: Optional[CatalogQuery] = UNSET
    """A query composed of one or more different types of filters to narrow the scope of targeted objects when calling
    the ``SearchCatalogObjects`` endpoint.

    Although a query can have multiple filters, only certain query types can be combined per call to
    `SearchCatalogObjects <api-endpoint:Catalog-SearchCatalogObjects>`__. Any combination of the following types may be
    used together:
    - `exact_query <entity:CatalogQueryExact>`__
    - `prefix_query <entity:CatalogQueryPrefix>`__
    - `range_query <entity:CatalogQueryRange>`__
    - `sorted_attribute_query <entity:CatalogQuerySortedAttribute>`__
    - `text_query <entity:CatalogQueryText>`__

    All other query types cannot be combined with any others.

    When a query filter is based on an attribute, the attribute must be searchable. Searchable attributes are listed as
    follows, along their parent types that can be searched for with applicable query filters.

    Searchable attribute and objects queryable by searchable attributes:
    - ``name``: ``CatalogItem``, ``CatalogItemVariation``, ``CatalogCategory``, ``CatalogTax``, ``CatalogDiscount``,
        ``CatalogModifier``, ``CatalogModifierList``, ``CatalogItemOption``, ``CatalogItemOptionValue``
    - ``description``: ``CatalogItem``, ``CatalogItemOptionValue``
    - ``abbreviation``: ``CatalogItem``
    - ``upc``: ``CatalogItemVariation``
    - ``sku``: ``CatalogItemVariation``
    - ``caption``: ``CatalogImage``
    - ``display_name``: ``CatalogItemOption``

    For example, to search for `CatalogItem <entity:CatalogItem>`__ objects by searchable attributes, you can use the
    ``"name"``, ``"description"``, or ``"abbreviation"`` attribute in an applicable query filter."""

    limit: Optional[int] = UNSET
    """A limit on the number of results to be returned in a single page. The limit is advisory - the implementation may
    return more or fewer results. If the supplied limit is negative, zero, or is higher than the maximum limit of 1,000,
    it will be ignored."""

    include_category_path_to_root: Optional[bool] = UNSET
    """Specifies whether or not to include the ``path_to_root`` list for each returned category instance. The
    ``path_to_root`` list consists of ``CategoryPathToRootNode`` objects and specifies the path that starts with the
    immediate parent category of the returned category and ends with its root category. If the returned category is a
    top-level category, the ``path_to_root`` list is empty and is not returned in the response payload. If
    ``include_category_path_to_root`` is ``true``, then the ``include_deleted_objects`` request parameter must be
    ``false``. Both properties cannot be ``true`` at the same time."""


class SearchCatalogObjectsRequestDict(TypedDict):
    cursor: NotRequired[str]
    object_types: NotRequired[list[CatalogObjectTypeOrStr]]
    include_deleted_objects: NotRequired[bool]
    include_related_objects: NotRequired[bool]
    begin_time: NotRequired[str]
    query: NotRequired[CatalogQueryDict]
    limit: NotRequired[int]
    include_category_path_to_root: NotRequired[bool]
