from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional

from ..glossary.tecnica import Tecnica


class Faixa(Enum):
    """Enumeração das faixas de Taekwondo."""

    BRANCA = "Branca"
    AMARELA = "Amarela"
    VERDE = "Verde"
    AZUL = "Azul"
    VERMELHA = "Vermelha"
    PRETA = "Preta"


@dataclass
class TecnicaFaixa:
    """Classe que representa uma técnica associada a uma faixa."""

    nome: str
    descricao: str = ""
    video_url: Optional[str] = None
    imagem_url: Optional[str] = None
    tecnica: Optional[Tecnica] = None

    def __post_init__(self):
        """Inicializa a técnica após a criação do objeto."""
        if self.tecnica is None:
            self.tecnica = Tecnica(self.nome)


@dataclass
class ConjuntoTecnicas:
    """Classe que representa um conjunto de técnicas (braços ou chutes) para uma faixa."""

    tecnicas_braco: List[TecnicaFaixa]
    tecnicas_chute: List[TecnicaFaixa]

    def get_todas_tecnicas(self) -> List[TecnicaFaixa]:
        """Retorna todas as técnicas do conjunto."""
        return self.tecnicas_braco + self.tecnicas_chute


class GerenciadorFaixas:
    """Classe para gerenciar as técnicas de cada faixa."""

    def __init__(self):
        """Inicializa o gerenciador de faixas."""
        self._faixas: Dict[Faixa, ConjuntoTecnicas] = {}
        self._carregar_tecnicas()

    def _carregar_tecnicas(self):
        """Carrega as técnicas para cada faixa."""
        # Este método será implementado nas classes filhas
        pass

    def get_tecnicas_faixa(self, faixa: Faixa) -> ConjuntoTecnicas:
        """Retorna as técnicas de uma faixa específica."""
        if faixa not in self._faixas:
            raise ValueError(f"Faixa {faixa.value} não encontrada")
        return self._faixas[faixa]

    def get_todas_faixas(self) -> List[Faixa]:
        """Retorna todas as faixas disponíveis."""
        return list(self._faixas.keys())

    def get_tecnicas_braco_faixa(self, faixa: Faixa) -> List[TecnicaFaixa]:
        """Retorna as técnicas de braço de uma faixa específica."""
        return self.get_tecnicas_faixa(faixa).tecnicas_braco

    def get_tecnicas_chute_faixa(self, faixa: Faixa) -> List[TecnicaFaixa]:
        """Retorna as técnicas de chute de uma faixa específica."""
        return self.get_tecnicas_faixa(faixa).tecnicas_chute
