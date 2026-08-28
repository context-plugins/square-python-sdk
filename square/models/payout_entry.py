from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.activity_type import ActivityTypeOrStr
from .money import Money, MoneyDict
from .payment_balance_activity_app_fee_refund_detail import (
    PaymentBalanceActivityAppFeeRefundDetail,
    PaymentBalanceActivityAppFeeRefundDetailDict,
)
from .payment_balance_activity_app_fee_revenue_detail import (
    PaymentBalanceActivityAppFeeRevenueDetail,
    PaymentBalanceActivityAppFeeRevenueDetailDict,
)
from .payment_balance_activity_automatic_savings_detail import (
    PaymentBalanceActivityAutomaticSavingsDetail,
    PaymentBalanceActivityAutomaticSavingsDetailDict,
)
from .payment_balance_activity_automatic_savings_reversed_detail import (
    PaymentBalanceActivityAutomaticSavingsReversedDetail,
    PaymentBalanceActivityAutomaticSavingsReversedDetailDict,
)
from .payment_balance_activity_charge_detail import (
    PaymentBalanceActivityChargeDetail,
    PaymentBalanceActivityChargeDetailDict,
)
from .payment_balance_activity_deposit_fee_detail import (
    PaymentBalanceActivityDepositFeeDetail,
    PaymentBalanceActivityDepositFeeDetailDict,
)
from .payment_balance_activity_deposit_fee_reversed_detail import (
    PaymentBalanceActivityDepositFeeReversedDetail,
    PaymentBalanceActivityDepositFeeReversedDetailDict,
)
from .payment_balance_activity_dispute_detail import (
    PaymentBalanceActivityDisputeDetail,
    PaymentBalanceActivityDisputeDetailDict,
)
from .payment_balance_activity_fee_detail import PaymentBalanceActivityFeeDetail, PaymentBalanceActivityFeeDetailDict
from .payment_balance_activity_free_processing_detail import (
    PaymentBalanceActivityFreeProcessingDetail,
    PaymentBalanceActivityFreeProcessingDetailDict,
)
from .payment_balance_activity_hold_adjustment_detail import (
    PaymentBalanceActivityHoldAdjustmentDetail,
    PaymentBalanceActivityHoldAdjustmentDetailDict,
)
from .payment_balance_activity_open_dispute_detail import (
    PaymentBalanceActivityOpenDisputeDetail,
    PaymentBalanceActivityOpenDisputeDetailDict,
)
from .payment_balance_activity_other_adjustment_detail import (
    PaymentBalanceActivityOtherAdjustmentDetail,
    PaymentBalanceActivityOtherAdjustmentDetailDict,
)
from .payment_balance_activity_other_detail import (
    PaymentBalanceActivityOtherDetail,
    PaymentBalanceActivityOtherDetailDict,
)
from .payment_balance_activity_refund_detail import (
    PaymentBalanceActivityRefundDetail,
    PaymentBalanceActivityRefundDetailDict,
)
from .payment_balance_activity_release_adjustment_detail import (
    PaymentBalanceActivityReleaseAdjustmentDetail,
    PaymentBalanceActivityReleaseAdjustmentDetailDict,
)
from .payment_balance_activity_reserve_hold_detail import (
    PaymentBalanceActivityReserveHoldDetail,
    PaymentBalanceActivityReserveHoldDetailDict,
)
from .payment_balance_activity_reserve_release_detail import (
    PaymentBalanceActivityReserveReleaseDetail,
    PaymentBalanceActivityReserveReleaseDetailDict,
)
from .payment_balance_activity_square_capital_payment_detail import (
    PaymentBalanceActivitySquareCapitalPaymentDetail,
    PaymentBalanceActivitySquareCapitalPaymentDetailDict,
)
from .payment_balance_activity_square_capital_reversed_payment_detail import (
    PaymentBalanceActivitySquareCapitalReversedPaymentDetail,
    PaymentBalanceActivitySquareCapitalReversedPaymentDetailDict,
)
from .payment_balance_activity_square_payroll_transfer_detail import (
    PaymentBalanceActivitySquarePayrollTransferDetail,
    PaymentBalanceActivitySquarePayrollTransferDetailDict,
)
from .payment_balance_activity_square_payroll_transfer_reversed_detail import (
    PaymentBalanceActivitySquarePayrollTransferReversedDetail,
    PaymentBalanceActivitySquarePayrollTransferReversedDetailDict,
)
from .payment_balance_activity_tax_on_fee_detail import (
    PaymentBalanceActivityTaxOnFeeDetail,
    PaymentBalanceActivityTaxOnFeeDetailDict,
)
from .payment_balance_activity_third_party_fee_detail import (
    PaymentBalanceActivityThirdPartyFeeDetail,
    PaymentBalanceActivityThirdPartyFeeDetailDict,
)
from .payment_balance_activity_third_party_fee_refund_detail import (
    PaymentBalanceActivityThirdPartyFeeRefundDetail,
    PaymentBalanceActivityThirdPartyFeeRefundDetailDict,
)


class PayoutEntry(SdkBaseModel):
    """One or more PayoutEntries that make up a Payout. Each one has a date, amount, and type of activity. The total
    amount of the payout will equal the sum of the payout entries for a batch payout"""

    id: str
    """A unique ID for the payout entry."""

    payout_id: str
    """The ID of the payout entries’ associated payout."""

    effective_at: OptionalNullable[str] = UNSET
    """The timestamp of when the payout entry affected the balance, in RFC 3339 format."""

    type_: Optional[ActivityTypeOrStr] = Field(default=UNSET, alias="type")
    gross_amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    fee_amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    net_amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    type_app_fee_revenue_details: Optional[PaymentBalanceActivityAppFeeRevenueDetail] = UNSET
    type_app_fee_refund_details: Optional[PaymentBalanceActivityAppFeeRefundDetail] = UNSET
    type_automatic_savings_details: Optional[PaymentBalanceActivityAutomaticSavingsDetail] = UNSET
    type_automatic_savings_reversed_details: Optional[PaymentBalanceActivityAutomaticSavingsReversedDetail] = UNSET
    type_charge_details: Optional[PaymentBalanceActivityChargeDetail] = UNSET
    type_deposit_fee_details: Optional[PaymentBalanceActivityDepositFeeDetail] = UNSET
    type_deposit_fee_reversed_details: Optional[PaymentBalanceActivityDepositFeeReversedDetail] = UNSET
    type_dispute_details: Optional[PaymentBalanceActivityDisputeDetail] = UNSET
    type_fee_details: Optional[PaymentBalanceActivityFeeDetail] = UNSET
    type_free_processing_details: Optional[PaymentBalanceActivityFreeProcessingDetail] = UNSET
    type_hold_adjustment_details: Optional[PaymentBalanceActivityHoldAdjustmentDetail] = UNSET
    type_open_dispute_details: Optional[PaymentBalanceActivityOpenDisputeDetail] = UNSET
    type_other_details: Optional[PaymentBalanceActivityOtherDetail] = UNSET
    type_other_adjustment_details: Optional[PaymentBalanceActivityOtherAdjustmentDetail] = UNSET
    type_refund_details: Optional[PaymentBalanceActivityRefundDetail] = UNSET
    type_release_adjustment_details: Optional[PaymentBalanceActivityReleaseAdjustmentDetail] = UNSET
    type_reserve_hold_details: Optional[PaymentBalanceActivityReserveHoldDetail] = UNSET
    type_reserve_release_details: Optional[PaymentBalanceActivityReserveReleaseDetail] = UNSET
    type_square_capital_payment_details: Optional[PaymentBalanceActivitySquareCapitalPaymentDetail] = UNSET
    type_square_capital_reversed_payment_details: Optional[
        PaymentBalanceActivitySquareCapitalReversedPaymentDetail
    ] = UNSET
    type_tax_on_fee_details: Optional[PaymentBalanceActivityTaxOnFeeDetail] = UNSET
    type_third_party_fee_details: Optional[PaymentBalanceActivityThirdPartyFeeDetail] = UNSET
    type_third_party_fee_refund_details: Optional[PaymentBalanceActivityThirdPartyFeeRefundDetail] = UNSET
    type_square_payroll_transfer_details: Optional[PaymentBalanceActivitySquarePayrollTransferDetail] = UNSET
    type_square_payroll_transfer_reversed_details: Optional[
        PaymentBalanceActivitySquarePayrollTransferReversedDetail
    ] = UNSET


class PayoutEntryDict(TypedDict):
    id: str
    payout_id: str
    effective_at: NotRequired[str | None]
    type_: NotRequired[ActivityTypeOrStr]
    gross_amount_money: NotRequired[Money | MoneyDict]
    fee_amount_money: NotRequired[Money | MoneyDict]
    net_amount_money: NotRequired[Money | MoneyDict]
    type_app_fee_revenue_details: NotRequired[
        PaymentBalanceActivityAppFeeRevenueDetail | PaymentBalanceActivityAppFeeRevenueDetailDict
    ]
    type_app_fee_refund_details: NotRequired[
        PaymentBalanceActivityAppFeeRefundDetail | PaymentBalanceActivityAppFeeRefundDetailDict
    ]
    type_automatic_savings_details: NotRequired[
        PaymentBalanceActivityAutomaticSavingsDetail | PaymentBalanceActivityAutomaticSavingsDetailDict
    ]
    type_automatic_savings_reversed_details: NotRequired[
        PaymentBalanceActivityAutomaticSavingsReversedDetail | PaymentBalanceActivityAutomaticSavingsReversedDetailDict
    ]
    type_charge_details: NotRequired[PaymentBalanceActivityChargeDetail | PaymentBalanceActivityChargeDetailDict]
    type_deposit_fee_details: NotRequired[
        PaymentBalanceActivityDepositFeeDetail | PaymentBalanceActivityDepositFeeDetailDict
    ]
    type_deposit_fee_reversed_details: NotRequired[
        PaymentBalanceActivityDepositFeeReversedDetail | PaymentBalanceActivityDepositFeeReversedDetailDict
    ]
    type_dispute_details: NotRequired[PaymentBalanceActivityDisputeDetail | PaymentBalanceActivityDisputeDetailDict]
    type_fee_details: NotRequired[PaymentBalanceActivityFeeDetail | PaymentBalanceActivityFeeDetailDict]
    type_free_processing_details: NotRequired[
        PaymentBalanceActivityFreeProcessingDetail | PaymentBalanceActivityFreeProcessingDetailDict
    ]
    type_hold_adjustment_details: NotRequired[
        PaymentBalanceActivityHoldAdjustmentDetail | PaymentBalanceActivityHoldAdjustmentDetailDict
    ]
    type_open_dispute_details: NotRequired[
        PaymentBalanceActivityOpenDisputeDetail | PaymentBalanceActivityOpenDisputeDetailDict
    ]
    type_other_details: NotRequired[PaymentBalanceActivityOtherDetail | PaymentBalanceActivityOtherDetailDict]
    type_other_adjustment_details: NotRequired[
        PaymentBalanceActivityOtherAdjustmentDetail | PaymentBalanceActivityOtherAdjustmentDetailDict
    ]
    type_refund_details: NotRequired[PaymentBalanceActivityRefundDetail | PaymentBalanceActivityRefundDetailDict]
    type_release_adjustment_details: NotRequired[
        PaymentBalanceActivityReleaseAdjustmentDetail | PaymentBalanceActivityReleaseAdjustmentDetailDict
    ]
    type_reserve_hold_details: NotRequired[
        PaymentBalanceActivityReserveHoldDetail | PaymentBalanceActivityReserveHoldDetailDict
    ]
    type_reserve_release_details: NotRequired[
        PaymentBalanceActivityReserveReleaseDetail | PaymentBalanceActivityReserveReleaseDetailDict
    ]
    type_square_capital_payment_details: NotRequired[
        PaymentBalanceActivitySquareCapitalPaymentDetail | PaymentBalanceActivitySquareCapitalPaymentDetailDict
    ]
    type_square_capital_reversed_payment_details: NotRequired[
        (
            PaymentBalanceActivitySquareCapitalReversedPaymentDetail
            | PaymentBalanceActivitySquareCapitalReversedPaymentDetailDict
        )
    ]
    type_tax_on_fee_details: NotRequired[
        PaymentBalanceActivityTaxOnFeeDetail | PaymentBalanceActivityTaxOnFeeDetailDict
    ]
    type_third_party_fee_details: NotRequired[
        PaymentBalanceActivityThirdPartyFeeDetail | PaymentBalanceActivityThirdPartyFeeDetailDict
    ]
    type_third_party_fee_refund_details: NotRequired[
        PaymentBalanceActivityThirdPartyFeeRefundDetail | PaymentBalanceActivityThirdPartyFeeRefundDetailDict
    ]
    type_square_payroll_transfer_details: NotRequired[
        PaymentBalanceActivitySquarePayrollTransferDetail | PaymentBalanceActivitySquarePayrollTransferDetailDict
    ]
    type_square_payroll_transfer_reversed_details: NotRequired[
        (
            PaymentBalanceActivitySquarePayrollTransferReversedDetail
            | PaymentBalanceActivitySquarePayrollTransferReversedDetailDict
        )
    ]
