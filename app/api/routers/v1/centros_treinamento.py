from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.models import CentroTreinamento
from app.schemas import CentroTreinamentoCreate, CentroTreinamentoResponse, CentroTreinamentoUpdate
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

router = APIRouter(prefix="/centros", tags=["Centros de Treinamento"])

@router.post("/", response_model=CentroTreinamentoResponse)
def create_centro(centro: CentroTreinamentoCreate, db: Session = Depends(get_db)):
    try:
        novo_centro = CentroTreinamento(**centro.dict())
        db.add(novo_centro)
        db.commit()
        db.refresh(novo_centro)
        return novo_centro
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail=f"Já existe um centro com o nome: {centro.nome}")

@router.get("/{centro_id}", response_model=CentroTreinamentoResponse)
def read_centro(centro_id: int, db: Session = Depends(get_db)):
    centro = db.query(CentroTreinamento).filter(CentroTreinamento.pk_id == centro_id).first()
    if not centro:
        raise HTTPException(status_code=404, detail="Centro de treinamento não encontrado")
    return centro

@router.get("/", response_model=Page[CentroTreinamentoResponse])
def read_centros(
    nome: str | None = None,
    proprietario: str | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(CentroTreinamento)
    
    if nome:
        query = query.filter(CentroTreinamento.nome.ilike(f"%{nome}%"))
    if proprietario:
        query = query.filter(CentroTreinamento.proprietario.ilike(f"%{proprietario}%"))
    
    return paginate(query)

@router.put("/{centro_id}", response_model=CentroTreinamentoResponse)
def update_centro(centro_id: int, centro_data: CentroTreinamentoUpdate, db: Session = Depends(get_db)):
    centro = db.query(CentroTreinamento).filter(CentroTreinamento.pk_id == centro_id).first()
    if not centro:
        raise HTTPException(status_code=404, detail="Centro de treinamento não encontrado")
    
    try:
        for field, value in centro_data.dict(exclude_unset=True).items():
            setattr(centro, field, value)
        
        db.commit()
        db.refresh(centro)
        return centro
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail="Erro de integridade dos dados")

@router.delete("/{centro_id}")
def delete_centro(centro_id: int, db: Session = Depends(get_db)):
    centro = db.query(CentroTreinamento).filter(CentroTreinamento.pk_id == centro_id).first()
    if not centro:
        raise HTTPException(status_code=404, detail="Centro de treinamento não encontrado")
    
    db.delete(centro)
    db.commit()
    return {"message": "Centro de treinamento deletado com sucesso"}