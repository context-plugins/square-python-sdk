from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Currency(str, Enum):
    """Indicates the associated currency for an amount of money. Values correspond to `ISO 4217
    <https://wikipedia.org/wiki/ISO_4217>`__."""

    UNKNOWN_CURRENCY = "UNKNOWN_CURRENCY"
    """Unknown currency"""

    AED = "AED"
    """United Arab Emirates dirham"""

    AFN = "AFN"
    """Afghan afghani"""

    ALL = "ALL"
    """Albanian lek"""

    AMD = "AMD"
    """Armenian dram"""

    ANG = "ANG"
    """Netherlands Antillean guilder"""

    AOA = "AOA"
    """Angolan kwanza"""

    ARS = "ARS"
    """Argentine peso"""

    AUD = "AUD"
    """Australian dollar"""

    AWG = "AWG"
    """Aruban florin"""

    AZN = "AZN"
    """Azerbaijani manat"""

    BAM = "BAM"
    """Bosnia and Herzegovina convertible mark"""

    BBD = "BBD"
    """Barbados dollar"""

    BDT = "BDT"
    """Bangladeshi taka"""

    BGN = "BGN"
    """Bulgarian lev"""

    BHD = "BHD"
    """Bahraini dinar"""

    BIF = "BIF"
    """Burundian franc"""

    BMD = "BMD"
    """Bermudian dollar"""

    BND = "BND"
    """Brunei dollar"""

    BOB = "BOB"
    """Boliviano"""

    BOV = "BOV"
    """Bolivian Mvdol"""

    BRL = "BRL"
    """Brazilian real"""

    BSD = "BSD"
    """Bahamian dollar"""

    BTN = "BTN"
    """Bhutanese ngultrum"""

    BWP = "BWP"
    """Botswana pula"""

    BYR = "BYR"
    """Belarusian ruble"""

    BZD = "BZD"
    """Belize dollar"""

    CAD = "CAD"
    """Canadian dollar"""

    CDF = "CDF"
    """Congolese franc"""

    CHE = "CHE"
    """WIR Euro"""

    CHF = "CHF"
    """Swiss franc"""

    CHW = "CHW"
    """WIR Franc"""

    CLF = "CLF"
    """Unidad de Fomento"""

    CLP = "CLP"
    """Chilean peso"""

    CNY = "CNY"
    """Chinese yuan"""

    COP = "COP"
    """Colombian peso"""

    COU = "COU"
    """Unidad de Valor Real"""

    CRC = "CRC"
    """Costa Rican colon"""

    CUC = "CUC"
    """Cuban convertible peso"""

    CUP = "CUP"
    """Cuban peso"""

    CVE = "CVE"
    """Cape Verdean escudo"""

    CZK = "CZK"
    """Czech koruna"""

    DJF = "DJF"
    """Djiboutian franc"""

    DKK = "DKK"
    """Danish krone"""

    DOP = "DOP"
    """Dominican peso"""

    DZD = "DZD"
    """Algerian dinar"""

    EGP = "EGP"
    """Egyptian pound"""

    ERN = "ERN"
    """Eritrean nakfa"""

    ETB = "ETB"
    """Ethiopian birr"""

    EUR = "EUR"
    """Euro"""

    FJD = "FJD"
    """Fiji dollar"""

    FKP = "FKP"
    """Falkland Islands pound"""

    GBP = "GBP"
    """Pound sterling"""

    GEL = "GEL"
    """Georgian lari"""

    GHS = "GHS"
    """Ghanaian cedi"""

    GIP = "GIP"
    """Gibraltar pound"""

    GMD = "GMD"
    """Gambian dalasi"""

    GNF = "GNF"
    """Guinean franc"""

    GTQ = "GTQ"
    """Guatemalan quetzal"""

    GYD = "GYD"
    """Guyanese dollar"""

    HKD = "HKD"
    """Hong Kong dollar"""

    HNL = "HNL"
    """Honduran lempira"""

    HRK = "HRK"
    """Croatian kuna"""

    HTG = "HTG"
    """Haitian gourde"""

    HUF = "HUF"
    """Hungarian forint"""

    IDR = "IDR"
    """Indonesian rupiah"""

    ILS = "ILS"
    """Israeli new shekel"""

    INR = "INR"
    """Indian rupee"""

    IQD = "IQD"
    """Iraqi dinar"""

    IRR = "IRR"
    """Iranian rial"""

    ISK = "ISK"
    """Icelandic króna"""

    JMD = "JMD"
    """Jamaican dollar"""

    JOD = "JOD"
    """Jordanian dinar"""

    JPY = "JPY"
    """Japanese yen"""

    KES = "KES"
    """Kenyan shilling"""

    KGS = "KGS"
    """Kyrgyzstani som"""

    KHR = "KHR"
    """Cambodian riel"""

    KMF = "KMF"
    """Comoro franc"""

    KPW = "KPW"
    """North Korean won"""

    KRW = "KRW"
    """South Korean won"""

    KWD = "KWD"
    """Kuwaiti dinar"""

    KYD = "KYD"
    """Cayman Islands dollar"""

    KZT = "KZT"
    """Kazakhstani tenge"""

    LAK = "LAK"
    """Lao kip"""

    LBP = "LBP"
    """Lebanese pound"""

    LKR = "LKR"
    """Sri Lankan rupee"""

    LRD = "LRD"
    """Liberian dollar"""

    LSL = "LSL"
    """Lesotho loti"""

    LTL = "LTL"
    """Lithuanian litas"""

    LVL = "LVL"
    """Latvian lats"""

    LYD = "LYD"
    """Libyan dinar"""

    MAD = "MAD"
    """Moroccan dirham"""

    MDL = "MDL"
    """Moldovan leu"""

    MGA = "MGA"
    """Malagasy ariary"""

    MKD = "MKD"
    """Macedonian denar"""

    MMK = "MMK"
    """Myanmar kyat"""

    MNT = "MNT"
    """Mongolian tögrög"""

    MOP = "MOP"
    """Macanese pataca"""

    MRO = "MRO"
    """Mauritanian ouguiya"""

    MUR = "MUR"
    """Mauritian rupee"""

    MVR = "MVR"
    """Maldivian rufiyaa"""

    MWK = "MWK"
    """Malawian kwacha"""

    MXN = "MXN"
    """Mexican peso"""

    MXV = "MXV"
    """Mexican Unidad de Inversion"""

    MYR = "MYR"
    """Malaysian ringgit"""

    MZN = "MZN"
    """Mozambican metical"""

    NAD = "NAD"
    """Namibian dollar"""

    NGN = "NGN"
    """Nigerian naira"""

    NIO = "NIO"
    """Nicaraguan córdoba"""

    NOK = "NOK"
    """Norwegian krone"""

    NPR = "NPR"
    """Nepalese rupee"""

    NZD = "NZD"
    """New Zealand dollar"""

    OMR = "OMR"
    """Omani rial"""

    PAB = "PAB"
    """Panamanian balboa"""

    PEN = "PEN"
    """Peruvian sol"""

    PGK = "PGK"
    """Papua New Guinean kina"""

    PHP = "PHP"
    """Philippine peso"""

    PKR = "PKR"
    """Pakistani rupee"""

    PLN = "PLN"
    """Polish złoty"""

    PYG = "PYG"
    """Paraguayan guaraní"""

    QAR = "QAR"
    """Qatari riyal"""

    RON = "RON"
    """Romanian leu"""

    RSD = "RSD"
    """Serbian dinar"""

    RUB = "RUB"
    """Russian ruble"""

    RWF = "RWF"
    """Rwandan franc"""

    SAR = "SAR"
    """Saudi riyal"""

    SBD = "SBD"
    """Solomon Islands dollar"""

    SCR = "SCR"
    """Seychelles rupee"""

    SDG = "SDG"
    """Sudanese pound"""

    SEK = "SEK"
    """Swedish krona"""

    SGD = "SGD"
    """Singapore dollar"""

    SHP = "SHP"
    """Saint Helena pound"""

    SLL = "SLL"
    """Sierra Leonean first leone"""

    SLE = "SLE"
    """Sierra Leonean second leone"""

    SOS = "SOS"
    """Somali shilling"""

    SRD = "SRD"
    """Surinamese dollar"""

    SSP = "SSP"
    """South Sudanese pound"""

    STD = "STD"
    """São Tomé and Príncipe dobra"""

    SVC = "SVC"
    """Salvadoran colón"""

    SYP = "SYP"
    """Syrian pound"""

    SZL = "SZL"
    """Swazi lilangeni"""

    THB = "THB"
    """Thai baht"""

    TJS = "TJS"
    """Tajikstani somoni"""

    TMT = "TMT"
    """Turkmenistan manat"""

    TND = "TND"
    """Tunisian dinar"""

    TOP = "TOP"
    """Tongan pa'anga"""

    TRY = "TRY"
    """Turkish lira"""

    TTD = "TTD"
    """Trinidad and Tobago dollar"""

    TWD = "TWD"
    """New Taiwan dollar"""

    TZS = "TZS"
    """Tanzanian shilling"""

    UAH = "UAH"
    """Ukrainian hryvnia"""

    UGX = "UGX"
    """Ugandan shilling"""

    USD = "USD"
    """United States dollar"""

    USN = "USN"
    """United States dollar (next day)"""

    USS = "USS"
    """United States dollar (same day)"""

    UYI = "UYI"
    """Uruguay Peso en Unidedades Indexadas"""

    UYU = "UYU"
    """Uruguyan peso"""

    UZS = "UZS"
    """Uzbekistan som"""

    VEF = "VEF"
    """Venezuelan bolívar soberano"""

    VND = "VND"
    """Vietnamese đồng"""

    VUV = "VUV"
    """Vanuatu vatu"""

    WST = "WST"
    """Samoan tala"""

    XAF = "XAF"
    """CFA franc BEAC"""

    XAG = "XAG"
    """Silver"""

    XAU = "XAU"
    """Gold"""

    XBA = "XBA"
    """European Composite Unit"""

    XBB = "XBB"
    """European Monetary Unit"""

    XBC = "XBC"
    """European Unit of Account 9"""

    XBD = "XBD"
    """European Unit of Account 17"""

    XCD = "XCD"
    """East Caribbean dollar"""

    XDR = "XDR"
    """Special drawing rights (International Monetary Fund)"""

    XOF = "XOF"
    """CFA franc BCEAO"""

    XPD = "XPD"
    """Palladium"""

    XPF = "XPF"
    """CFP franc"""

    XPT = "XPT"
    """Platinum"""

    XTS = "XTS"
    """Code reserved for testing"""

    XXX = "XXX"
    """No currency"""

    YER = "YER"
    """Yemeni rial"""

    ZAR = "ZAR"
    """South African rand"""

    ZMK = "ZMK"
    """Zambian kwacha"""

    ZMW = "ZMW"
    """Zambian kwacha"""

    BTC = "BTC"
    """Bitcoin"""

    XUS = "XUS"
    """USD Coin"""

    __str__ = str.__str__


CurrencyOrStr: TypeAlias = Annotated[Currency | str, open_enum_validator(Currency)]
