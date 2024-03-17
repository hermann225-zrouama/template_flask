# models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()

class Entreprise(Base):
    __tablename__ = 'entreprises'

    __table_args__ = ({'schema': os.environ.get('SCHEMAS')})
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    Identifiant_unique = Column(String, nullable=True)
    NUMERO_CC = Column(String, nullable=True)
    REGISTRE_COMMERCE = Column(String, nullable=True)
    SEGMENT_MARCHE = Column(String, nullable=True)
    GESTIONNAIRE = Column(String, nullable=True)
    CATEGORIE_NEW = Column(String, nullable=True)
    CATEGORIE = Column(String, nullable=True)
    CONTACT_MOBILE = Column(String, nullable=True)
    SECOND_MOBILE = Column(String, nullable=True)
    E_MAIL = Column(String, nullable=True)
    RAISON_SOCIALE_FIABILISE = Column(String, nullable=True)
    RAISON_SOCIALE_OCI = Column(String, nullable=True)
    RAISON_SOCIALE_IMPOT = Column(String, nullable=True)
    SIGLE = Column(String, nullable=True)
    NOM_PRENOMS_REPRESENTANT_LEGAL = Column(String, nullable=True)
    QUALITE_REPRESENTANT_LEGAL = Column(String, nullable=True)
    TEL_REPRESENTANT_LEGAL = Column(String, nullable=True)
    ADRESSE_POSTALE_REPRESENTANT_LEGAL = Column(String, nullable=True)
    ADRESSE_EMAIL_REPRESENTANT_LEGAL = Column(String, nullable=True)
    LOCALISATION = Column(String, nullable=True)
    ADRESSE_POSTALE_ENTREPRISE = Column(String, nullable=True)
    VILLE = Column(String, nullable=True)
    VILLE_COMMUNE = Column(String, nullable=True)
    ADRESSE_GEOGRAPHIQUE_COMPLETE = Column(String, nullable=True)
    DISTRICT = Column(String, nullable=True)
    REGION = Column(String, nullable=True)
    DEPARTEMENT = Column(String, nullable=True)
    FORME_JURIDIQUE = Column(String, nullable=True)
    SECTEUR_ACTIVITE = Column(String, nullable=True)
    LIBELLE_ACTIVITE = Column(String, nullable=True)
    DATE_DE_CREATION = Column(String, nullable=True)
    TYPE_SCENARIO = Column(String, nullable=True)
    CAPITAL = Column(String, nullable=True)
    NUMERO_DE_PIECE_IDENTITE_DU_REPRESENTANT_LEGAL = Column(String, nullable=True)
    NATIONALITE_DU_REPRESENTANT_LEGAL = Column(String, nullable=True)
    SITE_WEB_ENTREPRISE = Column(String, nullable=True)
    Type_client = Column(String, nullable=True)