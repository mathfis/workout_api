# /app/core/config.py 
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    # 2.1. Configuração de como o Pydantic deve carregar as variáveis
    model_config = SettingsConfigDict(
        env_file='.env', 
        env_file_encoding='utf-8',
        extra='ignore' 
    )
    
    # --- Configurações da Aplicação (Tipadas) ---
    PROJECT_NAME: str = "WorkoutAPI"
    ROOT_PATH: str = "/"

    # --- Configurações de Banco de Dados e Segurança ---
    
    DATABASE_URL: str = Field(
        default='sqlite+aiosqlite:///./workout.db',
        description="URL de conexão com o banco de dados. Prioriza a variável de ambiente."
    )

    SECRET_KEY: str = Field(
        default='AS09dflasdk90ASDfl2389dflkasd',
        description="Chave secreta para autenticação."
    )

# Instância única das configurações
settings = Settings()