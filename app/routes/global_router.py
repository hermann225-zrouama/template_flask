from fastapi import APIRouter, Depends, UploadFile, HTTPException
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.models.entreprises import Entreprise
from app.models.commerciaux import Commerciaux
from app.controller import crud
import pandas as pd


router = APIRouter()


@router.get("/")
def root():
    return {'Welcome to OCI'}


@router.post("/upload/b2b_data") 
def load_b2b_data(file: UploadFile = UploadFile(...), db: Session = Depends(get_db)):
    try:
        # Charger le fichier Excel dans un DataFrame 
        df = pd.read_excel(file.file, sheet_name="Base_vue_clients_unique_B2B")

        # Vérifier si les colonnes du DataFrame correspondent au modèle SQLAlchemy 
        model_columns = Entreprise.__table__.columns.keys()
        column_mapping = {col: col for col in model_columns}
        df = df.rename(columns=column_mapping)

        # Convertir le DataFrame en une liste de dictionnaires
        data = df.to_dict(orient='records')

        # Insérer les données dans la base de données en utilisant bulk_insert_mappings
        db.bulk_insert_mappings(Entreprise, data)

        db.commit() 
        return {"message": "Données chargées avec succès"} 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/upload/commerciaux_mapping") 
def load_commerciaux_mapping(file: UploadFile = UploadFile(...), db: Session = Depends(get_db)):
    try:
        # Charger le fichier Excel dans un DataFrame 
        df = pd.read_excel(file.file, sheet_name="Liste_clients_commerciaux")

        # Vérifier si les colonnes du DataFrame correspondent au modèle SQLAlchemy 
        model_columns = Commerciaux.__table__.columns.keys()
        column_mapping = {col: col for col in model_columns}
        df = df.rename(columns=column_mapping)

        # Convertir le DataFrame en une liste de dictionnaires
        data = df.to_dict(orient='records')

        # Insérer les données dans la base de données en utilisant bulk_insert_mappings
        db.bulk_insert_mappings(Commerciaux, data)

        db.commit() 
        return {"message": "Données chargées avec succès"} 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/get_data_for_commercial")
def fetch_b2b_data_for_one_commercial(commercial_id:int, db: Session=Depends(get_db)):
    commercial_data = crud.get_commercial_data(db, commercial_id)
    if commercial_data is None:
        raise HTTPException(status_code=404, detail="Commercial not found")
    return commercial_data

@router.post("/update_b2b")
def fetch_b2b_data_for_one_commercial(commercial_id: int, new_data: dict, db: Session=Depends(get_db)):
    commercial_data = crud.update_commercial_data(commercial_id, new_data, db)
    if commercial_data is None:
        raise HTTPException(status_code=404, detail="Commercial not found")
    return commercial_data
