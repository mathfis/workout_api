from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.models import Aluno, CentroTreinamento, Categoria
from app.schemas import AlunoCreate, AlunoResponse, AlunoUpdate
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

router = APIRouter(prefix="/alunos", tags=["Alunos"])

@router.post("/", response_model=AlunoResponse)
def create_aluno(aluno: AlunoCreate, db: Session = Depends(get_db)):
    try:
        novo_aluno = Aluno(**aluno.dict())
        db.add(novo_aluno)
        db.commit()
        db.refresh(novo_aluno)
        return novo_aluno
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail=f"Já existe um aluno cadastrado com o cpf: {aluno.cpf}")

@router.get("/{aluno_id}", response_model=AlunoResponse)
def read_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).options(
        joinedload(Aluno.centro_treinamento),
        joinedload(Aluno.categoria)
    ).filter(Aluno.pk_id == aluno_id).first()
    
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@router.get("/", response_model=Page[AlunoResponse])
def read_alunos(
    nome: str | None = None, 
    cpf: str | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Aluno).options(
        joinedload(Aluno.centro_treinamento),
        joinedload(Aluno.categoria)
    )
    
    if nome:
        query = query.filter(Aluno.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(Aluno.cpf == cpf)
    
    return paginate(query)

@router.put("/{aluno_id}", response_model=AlunoResponse)
def update_aluno(aluno_id: int, aluno_data: AlunoUpdate, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).filter(Aluno.pk_id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    try:
        for field, value in aluno_data.dict(exclude_unset=True).items():
            setattr(aluno, field, value)
        
        db.commit()
        db.refresh(aluno)
        return aluno
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=303, detail="Erro de integridade dos dados")

@router.delete("/{aluno_id}")
def delete_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = db.query(Aluno).filter(Aluno.pk_id == aluno_id).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    db.delete(aluno)
    db.commit()
    return {"message": "Aluno deletado com sucesso"}