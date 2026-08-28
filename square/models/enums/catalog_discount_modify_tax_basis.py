from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogDiscountModifyTaxBasis(str, Enum):
    MODIFY_TAX_BASIS = "MODIFY_TAX_BASIS"
    """Application of the discount will modify the tax basis."""

    DO_NOT_MODIFY_TAX_BASIS = "DO_NOT_MODIFY_TAX_BASIS"
    """Application of the discount will not modify the tax basis."""

    __str__ = str.__str__


CatalogDiscountModifyTaxBasisOrStr: TypeAlias = Annotated[
    CatalogDiscountModifyTaxBasis | str, open_enum_validator(CatalogDiscountModifyTaxBasis)
]
