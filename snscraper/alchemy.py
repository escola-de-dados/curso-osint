from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

# Classe que representa a tabela OSINT no banco de dados
class Osint(Base):
    __tablename__ = 'OSINT'

    # Colunas da tabela
    # # id: chave primária da tabela
    id = Column(Integer, primary_key=True)

    # # twitter_id: id do tweet no twitter
    twitter_id = Column(String(32), index=True)

    # # text: texto do tweet
    text = Column(Text)

    # # created_at: data de criação do tweet
    created_at = Column(DateTime)

    # # Retorna uma representação da classe, para ser usada em print()
    def __repr__(self):
        return f'Osint {self.twitter_id}'

