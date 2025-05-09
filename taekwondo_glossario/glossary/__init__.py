"""Módulo de glossário de termos do Taekwondo."""

from .termos import (
    Acoes,
    Bases,
    Direcoes,
    ModificadoresDirecao,
    PartesCorpo,
    PartesMao,
    PartesPe,
    TecnicasDeBloqueio,
    TermoBase,
    TermoEnumMixin,
    TiposChute,
    TiposMovimento,
)

# Lista de todas as enumerações de termos disponíveis
TERMOS_ENUMS = [
    Bases,
    Acoes,
    Direcoes,
    PartesCorpo,
    PartesMao,
    PartesPe,
    TecnicasDeBloqueio,
    TiposChute,
    TiposMovimento,
    ModificadoresDirecao,
]


# Função para obter todos os termos de todas as enumerações
def get_all_terms():
    """Retorna todos os termos disponíveis no sistema."""
    termos = {}
    for enum in TERMOS_ENUMS:
        termos[enum.__name__] = enum.listar_todos()
    return termos


__all__ = [
    "TERMOS_ENUMS",
    "Acoes",
    "Bases",
    "Direcoes",
    "ModificadoresDirecao",
    "PartesCorpo",
    "PartesMao",
    "PartesPe",
    "TecnicasDeBloqueio",
    "TermoBase",
    "TermoEnumMixin",
    "TiposChute",
    "TiposMovimento",
    "get_all_terms",
]
