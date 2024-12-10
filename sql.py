# senha banco: fiap23112024
# master user name: fiaptc & fiaptc2 & fiaptc3
import psycopg2
from typing import Union


class SQL:
    
    def __init__(self):
        
        self.conn = None
        self._connection = None

    
    def closeConnection(self):
        try:
            if self.conn is not None:
                self.conn.close()
                self.connection.close()
                
            self.conn = None
            self._connection = None
      
        except Exception as ex:
            print(f"ERRO closeConnection - {str(ex)}")    
        
        
    def connect(self):
        if self._connection is None:
            
            # Acess to PostgreSQL AWS.
            host = "database-3.cnwvjmmuwln2.us-east-1.rds.amazonaws.com"
            database = "creditCard"
            user = "fiaptc3"
            password = "fiap23112024"
            port = 5432

            try:
                # Estabelecendo a conexão
                self._connection = psycopg2.connect(
                    host=host,
                    database=database,
                    user=user,
                    password=password,
                    port=port
                )
                print("Conexão bem-sucedida!")

                # Criando um cursor
                
                return self._connection 
            
            except psycopg2.Error as ex:
                print(f"Erro ao conectar ao PostgreSQL: {ex}")
                self._connection = None

        else:
            return self._connection


    def formatQuery(self, query: Union[str, tuple]):
        if isinstance(query, str):
            parameters = None
                
        elif isinstance(query, tuple) or isinstance(list, query):
            query, parameters = query
        
        else:
            print("PARÂMETRO NÃO SUPORTADO")
            return "", ""
        
        query = query.replace("\n", "")
        
        return query, parameters
    
    
    def sqlExecute(self, query: Union[str, tuple], closeConn=True):
        """
            USE TO: INSERT, UPDATE, DELETE
            *** closeConn: If use to INSERT/ UPDATE using FOR change to False ***
        """
        try:
            query, parameters = self.formatQuery(query)
            
            connection = self.connect()
            conn = connection.cursor()
            conn.execute(query, parameters)
            connection.commit()

            if closeConn:
                self.closeConnection()
                
            print("COMANDO EFETUADO COM SUCESSO !")
            
        except Exception as ex:
            print(f"ERRO sqlExecute - {str(ex)}")
            self.closeConnection()


    def sqlSelect(self, query:str, closeConn=True):
        "USE TO: SELECT"
        try:
            query = query.replace("\n", "")
            connection = self.connect()
            conn = connection.cursor()
            conn.execute(query)
            print("COMANDO EFETUADO COM SUCESSO !")
            result = conn.fetchall()
            
            if closeConn:
                self.closeConnection()
                
            return result
            
        except Exception as ex:
            print(f"ERRO sqlSelect - {str(ex)}")
            self.closeConnection()
        

_sql = SQL()    
def sqlExecute(query: Union[str, tuple], closeConn=True):
    return _sql.sqlExecute(query, closeConn)
    
    
def sqlSelect(query:str, closeConn=True):
    return _sql.sqlSelect(query, closeConn)
