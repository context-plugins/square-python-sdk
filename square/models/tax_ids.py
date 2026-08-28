from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TaxIds(SdkBaseModel):
    """Identifiers for the location used by various governments for tax purposes."""

    eu_vat: Optional[str] = UNSET
    """The EU VAT number for this location. For example, ``IE3426675K``. If the EU VAT number is present, it is
    well-formed and has been validated with VIES, the VAT Information Exchange System."""

    fr_siret: Optional[str] = UNSET
    """The SIRET (Système d'Identification du Répertoire des Entreprises et de leurs Etablissements) number is a
    14-digit code issued by the French INSEE. For example, ``39922799000021``."""

    fr_naf: Optional[str] = UNSET
    """The French government uses the NAF (Nomenclature des Activités Françaises) to display and track economic
    statistical data. This is also called the APE (Activite Principale de l’Entreprise) code. For example, ``6910Z``."""

    es_nif: Optional[str] = UNSET
    """The NIF (Numero de Identificacion Fiscal) number is a nine-character tax identifier used in Spain. If it is
    present, it has been validated. For example, ``73628495A``."""

    jp_qii: Optional[str] = UNSET
    """The QII (Qualified Invoice Issuer) number is a 14-character tax identifier used in Japan. For example,
    ``T1234567890123``."""


class TaxIdsDict(TypedDict):
    eu_vat: NotRequired[str]
    fr_siret: NotRequired[str]
    fr_naf: NotRequired[str]
    es_nif: NotRequired[str]
    jp_qii: NotRequired[str]
