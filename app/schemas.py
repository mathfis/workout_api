from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# --- Centro de Treinamento ---
class CentroTreinamentoBase(BaseModel):
    nome: str
    endereco: str
    proprietario: str

class CentroTreinamentoCreate(CentroTreinamentoBase):
    pass

class CentroTreinamentoResponse(CentroTreinamentoBase):
    pk_id: int
    valid: bool

    class Config:
        from_attributes = True

# --- Categoria ---
class CategoriaBase(BaseModel):
    nome: str
    cpf: str
    peso: float
    scenzo_: str
    centro_treinamento_id: int

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaResponse(CategoriaBase):
    pk_id: int
    valid: bool
    date: datetime
    centro_treinamento: Optional[CentroTreinamentoResponse] = None

    class Config:
        from_attributes = True

# --- Aluno ---
class AlunoBase(BaseModel):
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str
    centro_treinamento_id: int
    categoria_id: int

class AlunoCreate(AlunoBase):
    pass

class AlunoResponse(AlunoBase):
    pk_id: int
    valid: bool
    centro_treinamento: Optional[CentroTreinamentoResponse] = None
    categoria: Optional[CategoriaResponse] = None

    class Config:
        from_attributes = True

# Schemas para atualização
class AlunoUpdate(BaseModel):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    idade: Optional[int] = None
    peso: Optional[float] = None
    altura: Optional[float] = None
    sexo: Optional[str] = None
    centro_treinamento_id: Optional[int] = None
    categoria_id: Optional[int] = None

class CategoriaUpdate(BaseModel):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    peso: Optional[float] = None
    scenzo_: Optional[str] = None
    centro_treinamento_id: Optional[int] = None

class CentroTreinamentoUpdate(BaseModel):
    nome: Optional[str] = None
    endereco: Optional[str] = None
    proprietario: Optional[str] = None