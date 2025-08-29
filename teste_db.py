# test_db.py
import sys
import os
from sqlalchemy import text  # ← IMPORTANTE: Adicionar esta importação

# Adicionar a pasta app ao path do Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal, engine
from app.models import Base

def test_database():
    print("🧪 Testando conexão com o banco de dados...")
    
    # Criar tabelas
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Tabelas criadas com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao criar tabelas: {e}")
        return False
    
    # Testar conexão - USAR text() para queries SQL
    db = SessionLocal()
    try:
        result = db.execute(text("SELECT 1"))  # ← Corrigido aqui
        print("✅ Conexão com SQLite bem-sucedida!")
        print(f"📊 Resultado do teste: {result.scalar()}")
        return True
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
        return False
    finally:
        db.close()

if __name__ == "__main__":
    success = test_database()
    if success:
        print("\n🎉 Tudo funcionando! Agora execute:")
        print("uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")
    else:
        print("\n💥 Houve problemas na configuração do banco.")