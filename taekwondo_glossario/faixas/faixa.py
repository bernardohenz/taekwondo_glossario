import json
import os
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional

from ..glossary.tecnica import Tecnica


class FaixaEnum(Enum):
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
class Faixa:
    """Classe que representa uma faixa de Taekwondo com suas técnicas."""

    cor: str
    nome: str
    tecnicas_braco: List[str]
    tecnicas_chute: List[str]

    @classmethod
    def carregar_de_json(cls, caminho_arquivo: str) -> "Faixa":
        """Carrega os dados de uma faixa a partir de um arquivo JSON."""
        with open(caminho_arquivo, encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        return cls(
            cor=dados["cor"],
            nome=dados["nome"],
            tecnicas_braco=dados["tecnicas_braco"],
            tecnicas_chute=dados["tecnicas_chute"],
        )

    def get_tecnicas_braco_objetos(self) -> List[TecnicaFaixa]:
        """Retorna as técnicas de braço como objetos TecnicaFaixa."""
        return [TecnicaFaixa(nome=tecnica) for tecnica in self.tecnicas_braco]

    def get_tecnicas_chute_objetos(self) -> List[TecnicaFaixa]:
        """Retorna as técnicas de chute como objetos TecnicaFaixa."""
        return [TecnicaFaixa(nome=tecnica) for tecnica in self.tecnicas_chute]

    def get_todas_tecnicas(self) -> List[TecnicaFaixa]:
        """Retorna todas as técnicas da faixa como objetos TecnicaFaixa."""
        return self.get_tecnicas_braco_objetos() + self.get_tecnicas_chute_objetos()


class GerenciadorFaixas:
    """Classe para gerenciar as técnicas de cada faixa."""

    def __init__(self, diretorio_faixas: str = None):
        """Inicializa o gerenciador de faixas.

        Args:
            diretorio_faixas: Diretório onde estão os arquivos JSON das faixas.
                             Se None, usa o diretório padrão.
        """
        if diretorio_faixas is None:
            # Usa o diretório atual como padrão
            diretorio_faixas = os.path.dirname(os.path.abspath(__file__))

        self.diretorio_faixas = diretorio_faixas
        self._faixas: Dict[str, Faixa] = {}
        self._carregar_faixas()

    def _carregar_faixas(self):
        """Carrega todas as faixas dos arquivos JSON."""
        # Lista todos os arquivos JSON no diretório
        arquivos_json = [f for f in os.listdir(self.diretorio_faixas) if f.endswith(".json") and f.startswith("faixa_")]

        for arquivo in arquivos_json:
            caminho_arquivo = os.path.join(self.diretorio_faixas, arquivo)
            faixa = Faixa.carregar_de_json(caminho_arquivo)
            self._faixas[faixa.cor.lower()] = faixa

    def get_faixa(self, cor: str) -> Faixa:
        """Retorna uma faixa específica pelo nome da cor.

        Args:
            cor: Nome da cor da faixa (ex: "branca", "amarela", etc.)

        Returns:
            Objeto Faixa correspondente à cor especificada.

        Raises:
            ValueError: Se a faixa não for encontrada.
        """
        cor = cor.lower()
        if cor not in self._faixas:
            raise ValueError(f"Faixa {cor} não encontrada")
        return self._faixas[cor]

    def get_todas_faixas(self) -> List[Faixa]:
        """Retorna todas as faixas disponíveis."""
        return list(self._faixas.values())

    def get_tecnicas_braco_faixa(self, cor: str) -> List[TecnicaFaixa]:
        """Retorna as técnicas de braço de uma faixa específica."""
        return self.get_faixa(cor).get_tecnicas_braco_objetos()

    def get_tecnicas_chute_faixa(self, cor: str) -> List[TecnicaFaixa]:
        """Retorna as técnicas de chute de uma faixa específica."""
        return self.get_faixa(cor).get_tecnicas_chute_objetos()
