
### MongoDB client ###

# Descarga versión community: https://www.mongodb.com/try/download
# Instalación:https://www.mongodb.com/docs/manual/tutorial
# Módulo conexión MongoDB: pip install pymongo
# Ejecución: sudo mongod --dbpath "/path/a/la/base/de/datos/"
# Conexión: mongodb://localhost

# from pymongo import MongoClient
# Descomentar el db_client local o remoto correspondiente

# Base de datos local MongoDB
#db_client = MongoClient().local


# Base de datos remota MongoDB Atlas (https://mongodb.com)
# db_client = MongoClient(
#    "mongodb+srv://<user>:<password>@<url>/?retryWrites=true&w=majority").test

# Despliegue API en la nube:
# Deta - https://www.deta.sh/
# Intrucciones - https://fastapi.tiangolo.com/deployment/deta/b


### MySQL client ###

# Descarga versión community: https://dev.mysql.com/downloads/mysql/
# Instalación: https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/
# Módulo conexión MySQL: pip install mysql-connector-python
# Ejecución: sudo mysql -u root -p
# Conexión: mysql://localhost

# from mysql.connector import connect
# # Descomentar el db_client local o remoto correspondiente

# # definir variable db_client como global para poder usarla en otros archivos
# global db_client


# # Base de datos local MySQL
# db_client = mysql.connector.connect(
#     "localhost", "root", "password", "test").test

# # Base de datos remota MySQL
# db_client = mysql.connector.connect(
#     ""
# )
