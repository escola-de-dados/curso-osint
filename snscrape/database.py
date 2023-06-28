from alchemy import Osint
from json import load

from datetime import timedelta, datetime

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker


# Cria o engine para o banco de dados, usando as informações do arquivo config.json	
with open("config.json") as jsonfile:
    db_config = load(jsonfile)['database_dml']

engine = create_engine(URL(db_config['drivername'], db_config['username'],
                           db_config['password'], db_config['host'],
                           db_config['port'], db_config['database']))


# Insere um tweet no banco de dados
def insert_tweet(tweet):
    # Cria uma sessão para o banco de dados
    Session = sessionmaker(bind=engine)
    session = Session()
    
	# Cria um objeto Osint com os dados do tweet
    new = Osint(twitter_id=tweet['id'], text=tweet['rawContent'], created_at=datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S+00:00') + timedelta(hours=3))
    
	# Adiciona o objeto ao banco de dados
    session.add(new)
    
	# Commita as mudanças
    session.commit()
    
	# Fecha a sessão
    session.close()