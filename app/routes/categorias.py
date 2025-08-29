from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.models import Categoria, CentroTreinamento
from app.schemas import CategoriaCreate, CategoriaResponse, CategoriaUpdate
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.post("/", response_model=CategoriaResponse)
def create_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    try:
        nova_categoria = Categoria(**categoria.dict())
        db.add(nova_categoria)
        db.commit()
        db.refresh(nova_categoria)
        return nova_categoria
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail=f"Já existe uma categoria com o CPF: {categoria.cpf}")

@router.get("/{categoria_id}", response_model=CategoriaResponse)
def read_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).options(
        joinedload(Categoria.centro_treinamento)
    ).filter(Categoria.pk_id == categoria_id).first()
    
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

@router.get("/", response_model=Page[CategoriaResponse])
def read_categorias(
    nome: str | None = None,
    cpf: str | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Categoria).options(
        joinedload(Categoria.centro_treinamento)
    )
    
    if nome:
        query = query.filter(Categoria.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(Categoria.cpf == cpf)
    
    return paginate(query)

@router.put("/{categoria_id}", response_model=CategoriaResponse)
def update_categoria(categoria_id: int, categoria_data: CategoriaUpdate, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter(Categoria.pk_id == categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    
    try:
        for field, value in categoria_data.dict(exclude_unset=True).items():
            setattr(categoria, field, value)
        
        db.commit()
        db.refresh(categoria)
        return categoria
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail="Erro de integridade dos dados")

@router.delete("/{categoria_id}")
def delete_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter(Categoria.pk_id == categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    
    db.delete(categoria)
    db.commit()
    return {"message": "Categoria deletada com sucesso"}