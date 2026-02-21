from pydantic import BaseModel, Field
from enum import Enum


# ── Country code enum (user sees uppercase, model receives lowercase) ───────

class CountryCodeEnum(str, Enum):
    AFG = "afg"; AGO = "ago"; ARG = "arg"; ARM = "arm"; BFA = "bfa"
    BGD = "bgd"; BIH = "bih"; BLZ = "blz"; BOL = "bol"; BRA = "bra"
    BRN = "brn"; BTN = "btn"; BWA = "bwa"; CHL = "chl"; CIV = "civ"
    COD = "cod"; COG = "cog"; COL = "col"; COM = "com"; CRI = "cri"
    CZE = "cze"; DOM = "dom"; ECU = "ecu"; EGY = "egy"; ESP = "esp"
    ETH = "eth"; FIN = "fin"; FRA = "fra"; GBR = "gbr"; GHA = "gha"
    GMB = "gmb"; GRC = "grc"; GTM = "gtm"; GUY = "guy"; HND = "hnd"
    HUN = "hun"; IDN = "idn"; IND = "ind"; ISR = "isr"; ITA = "ita"
    JAM = "jam"; JOR = "jor"; KEN = "ken"; KHM = "khm"; KOR = "kor"
    LAO = "lao"; LBN = "lbn"; LBR = "lbr"; LKA = "lka"; LSO = "lso"
    LTU = "ltu"; MDA = "mda"; MDG = "mdg"; MDV = "mdv"; MEX = "mex"
    MHL = "mhl"; MKD = "mkd"; MLI = "mli"; MMR = "mmr"; MNG = "mng"
    MUS = "mus"; MWI = "mwi"; MYS = "mys"; NAM = "nam"; NGA = "nga"
    NIC = "nic"; NPL = "npl"; PAK = "pak"; PAN = "pan"; PER = "per"
    PHL = "phl"; PRT = "prt"; PRY = "pry"; RUS = "rus"; RWA = "rwa"
    SDN = "sdn"; SEN = "sen"; SLV = "slv"; SVK = "svk"; SWE = "swe"
    SWZ = "swz"; THA = "tha"; TJK = "tjk"; TLS = "tls"; TON = "ton"
    TUN = "tun"; TUR = "tur"; TZA = "tza"; UGA = "uga"; USA = "usa"
    VNM = "vnm"; VUT = "vut"; WSM = "wsm"; ZAF = "zaf"; ZMB = "zmb"
    ZWE = "zwe"


# ── Country name enum (user sees title case, model receives lowercase) ──────

class CountryNameEnum(str, Enum):
    Afganistan = "afganistán"
    Angola = "angola"
    Argentina = "argentina"
    Armenia = "armenia"
    Bangladesh = "bangladesh"
    Belice = "belice"
    Bhutan = "bhután"
    Bolivia = "bolivia (estado plurinacional de)"
    Bosnia = "bosnia y herzegovina"
    Botswana = "botswana"
    Brasil = "brasil"
    Brunei = "brunei darussalam"
    Burkina_Faso = "burkina faso"
    Camboya = "camboya"
    Chequia = "chequia"
    Chile = "chile"
    Colombia = "colombia"
    Comoras = "comoras"
    Congo = "congo"
    Congo_Dem = "congo, rep. dem. del"
    Costa_Rica = "costa rica"
    Cote_Divoire = "côte d'ivoire"
    Ecuador = "ecuador"
    Egipto = "egipto"
    El_Salvador = "el salvador"
    Eslovaquia = "eslovaquia"
    Espana = "españa"
    Estados_Unidos = "estados unidos de américa"
    Eswatini = "eswatini"
    Etiopia = "etiopía"
    Federacion_Rusia = "federación rusia"
    Filipinas = "filipinas"
    Finlandia = "finlandia"
    Francia = "francia"
    Gambia = "gambia"
    Ghana = "ghana"
    Grecia = "grecia"
    Guatemala = "guatemala"
    Guyana = "guyana"
    Honduras = "honduras"
    Hungria = "hungría"
    India = "india"
    Indonesia = "indonesia"
    Islas_Marshall = "islas marshall"
    Israel = "israel"
    Italia = "italia"
    Jamaica = "jamaica"
    Jordania = "jordania"
    Kenya = "kenya"
    Lesotho = "lesotho"
    Liberia = "liberia"
    Lituania = "lituania"
    Libano = "líbano"
    Macedonia = "macedonia del norte"
    Madagascar = "madagascar"
    Malasia = "malasia"
    Malawi = "malawi"
    Maldivas = "maldivas"
    Mali = "malí"
    Mauricio = "mauricio"
    Mongolia = "mongolia"
    Myanmar = "myanmar"
    Mexico = "méxico"
    Namibia = "namibia"
    Nepal = "nepal"
    Nicaragua = "nicaragua"
    Nigeria = "nigeria"
    Pakistan = "pakistán"
    Panama = "panamá"
    Paraguay = "paraguay"
    Peru = "perú"
    Portugal = "portugal"
    Reino_Unido = "reino unido de gran bretaña e irlanda del norte"
    Corea = "república de corea"
    Moldova = "república de moldova"
    Laos = "república democrática popular lao"
    Rep_Dominicana = "república dominicana"
    Rwanda = "rwanda"
    Samoa = "samoa"
    Senegal = "senegal"
    Sri_Lanka = "sri lanka"
    Sudafrica = "sudáfrica"
    Sudan = "sudán"
    Suecia = "suecia"
    Tailandia = "tailandia"
    Tanzania = "tanzanía, república unida de"
    Tayikistan = "tayikistán"
    Timor_Leste = "timor-leste"
    Tonga = "tonga"
    Tunez = "túnez"
    Turkiye = "türkiye"
    Uganda = "uganda"
    Vanuatu = "vanuatu"
    Viet_Nam = "viet nam"
    Zambia = "zambia"
    Zimbabwe = "zimbabwe"


# ── Occupation code enum (user sees uppercase, model receives lowercase) ────

class OccupationCodeEnum(str, Enum):
    OCU_ISCO08_0 = "ocu_isco08_0"
    OCU_ISCO08_1 = "ocu_isco08_1"
    OCU_ISCO08_2 = "ocu_isco08_2"
    OCU_ISCO08_3 = "ocu_isco08_3"
    OCU_ISCO08_4 = "ocu_isco08_4"
    OCU_ISCO08_5 = "ocu_isco08_5"
    OCU_ISCO08_6 = "ocu_isco08_6"
    OCU_ISCO08_7 = "ocu_isco08_7"
    OCU_ISCO08_8 = "ocu_isco08_8"
    OCU_ISCO08_9 = "ocu_isco08_9"
    OCU_ISCO08_TOTAL = "ocu_isco08_total"
    OCU_ISCO08_X = "ocu_isco08_x"
    OCU_ISCO88_0 = "ocu_isco88_0"
    OCU_ISCO88_1 = "ocu_isco88_1"
    OCU_ISCO88_2 = "ocu_isco88_2"
    OCU_ISCO88_3 = "ocu_isco88_3"
    OCU_ISCO88_4 = "ocu_isco88_4"
    OCU_ISCO88_5 = "ocu_isco88_5"
    OCU_ISCO88_6 = "ocu_isco88_6"
    OCU_ISCO88_7 = "ocu_isco88_7"
    OCU_ISCO88_8 = "ocu_isco88_8"
    OCU_ISCO88_9 = "ocu_isco88_9"
    OCU_ISCO88_TOTAL = "ocu_isco88_total"
    OCU_ISCO88_X = "ocu_isco88_x"
    OCU_SKILL_L1 = "ocu_skill_l1"
    OCU_SKILL_L2 = "ocu_skill_l2"
    OCU_SKILL_L3_4 = "ocu_skill_l3-4"
    OCU_SKILL_TOTAL = "ocu_skill_total"
    OCU_SKILL_X = "ocu_skill_x"


# ── Occupation label enum (user sees title case, model receives lowercase) ──

class OccupationNameEnum(str, Enum):
    Isco08_0 = "ocupación (ciuo-08): 0. ocupaciones militares"
    Isco08_1 = "ocupación (ciuo-08): 1. directores y gerentes"
    Isco08_2 = "ocupación (ciuo-08): 2. profesionales científicos e intelectuales"
    Isco08_3 = "ocupación (ciuo-08): 3. técnicos y profesionales de nivel medio"
    Isco08_4 = "ocupación (ciuo-08): 4. personal de apoyo administrativo"
    Isco08_5 = "ocupación (ciuo-08): 5. trabajadores de los servicios y vendedores de comercios y mercados"
    Isco08_6 = "ocupación (ciuo-08): 6. agricultores y trabajadores calificados agropecuarios, forestales y pesqueros"
    Isco08_7 = "ocupación (ciuo-08): 7. oficiales, operarios y artesanos de artes mecánicas y de otros oficios"
    Isco08_8 = "ocupación (ciuo-08): 8. operadores de instalaciones y máquinas y ensambladores"
    Isco08_9 = "ocupación (ciuo-08): 9. ocupaciones elementales"
    Isco08_Total = "ocupación (ciuo-08): total"
    Isco08_X = "ocupación (ciuo-08): x. no clasificados en otra parte"
    Isco88_0 = "ocupación (ciuo-88): 0. fuerzas armadas"
    Isco88_1 = "ocupación (ciuo-88): 1. miembros del poder ejecutivo y de los cuerpos legislativos y personal directivo de la administración pública y de empresas"
    Isco88_2 = "ocupación (ciuo-88): 2. profesionales científicos e intelectuales"
    Isco88_3 = "ocupación (ciuo-88): 3. técnicos y profesionales de nivel medio"
    Isco88_4 = "ocupación (ciuo-88): 4. empleados de oficina"
    Isco88_5 = "ocupación (ciuo-88): 5. trabajadores de los servicios y vendedores de comercios y mercados"
    Isco88_6 = "ocupación (ciuo-88): 6. agricultores y trabajadores calificados agropecuarios y pesqueros"
    Isco88_7 = "ocupación (ciuo-88): 7. oficiales, operarios y artesanos de artes mecánicas y de otros oficios"
    Isco88_8 = "ocupación (ciuo-88): 8. operadores de instalaciones y máquinas y montadores"
    Isco88_9 = "ocupación (ciuo-88): 9. trabajadores no calificados"
    Isco88_Total = "ocupación (ciuo-88): total"
    Isco88_X = "ocupación (ciuo-88): x. no pueden clasificarse según la ocupación"
    Skill_L1 = "ocupación (nivel de competencia): nivel de competencia 1 ~ bajo"
    Skill_L2 = "ocupación (nivel de competencia): nivel de competencia 2 ~ medio"
    Skill_L3_4 = "ocupación (nivel de competencia): niveles de competencia 3 y 4 ~ altos"
    Skill_X = "ocupación (nivel de competencia): no clasificados en otra parte"
    Skill_Total = "ocupación (nivel de competencia): total"


# ── Observation status enum ─────────────────────────────────────────────────

class ObservationStatusEnum(str, Enum):
    Poco_Fiable = "poco fiable"
    Ruptura_De_Serie = "ruptura de serie"
    Empty = ""


# ── Input and output schemas ────────────────────────────────────────────────

class PredictionInput(BaseModel):
    """
    Input schema for gender pay gap prediction.

    Field aliases provide user-friendly names in the API documentation
    while internal attribute names maintain consistency with the
    original training data column names.
    """

    # Categorical identifiers
    ref_area: CountryCodeEnum = Field(alias="country_code")
    ref_area_label: CountryNameEnum = Field(alias="country_name")
    classif1: OccupationCodeEnum = Field(alias="occupation_code")
    classif1_label: OccupationNameEnum = Field(alias="occupation_name")
    obs_status_label: ObservationStatusEnum = Field(alias="observation_status")

    # Temporal variable
    time: int = Field(alias="year")

    # Employment figures by gender (in thousands)
    obs_value_employees_women: float = Field(alias="employees_women")
    obs_value_employees_men: float = Field(alias="employees_men")

    # Average hourly earnings by gender (local currency)
    obs_value_earnings_women: float = Field(alias="earnings_women")
    obs_value_earnings_men: float = Field(alias="earnings_men")

    # Average weekly hours worked by gender
    obs_value_hours_women: float = Field(alias="hours_women")
    obs_value_hours_men: float = Field(alias="hours_men")

    # Derived ratio and difference features
    earnings_ratio: float = Field(alias="earnings_ratio")
    hours_ratio: float = Field(alias="hours_ratio")
    employment_ratio: float = Field(alias="employment_ratio")
    delta_earnings: float = Field(alias="delta_earnings")
    delta_hours: float = Field(alias="delta_hours")

    model_config = {"populate_by_name": True}


class PredictionOutput(BaseModel):
    """
    Output schema for prediction response.

    Returns the predicted gender pay gap as a percentage
    along with a status message.
    """
    predicted_pay_gap: float
    message: str