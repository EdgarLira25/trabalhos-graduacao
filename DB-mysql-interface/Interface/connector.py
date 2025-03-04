"MODULO DE CONEXÃO COM MYSQL"
from configparser import ConfigParser
from model import Hotel, Patrocinam, Patrocinadores
import mysql.connector

config = ConfigParser()

class DB:

   def __init__(self, host: str, dbase: str,
                 user: str, passw: str, port: str) -> None:
        self.con = mysql.connector.connect(
            host=host,
            database=dbase,
            user=user,
            password=passw,
            port=port,
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.con.cursor()

   def select_all(self, table_name : str):
      self.cursor.execute(f"SELECT * FROM {table_name}")
      resp = self.cursor.fetchall()
      return resp

   def select_especific_value(self, collumn : str, value : str, table_name):
      self.cursor.execute(f"SELECT * FROM {table_name} WHERE {collumn} = '{value}' ")
      resp = self.cursor.fetchall()
      return resp

   def insert_hotel(self, hotel : Hotel):
      try:
         sql = f"""INSERT INTO HOTEL VALUES 
               ({hotel.Numero_Registro_Imobiliario}, '{hotel.Nome_Fantasia}',
               {hotel.Tamanho_m2},'{hotel.Categoria}','{hotel.Loc_Logradouro}',
               '{hotel.Loc_Bairro}',{hotel.Loc_Numero},'{hotel.Loc_Cidade}',
               {hotel.Loc_CEP},'{hotel.Loc_Estado}',{hotel.Registro_da_rede});   
               """.strip()
         self.cursor.execute(sql)
         self.con.commit()
         return True
      except Exception as e:
         print(e)
         return False

   def delete_hotel(self, Numero_Registro_Imobiliario : int):
      try:
         sql = f"""
            DELETE FROM HOTEL 
            WHERE Numero_Registro_Imobiliario = '{Numero_Registro_Imobiliario}';
         """.strip()
         self.cursor.execute(sql)
         self.con.commit()
         return True
      except Exception as e:
         print(e)
         return False

   def alter_hotel(self, Numero_Registro_Imobiliario : int, collumn : str, value : str):
      try:
         sql = f"""
            UPDATE HOTEL SET {collumn} = '{value}' 
            WHERE Numero_Registro_Imobiliario = {Numero_Registro_Imobiliario};
         """.strip()
         self.cursor.execute(sql)
         self.con.commit()
         return True
      except Exception as e:
         print(e)
         return False

   def insert_patrocinadores(self, patrocinadores : Patrocinadores ):
      try:
         sql = f"""INSERT INTO PATROCINADORES VALUES 
               ('{patrocinadores.Nome}', '{patrocinadores.Tipo_de_patrocinio}',
               '{patrocinadores.Data_de_Inicio}',{patrocinadores.CNPJ}); 
               """.strip()
         self.cursor.execute(sql)
         self.con.commit()
         return True

      except Exception as e:
         print(e)
         return False

   def delete_patrocinadores(self, CNPJ : int):
      try:
         sql = f"""
            DELETE FROM PATROCINADORES 
            WHERE CNPJ = '{CNPJ}';
         """.strip()
         self.cursor.execute(sql)
         self.con.commit()
         return True

      except Exception as e:
         print(e)
         return False

   def alter_patrocinadores(self, CNPJ : int, collumn : str, value : str):
      try:
         sql = f"""
            UPDATE PATROCINADORES SET {collumn} = '{value}' 
            WHERE CNPJ = {CNPJ};
         """.strip()
         self.cursor.execute(sql)
         self.con.commit()
         return True

      except Exception as e:
         print(e)
         return False
   

   def insert_patrocinam(self, patrocinam : Patrocinam):
      try:
         sql = f"""INSERT INTO PATROCINAM VALUES 
               ({patrocinam.Numero_Registro_Imobiliario}, {patrocinam.CNPJ}); 
               """.strip()
         self.cursor.execute(sql)
         self.con.commit()
         return True

      except Exception as e:
         print(e)
         return False
   
   def delete_patrocinam(self, Numero_Registro_Imobiliario : int, CNPJ : int):
      try:
         sql = f"""
            DELETE FROM PATROCINAM 
            WHERE Numero_Registro_Imobiliario = '{Numero_Registro_Imobiliario}' AND CNPJ = '{CNPJ}';
         """.strip()
         self.cursor.execute(sql)
         self.con.commit()
         return True

      except Exception as e:
         print(e)
         return False

   def alter_patrocinam(self, Numero_Registro_Imobiliario : int, CNPJ :int,  collumn : str, value : str):
      try:
         sql = f"""
            UPDATE PATROCINAM SET {collumn} = '{value}' 
            WHERE Numero_Registro_Imobiliario = {Numero_Registro_Imobiliario} AND CNPJ = {CNPJ};
         """.strip()
         self.cursor.execute(sql)
         self.con.commit()
         return True

      except Exception as e:
         print(e)
         return False
