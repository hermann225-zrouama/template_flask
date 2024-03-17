from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.config.db import get_db
from app.schemas.sales_admin import Sales_admins
from app.models.commerciaux import Commerciaux
from app.models.entreprises import Entreprise


def get_commercial_data(db: Session, commercial_id: int):
    try:
        commercial = db.query(Commerciaux).filter(Commerciaux.id == commercial_id).first()
        if commercial:
            return db.query(Entreprise).filter(Entreprise.GESTIONNAIRE == commercial.GESTIONNAIRE).join(Commerciaux, Entreprise.GESTIONNAIRE == Commerciaux.GESTIONNAIRE).all()
        return []
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_commercial_data(commercial_id: int, new_data: dict, db: Session=Depends(get_db)):
    try:
        commercial = db.query(Commerciaux).filter(Commerciaux.id == commercial_id).first()
        if commercial:
            entreprise_id = new_data.get('id')  # Récupérer l'ID de l'entreprise à mettre à jour
            entreprise = db.query(Entreprise).filter(Entreprise.id == entreprise_id).first()  # Récupérer l'entreprise correspondante
            if entreprise:
                for key, value in new_data.items():
                    setattr(entreprise, key, value)  # Mettre à jour les champs de l'entreprise avec les nouvelles données
                db.commit()
                return [entreprise]  # Retourner l'entreprise mise à jour dans une liste
        return []  # Si aucune entreprise n'est trouvée ou si le commercial n'existe pas, retourner une liste vide
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
