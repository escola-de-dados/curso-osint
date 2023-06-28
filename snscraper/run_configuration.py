from alchemy import Osint
from json import load
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

# Esse código aqui deve ser executado apenas uma vez, para criar as tabelas no banco de dados
#
## Primeiramente precisamos pegar as informações de acesso ao banco de dados
with open("config.json") as jsonfile:
    db_config = load(jsonfile)['database_dml']

# Agora criamos o engine para o banco de dados
engine = create_engine(URL(db_config['drivername'], 
						   db_config['username'], db_config['password'], 
						   db_config['host'], db_config['port'], 
						   db_config['database']))

# Criamos as tabelas no banco de dados
# No nosso caso, somente uma tabela
Osint.__table__.create(bind=engine, checkfirst=True)