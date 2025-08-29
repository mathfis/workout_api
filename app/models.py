from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class CentroTreinamento(Base):
    __tablename__ = "centro_treinamento"
    
    pk_id = Column(Integer, primary_key=True, index=True)
    id = Column(String, unique=True, index=True)  # uuid
    nome = Column(String(20), unique=True, index=True)
    endereco = Column(String(60))
    proprietario = Column(String(30))

    alunos = relationship("Aluno", back_populates="centro_treinamento")


class Categoria(Base):
    __tablename__ = "categoria"
    
    pk_id = Column(Integer, primary_key=True, index=True)
    id = Column(String, unique=True, index=True)  # uuid
    nome = Column(String(10), unique=True)

    alunos = relationship("Aluno", back_populates="categoria")


class Aluno(Base):
    __tablename__ = "aluno"
    
    pk_id = Column(Integer, primary_key=True, index=True)
    id = Column(String, unique=True, index=True)  # uuid
    nome = Column(String(50))
    cpf = Column(String(11), unique=True, index=True)
    idade = Column(Integer)
    peso = Column(Float)
    altura = Column(Float)
    sexo = Column(String(1))

    centro_treinamento_id = Column(Integer, ForeignKey("centro_treinamento.pk_id"))
    categoria_id = Column(Integer, ForeignKey("categoria.pk_id"))

    centro_treinamento = relationship("CentroTreinamento", back_populates="alunos")
    categoria = relationship("Categoria", back_populates="alunos")
