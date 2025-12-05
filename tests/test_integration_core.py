# tests/test_integration_core.py

import pytest
from app.core.config import settings
from typing import get_type_hints

## ----------------------------------------------------
## TESTES CORE (CONFIGURAÇÃO)
## ----------------------------------------------------

def test_settings_load_successfully():
    """
    Verifica se a instância de configurações (settings) é carregada.
    """
    # A simples importação sem erro já indica sucesso, mas verificamos o tipo.
    assert isinstance(settings.PROJECT_NAME, str)
    assert settings.PROJECT_NAME == "WorkoutAPI"

def test_database_url_is_correctly_typed_and_defaulted():
    """
    Verifica se a DATABASE_URL está tipada corretamente (str) e 
    se o valor padrão assíncrono do SQLite foi carregado.
    """
    # 1. Verifica se o campo DATABASE_URL tem o tipo correto (string)
    type_hints = get_type_hints(settings.__class__)
    assert type_hints['DATABASE_URL'] == str
    
    # 2. Verifica se o valor padrão assíncrono foi carregado
    expected_default = 'sqlite+aiosqlite:///./workout.db'
    assert settings.DATABASE_URL == expected_default
    
    # 3. Verifica se o SECRET_KEY foi carregado
    assert len(settings.SECRET_KEY) > 10