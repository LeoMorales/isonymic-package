# -*- coding: utf-8 -*-
import pandas as pd
import warnings
from typing import Optional


# Constants
PROVINCE_NAME_BY_ID_DICT = {
    "02": "Ciudad Autónoma de Buenos Aires",
    "06": "Buenos Aires",
    "10": "Catamarca",
    "14": "Córdoba",
    "18": "Corrientes",
    "22": "Chaco",
    "26": "Chubut",
    "30": "Entre Ríos",
    "34": "Formosa",
    "38": "Jujuy",
    "42": "La Pampa",
    "46": "La Rioja",
    "50": "Mendoza",
    "54": "Misiones",
    "58": "Neuquén",
    "62": "Río Negro",
    "66": "Salta",
    "70": "San Juan",
    "74": "San Luis",
    "78": "Santa Cruz",
    "82": "Santa Fe",
    "86": "Santiago del Estero",
    "90": "Tucumán",
    "94": "Tierra del Fuego, Antártida e Islas del Atlántico Sur",
}

REGION_BY_PROVINCE_CODE_DICT = {
    "38": "NOA",
    "66": "NOA",
    "34": "NEA",
    "22": "NEA",
    "10": "NOA",
    "86": "NOA",
    "54": "NEA",
    "90": "NOA",
    "18": "NEA",
    "46": "NOA",
    "82": "Centro",
    "70": "Cuyo",
    "14": "Centro",
    "30": "NEA",
    "74": "Cuyo",
    "50": "Cuyo",
    "06": "Centro",
    "02": "Centro",
    "42": "Centro",
    "58": "Patagonia",
    "62": "Patagonia",
    "26": "Patagonia",
    "78": "Patagonia",
    "94": "Patagonia",
}

DEPARTMENT_NAME_BY_ID_DICT = {
    "06280": "General Alvarado",
    "06357": "General Pueyrredón",
    "06518": "Mar Chiquita",
    "06868": "Villa Gesell",
    "06644": "Pinamar",
    "06336": "General Lavalle",
    "06420": "La Costa",
    "10084": "Pomán",
    "06505": "Magdalena",
    "06861": "Vicente López",
    "50042": "La Paz",
    "06196": "Coronel Pringles",
    "06805": "Tigre",
    "66035": "Cerrillos",
    "06056": "Bahía Blanca",
    "14070": "Minas",
    "14077": "Pocho",
    "14119": "Río Segundo",
    "86063": "Choya",
    "06819": "Tornquist",
    "06854": "25 de Mayo",
    "06588": "9 de Julio",
    "14161": "Tercero Arriba",
    "06301": "General Belgrano",
    "10042": "Capayán",
    "06547": "Monte",
    "06693": "Roque Pérez",
    "06638": "Pilar",
    "06210": "Chacabuco",
    "06469": "Lincoln",
    "06364": "General Rodríguez",
    "06784": "Suipacha",
    "06483": "Lobos",
    "06287": "General Alvear",
    "06658": "Quilmes",
    "06798": "Tapalqué",
    "14021": "Colón",
    "62084": "Valcheta",
    "62077": "San Antonio",
    "38056": "San Antonio",
    "62049": "9 de julio",
    "58105": "Picunches",
    "06602": "Patagones",
    "74056": "Juan Martín de Pueyrredón",
    "74035": "General Pedernera",
    "74014": "Belgrano",
    "74049": "Junín",
    "58098": "Picún Leufú",
    "58112": "Zapala",
    "50119": "Tunuyán",
    "10063": "Fray Mamerto Esquiú",
    "50049": "Las Heras",
    "62063": "Pichi Mahuida",
    "62007": "Adolfo Alsina",
    "66105": "Los Andes",
    "66126": "Orán",
    "34063": "Ramón Lista",
    "66084": "La Candelaria",
    "82035": "Garay",
    "82070": "Las Colonias",
    "70133": "Zonda",
    "54007": "Apóstoles",
    "06623": "Pergamino",
    "22126": "1ro. de Mayo",
    "10112": "San Isidro",
    "06035": "Avellaneda",
    "46035": "Chamical",
    "74063": "Libertador General San Martín",
    "74021": "Coronel Pringles",
    "74028": "Chacabuco",
    "06735": "San Antonio de Areco",
    "22112": "O¨Higgins",
    "06560": "Moreno",
    "06427": "La Matanza",
    "30015": "Concordia",
    "30035": "Federal",
    "30056": "Gualeguaychú",
    "30063": "Islas del Ibicuy",
    "30105": "Victoria",
    "30021": "Diamante",
    "30098": "Uruguay",
    "30084": "Paraná",
    "06707": "Saladillo",
    "06455": "Las Flores",
    "06686": "Rojas",
    "06252": "Escobar",
    "06412": "José C. Paz",
    "86014": "Alberdi",
    "86098": "Juan F. Ibarra",
    "86077": "General Taboada",
    "74042": "Gobernador Dupuy",
    "06511": "Maipú",
    "06343": "General Paz",
    "06308": "General Guido",
    "06315": "General Juan Madariaga",
    "06791": "Tandil",
    "06203": "Coronel Suárez",
    "06014": "Adolfo Gonzales Chaves",
    "66014": "Cachi",
    "66042": "Chicoana",
    "66098": "La Viña",
    "06672": "Rauch",
    "66112": "Metán",
    "66119": "Molinos",
    "14028": "Cruz del Eje",
    "14091": "Punilla",
    "14147": "Santa María",
    "86154": "Rivadavia",
    "86126": "Ojo de Agua",
    "66007": "Anta",
    "26084": "Río Senguer",
    "62021": "Bariloche",
    "38021": "Dr. Manuel Belgrano",
    "38070": "Santa Bárbara",
    "38049": "Rinconada",
    "06721": "Salliqueló",
    "06091": "Berazategui",
    "66049": "General Güemes",
    "66154": "San Carlos",
    "14126": "San Alberto",
    "50112": "Santa Rosa",
    "66091": "La Poma",
    "26007": "Biedma",
    "18126": "Saladas",
    "50084": "Rivadavia",
    "62028": "Conesa",
    "26042": "Gaiman",
    "26077": "Rawson",
    "46077": "General Lamadrid",
    "74007": "Ayacucho",
    "18063": "General Paz",
    "06351": "General Pinto",
    "06742": "San Cayetano",
    "06833": "Tres Arroyos",
    "06189": "Coronel Dorrego",
    "06581": "Necochea",
    "46105": "Independencia",
    "46084": "General Ocampo",
    "14140": "San Justo",
    "14182": "Unión",
    "46007": "Arauco",
    "06466": "Lezama",
    "06217": "Chascomús",
    "06218": "Chascomús",
    "06655": "Punta Indio",
    "38014": "El Carmen",
    "10091": "Santa María",
    "06126": "Campana",
    "10098": "Santa Rosa",
    "10070": "La Paz",
    "78042": "Magallanes",
    "78007": "Corpen Aike",
    "14175": "Tulumba",
    "14098": "Río Cuarto",
    "50126": "Tupungato",
    "34042": "Pilagás",
    "34021": "Laishí",
    "34056": "Pirané",
    "22063": "General Güemes",
    "02042": "Comuna 6",
    "22036": "12 de Octubre",
    "62056": "Ñorquinco",
    "62091": "25 de Mayo",
    "50105": "San Rafael",
    "26105": "Telsen",
    "62070": "Pilcaniyeu",
    "06007": "Adolfo Alsina",
    "06028": "Almirante Brown",
    "06616": "Pellegrini",
    "46063": "General Belgrano",
    "86056": "Copo",
    "58049": "Huiliches",
    "58021": "Catán Lil",
    "30077": "Nogoyá",
    "30091": "Tala",
    "30049": "Gualeguay",
    "30028": "Federación",
    "30070": "La Paz",
    "30042": "Feliciano",
    "22007": "Almirante Brown",
    "66140": "Rosario de la Frontera",
    "58028": "Collón Curá",
    "06651": "Puán",
    "06875": "Villarino",
    "58070": "Los Lagos",
    "58056": "Lácar",
    "10035": "Belén",
    "58035": "Confluencia",
    "14084": "Presidente Roque Saenz Peña",
    "58014": "Añelo",
    "58063": "Loncopué",
    "58084": "Ñorquín",
    "10049": "Capital",
    "10014": "Ancasti",
    "58091": "Pehuenches",
    "58077": "Minas",
    "58042": "Chos Malal",
    "26014": "Cushamen",
    "78035": "Lago Buenos Aires",
    "06392": "General Villegas",
    "14035": "General Roca",
    "50014": "General Alvear",
    "66077": "La Caldera",
    "86147": "Río Hondo",
    "46098": "Vinchina",
    "42147": "Trenel",
    "46014": "Capital",
    "14112": "Río Seco",
    "62014": "Avellaneda",
    "62042": "General Roca",
    "02014": "Comuna 2",
    "50028": "Guaymallén",
    "14056": "Juárez Celman",
    "02056": "Comuna 8",
    "86084": "Guasayán",
    "66028": "La Capital",
    "14154": "Sobremonte",
    "94015": "Ushuaia",
    "94008": "Río Grande",
    "02091": "Comuna 13",
    "78021": "Güer Aike",
    "14014": "Capital",
    "10028": "Antofagasta de la Sierra",
    "50091": "San Carlos",
    "86035": "Banda",
    "26070": "Paso de Indios",
    "50063": "Luján de Cuyo",
    "26035": "Futaleufú",
    "78049": "Río Chico",
    "78028": "Lago Argentino",
    "62035": "El Cuy",
    "26063": "Mártires",
    "86182": "Sarmiento",
    "78014": "Deseado",
    "26056": "Languiñeo",
    "86042": "Belgrano",
    "86007": "Aguirre",
    "22091": "Maipú",
    "50056": "Lavalle",
    "50077": "Malargüe",
    "02021": "Comuna 3",
    "86189": "Silípica",
    "86161": "Robles",
    "86105": "Loreto",
    "06648": "Presidente Perón",
    "86049": "Capital",
    "30008": "Colón",
    "30113": "Villaguay",
    "06168": "Castelli",
    "30088": "San Salvador",
    "66021": "Cafayate",
    "02098": "Comuna 14",
    "46021": "Castro Barros",
    "06847": "Tres Lomas",
    "02035": "Comuna 5",
    "06441": "La Plata",
    "42119": "Quemú Quemú",
    "06448": "Laprida",
    "06119": "Brandsen",
    "42126": "Rancul",
    "06147": "Carlos Casares",
    "42035": "Conhelo",
    "06700": "Saavedra",
    "06154": "Carlos Tejedor",
    "22133": "Quitilipi",
    "06609": "Pehuajó",
    "06826": "Trenque Lauquen",
    "06595": "Olavarría",
    "06539": "Merlo",
    "22056": "General Donovan",
    "06260": "Esteban Echeverría",
    "06077": "Arrecifes",
    "06140": "Capitán Sarmiento",
    "22028": "Chacabuco",
    "06161": "Carmen de Areco",
    "06714": "Salto",
    "06266": "Exaltación de la Cruz",
    "06760": "San Miguel",
    "06728": "San Andrés de Giles",
    "06413": "Junín",
    "06042": "Ayacucho",
    "06399": "Guaminí",
    "06245": "Ensenada",
    "06532": "Mercedes",
    "06497": "Luján",
    "06756": "San Isidro",
    "06084": "Benito Juárez",
    "06175": "Colón",
    "06408": "Hurlingham",
    "42021": "Capital",
    "06568": "Morón",
    "06515": "Malvinas Argentinas",
    "06410": "Ituzaingó",
    "06840": "Tres de Febrero",
    "46028": "Coronel Felipe Varela",
    "06224": "Chivilcoy",
    "06021": "Alberti",
    "06112": "Bragado",
    "06329": "General Las Heras",
    "06525": "Marcos Paz",
    "06385": "General Viamonte",
    "06270": "José M. Ezeiza",
    "06274": "Florencio Varela",
    "06574": "Navarro",
    "06134": "Cañuelas",
    "86070": "Figueroa",
    "06778": "San Vicente",
    "06630": "Pila",
    "06322": "General La Madrid",
    "06105": "Bolívar",
    "06553": "Monte Hermoso",
    "06476": "Lobería",
    "06098": "Berisso",
    "06812": "Tordillo",
    "06749": "San Fernando",
    "06882": "Zárate",
    "06665": "Ramallo",
    "06763": "San Nicolás",
    "86168": "Salavina",
    "86133": "Pellegrini",
    "86028": "Avellaneda",
    "06063": "Balcarce",
    "06406": "Hipólito Yrigoyen",
    "86119": "Moreno",
    "06238": "Dolores",
    "06049": "Azul",
    "06231": "Daireaux",
    "50021": "Godoy Cruz",
    "50070": "Maipú",
    "66063": "Guachipas",
    "50007": "Capital",
    "14133": "San Javier",
    "14105": "Río Primero",
    "50035": "Junín",
    "18168": "Santo Tomé",
    "46126": "Sanagasta",
    "46056": "General Ángel V. Peñaloza",
    "46042": "Chilecito",
    "42028": "Catriló",
    "38063": "San Pedro",
    "38105": "Valle Grande",
    "46070": "General Juan F. Quiroga",
    "46112": "Rosario Vera Peñaloza",
    "10105": "Tinogasta",
    "14063": "Marcos Juárez",
    "90119": "Yerba Buena",
    "90105": "Tafí Viejo",
    "46091": "General San Martín",
    "42007": "Atreucó",
    "54119": "25 de Mayo",
    "46049": "Famatina",
    "54098": "San Ignacio",
    "46119": "San Blas de Los Sauces",
    "42070": "Guatraché",
    "42084": "Lihuel Calel",
    "34014": "Formosa",
    "10021": "Andalgalá",
    "10007": "Ambato",
    "10077": "Paclín",
    "34049": "Pilcomayo",
    "10056": "El Alto",
    "26098": "Tehuelches",
    "26021": "Escalante",
    "14049": "Ischilín",
    "14168": "Totoral",
    "14042": "General San Martín",
    "06462": "Leandro N. Alem",
    "22084": "Libertador General San Martín",
    "26049": "Gastre",
    "06294": "General Arenales",
    "22014": "Bermejo",
    "14007": "Calamuchita",
    "18175": "Sauce",
    "06679": "Rivadavia",
    "54063": "Iguazú",
    "02063": "Comuna 9",
    "58007": "Aluminé",
    "26091": "Sarmiento",
    "02007": "Comuna 1",
    "02028": "Comuna 4",
    "02084": "Comuna 12",
    "34028": "Matacos",
    "38094": "Tilcara",
    "38042": "Palpalá",
    "02049": "Comuna 7",
    "34035": "Patiño",
    "34007": "Bermejo",
    "38084": "Susques",
    "66070": "Iruya",
    "42140": "Toay",
    "38007": "Cochinoca",
    "38098": "Tumbaya",
    "02070": "Comuna 10",
    "90007": "Burruyacú",
    "90112": "Trancas",
    "90098": "Tafí del Valle",
    "42042": "Curacó",
    "22161": "Tapenagá",
    "02077": "Comuna 11",
    "70105": "Sarmiento",
    "70014": "Angaco",
    "18035": "Curuzu Cuatia",
    "18147": "San Martín",
    "18105": "Mercedes",
    "86175": "San Martín",
    "86112": "Mitre",
    "86021": "Atamisqui",
    "18119": "Paso de los Libres",
    "18070": "Goya",
    "18091": "Lavalle",
    "18161": "San Roque",
    "18056": "General Alvear",
    "18028": "Concepción",
    "18007": "Bella Vista",
    "86091": "Jiménez",
    "06182": "Coronel de Marina Leonardo Rosales",
    "06070": "Baradero",
    "06770": "San Pedro",
    "66161": "Santa Victoria",
    "66056": "General José de San Martín",
    "66133": "Rivadavia",
    "66147": "Rosario de Lerma",
    "38035": "Ledesma",
    "38028": "Humahuaca",
    "38112": "Yaví",
    "38077": "Santa Catalina",
    "06277": "Florentino Ameghino",
    "26028": "Florentino Ameghino",
    "90049": "La Cocha",
    "90035": "Graneros",
    "90042": "Juan Bautista Alberdi",
    "90077": "Río Chico",
    "90091": "Simoca",
    "90021": "Chicligasta",
    "90070": "Monteros",
    "90056": "Leales",
    "90028": "Famaillá",
    "90084": "Capital",
    "90014": "Cruz Alta",
    "90063": "Lules",
    "82042": "General López",
    "82028": "Villa Constitución",
    "82014": "Caseros",
    "82084": "Rosario",
    "82119": "San Lorenzo",
    "82056": "Iriondo",
    "82007": "Belgrano",
    "82105": "San Jerónimo",
    "70028": "Capital",
    "70126": "25 de Mayo",
    "82126": "San Martín",
    "82063": "La Capital",
    "42056": "Chapaleufú",
    "54091": "Oberá",
    "82021": "Castellanos",
    "82112": "San Justo",
    "82091": "San Cristóbal",
    "82098": "San Javier",
    "82049": "General Obligado",
    "82133": "Vera",
    "82077": "9 de Julio",
    "70049": "Iglesia",
    "70119": "Valle Fértil",
    "70112": "Ullum",
    "70007": "Albardón",
    "42133": "Realicó",
    "70042": "Chimbas",
    "42105": "Maracó",
    "70091": "San Martín",
    "70084": "Rivadavia",
    "70098": "Santa Lucía",
    "70063": "9 de Julio",
    "70077": "Rawson",
    "70070": "Pocito",
    "70035": "Caucete",
    "42154": "Utracán",
    "42098": "Loventué",
    "42077": "Hucal",
    "42014": "Caleu Caleu",
    "42091": "Limay Mahuida",
    "42112": "Puelén",
    "42049": "Chalileo",
    "42063": "Chical Co",
    "86140": "Quebrachos",
    "18112": "Monte Caseros",
    "18049": "Esquina",
    "18098": "Mbucuruyá",
    "18154": "San Miguel",
    "18042": "Empedrado",
    "18084": "Ituzaingó",
    "18021": "Capital",
    "18140": "San Luis del Palmar",
    "18133": "San Cosme",
    "18077": "Itatí",
    "18014": "Berón de Astrada",
    "94011": "Tolhuin",
    "54028": "Capital",
    "54021": "Candelaria",
    "54014": "Cainguás",
    "54077": "Libertador General San Martín",
    "54049": "General Manuel Belgrano",
    "54056": "Guaraní",
    "54070": "Leandro N. Alem",
    "54105": "San Javier",
    "54035": "Concepción",
    "54084": "Montecarlo",
    "54042": "Eldorado",
    "54112": "San Pedro",
    "22119": "Presidencia de la Plaza",
    "22154": "Sargento Cabral",
    "22070": "Independencia",
    "22098": "Mayor Luis Jorge Fontana",
    "22043": "Fray Justo Santamaría de Oro",
    "22105": "9 de Julio",
    "22039": "2 de Abril",
    "06434": "Lanús",
    "22140": "San Fernando",
    "22147": "San Lorenzo",
    "06490": "Lomas de Zamora",
    "22049": "General Belgrano",
    "22168": "25 de Mayo",
    "22077": "Libertad",
    "22021": "Comandante Fernandez",
    "02105": "Comuna 15",
    "70056": "Jáchal",
    "70021": "Calingasta",
    "06371": "General San Martín",
    "50098": "San Martín",
    "94028": "Antártida Argentina",
}

REGION_CODE_BY_REGION_NAME_DICT = {
    "NOA": "01",
    "NEA": "02",
    "Centro": "03",
    "Cuyo": "04",
    "Patagonia": "05",
}


# Functions
def is_region(presumed_region: str) -> bool:
    """Check if the given name is a valid region in Argentina.

    Args:
        presumed_region (str): A region name of Argentina.

    Returns:
        bool: True if it is a valid region of Argentina, False otherwise.
    """
    return presumed_region in REGION_CODE_BY_REGION_NAME_DICT


def is_province(presumed_province: str) -> bool:
    """Check if the given name is a valid province in Argentina.

    Args:
        presumed_province (str): A province name of Argentina.

    Returns:
        bool: True if it is a valid province of Argentina, False otherwise.
    """
    return presumed_province in PROVINCE_NAME_BY_ID_DICT.values()


def append_cell_codes_deprecated(
    df: pd.DataFrame, department_code_column: str = "departamento_id"
) -> pd.DataFrame:
    """Append department, province, and region information to the dataframe.

    Deprecated: Use `append_cell_description` instead.

    Args:
        df (pd.DataFrame): The input dataframe.
        department_code_column (str): The column name for department codes.

    Returns:
        pd.DataFrame: DataFrame with added columns for department, province, and region names.
    """
    warnings.warn(
        "append_cell_codes_deprecated is deprecated. Use append_cell_description instead.",
        DeprecationWarning,
    )
    return append_cell_description(df, department_code_column)


def append_cell_description(
    df: pd.DataFrame, department_code_column: str = "departamento_id"
) -> pd.DataFrame:
    """Add department, province, and region information to the dataframe.

    Args:
        df (pd.DataFrame): The input dataframe.
        department_code_column (str): The column name for department codes.

    Returns:
        pd.DataFrame: DataFrame with added columns for department, province, and region information.
    """
    df_output = df.copy()

    df_output["departamento_nombre"] = df_output[department_code_column].map(
        DEPARTMENT_NAME_BY_ID_DICT
    )
    df_output["provincia_id"] = df_output[department_code_column].str.slice(0, 2)
    df_output["provincia_nombre"] = df_output["provincia_id"].map(
        PROVINCE_NAME_BY_ID_DICT
    )
    df_output["region_nombre"] = df_output["provincia_id"].map(
        REGION_BY_PROVINCE_CODE_DICT
    )
    df_output["region_id"] = df_output["region_nombre"].map(
        REGION_CODE_BY_REGION_NAME_DICT
    )

    return df_output


def append_province_description(
    df: pd.DataFrame, province_code_column: str = "province_id"
) -> pd.DataFrame:
    """Add province and region information to the dataframe.

    Args:
        df (pd.DataFrame): The input dataframe.
        province_code_column (str): The column name for province codes.

    Returns:
        pd.DataFrame: DataFrame with added columns for province and region information.
    """
    df_output = df.copy()

    df_output["provincia_nombre"] = df_output[province_code_column].map(
        PROVINCE_NAME_BY_ID_DICT
    )
    df_output["region_nombre"] = df_output[province_code_column].map(
        REGION_BY_PROVINCE_CODE_DICT
    )
    df_output["region_id"] = df_output["region_nombre"].map(
        REGION_CODE_BY_REGION_NAME_DICT
    )

    return df_output
