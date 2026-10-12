from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.order_service_charge_calculation_phase import OrderServiceChargeCalculationPhaseOrStr
from .enums.order_service_charge_scope import OrderServiceChargeScopeOrStr
from .enums.order_service_charge_treatment_type import OrderServiceChargeTreatmentTypeOrStr
from .enums.order_service_charge_type import OrderServiceChargeTypeOrStr
from .money import Money, MoneyDict
from .order_line_item_applied_tax import OrderLineItemAppliedTax, OrderLineItemAppliedTaxDict


class OrderReturnServiceCharge(SdkBaseModel):
    """Represents the service charge applied to the original order."""

    uid: OptionalNullable[str] = UNSET
    """A unique ID that identifies the return service charge only within this order."""

    source_service_charge_uid: OptionalNullable[str] = UNSET
    """The service charge ``uid`` from the order containing the original service charge. ``source_service_charge_uid``
    is ``null`` for unlinked returns."""

    name: OptionalNullable[str] = UNSET
    """The name of the service charge."""

    catalog_object_id: OptionalNullable[str] = UNSET
    """The catalog object ID of the associated `OrderServiceCharge <entity:OrderServiceCharge>`__."""

    catalog_version: OptionalNullable[int] = UNSET
    """The version of the catalog object that this service charge references."""

    percentage: OptionalNullable[str] = UNSET
    """The percentage of the service charge, as a string representation of a decimal number. For example, a value of
    ``"7.25"`` corresponds to a percentage of 7.25%.

    Either ``percentage`` or ``amount_money`` should be set, but not both."""

    amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    applied_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    total_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    total_tax_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    calculation_phase: Optional[OrderServiceChargeCalculationPhaseOrStr] = UNSET
    """Represents a phase in the process of calculating order totals. Service charges are applied after the indicated
    phase.

    `Read more about how order totals are calculated.
    <https://developer.squareup.com/docs/orders-api/how-it-works#how-totals-are-calculated>`__"""

    taxable: OptionalNullable[bool] = UNSET
    """Indicates whether the surcharge can be taxed. Service charges calculated in the ``TOTAL_PHASE`` cannot be marked
    as taxable."""

    applied_taxes: OptionalNullable[list[OrderLineItemAppliedTax]] = UNSET
    """The list of references to ``OrderReturnTax`` entities applied to the ``OrderReturnServiceCharge``. Each
    ``OrderLineItemAppliedTax`` has a ``tax_uid`` that references the ``uid`` of a top-level ``OrderReturnTax`` that is
    being applied to the ``OrderReturnServiceCharge``. On reads, the applied amount is populated."""

    treatment_type: Optional[OrderServiceChargeTreatmentTypeOrStr] = UNSET
    """Indicates whether the service charge will be treated as a value-holding line item or apportioned toward a line
    item."""

    scope: Optional[OrderServiceChargeScopeOrStr] = UNSET
    """Indicates whether this is a line-item or order-level apportioned service charge."""

    type_: Optional[OrderServiceChargeTypeOrStr] = Field(default=UNSET, alias="type")


class OrderReturnServiceChargeDict(TypedDict):
    uid: NotRequired[str | None]
    source_service_charge_uid: NotRequired[str | None]
    name: NotRequired[str | None]
    catalog_object_id: NotRequired[str | None]
    catalog_version: NotRequired[int | None]
    percentage: NotRequired[str | None]
    amount_money: NotRequired[MoneyDict]
    applied_money: NotRequired[MoneyDict]
    total_money: NotRequired[MoneyDict]
    total_tax_money: NotRequired[MoneyDict]
    calculation_phase: NotRequired[OrderServiceChargeCalculationPhaseOrStr]
    taxable: NotRequired[bool | None]
    applied_taxes: NotRequired[list[OrderLineItemAppliedTaxDict] | None]
    treatment_type: NotRequired[OrderServiceChargeTreatmentTypeOrStr]
    scope: NotRequired[OrderServiceChargeScopeOrStr]
    type_: NotRequired[OrderServiceChargeTypeOrStr]
