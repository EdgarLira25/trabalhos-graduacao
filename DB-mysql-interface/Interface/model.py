from typing import NamedTuple

class Hotel(NamedTuple):
    Numero_Registro_Imobiliario : int
    Nome_Fantasia : str
    Tamanho_m2 : int
    Categoria : str
    Loc_Logradouro : str
    Loc_Bairro : str
    Loc_Numero : int
    Loc_Cidade : str
    Loc_CEP : int
    Loc_Estado : str
    Registro_da_rede : int

class Patrocinadores(NamedTuple):
    Nome : str
    Tipo_de_patrocinio : str
    Data_de_Inicio : str
    CNPJ : int

class Patrocinam(NamedTuple):
    Numero_Registro_Imobiliario : int
    CNPJ : int