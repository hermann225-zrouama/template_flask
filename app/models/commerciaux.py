from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import os
Base = declarative_base()

class Commerciaux(Base):
    __tablename__ = 'commerciaux'

    __table_args__ = ({'schema': os.environ.get('SCHEMAS')})

    id = Column(Integer, primary_key=True, autoincrement=True)
    NUMERO_CC = Column(String, nullable=True)
    SEGMENT_MARCHE = Column(String, nullable=True)
    GESTIONNAIRE = Column(String, nullable=True)
    Login = Column(String, nullable=True)
    Mot_de_passe = Column(String, nullable=True)
