from fastapi import FastAPI
from app.database import engine, Base
from app.routes import alunos, categorias, centros_treinamento
from fastapi_pagination import add_pagination
import uvicorn
import os

# Criar tabelas automaticamente (para dev; em prod use alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Workout API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "API Workout funcionando com SQLite!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "SQLite"}

# Rotas
app.include_router(alunos.router, prefix="/alunos", tags=["Alunos"])
app.include_router(categorias.router, prefix="/categorias", tags=["Categorias"])
app.include_router(centros_treinamento.router, prefix="/centros", tags=["Centros de Treinamento"])

add_pagination(app)

# Custom startup message
def custom_startup_message():
    print("\n" + "="*60)
    print("🚀 WORKOUT API INICIADA COM SUCESSO!")
    print("="*60)
    print(f"📊 Local: http://localhost:8000")
    print(f"📚 Docs: http://localhost:8000/docs")
    print(f"🔍 Redoc: http://localhost:8000/redoc")
    print("="*60)
    print("📋 Endpoints disponíveis:")
    print(f"   • Alunos: http://localhost:8000/alunos")
    print(f"   • Categorias: http://localhost:8000/categorias")
    print(f"   • Centros: http://localhost:8000/centros")
    print("="*60)
    print("⏹️  Pressione CTRL+C para parar o servidor")
    print("="*60 + "\n")

# Adicionar evento de startup
@app.on_event("startup")
async def startup_event():
    custom_startup_message()

# Para executar diretamente: python app/main.py
if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )