from typing import Dict, List, Tuple

import Levenshtein

from taekwondo_glossario.glossary import TERMOS_ENUMS


class Tecnica:
    """Classe que representa uma técnica de Taekwondo e identifica os termos presentes nela."""

    def __init__(self, nome: str, max_distance: int = 2):
        """Inicializa uma técnica com o nome fornecido.

        Args:
            nome: Nome da técnica
            max_distance: Distância máxima de Levenshtein permitida (padrão: 2)
        """
        self.nome = nome
        self.max_distance = max_distance
        self.termos_encontrados = self._encontrar_termos()

    def _calcular_similaridade(self, termo: str, palavra: str) -> Tuple[bool, int]:
        """Calcula a similaridade entre um termo e uma palavra usando a distância de Levenshtein.

        Args:
            termo: Termo a ser comparado
            palavra: Palavra onde procurar o termo

        Returns:
            Tuple contendo (se encontrou, distância)
        """
        # Calcula a distância de Levenshtein
        distancia = Levenshtein.distance(palavra.lower(), termo.lower())

        # Se a distância for menor ou igual ao máximo permitido, encontrou
        if distancia <= self.max_distance:
            return True, distancia

        return False, 0

    def _encontrar_termos(self) -> Dict[str, List[Dict[str, str]]]:
        """Encontra todos os termos presentes no nome da técnica."""
        # Divide o nome da técnica em palavras e remove hífens
        palavras = [p.replace("-", " ") for p in self.nome.lower().split()]

        # Dicionário para armazenar os termos encontrados por categoria
        termos_por_categoria = {}
        # Lista para manter a ordem dos termos encontrados
        ordem_termos = []
        # Conjunto para rastrear palavras já processadas
        palavras_processadas = set()

        # Para cada palavra na técnica
        i = 0
        while i < len(palavras):
            palavra_atual = palavras[i]
            termo_encontrado = False

            # Tenta encontrar termos compostos (3 palavras)
            if i + 2 < len(palavras):
                termo_composto = " ".join(palavras[i : i + 3])
                for enum in TERMOS_ENUMS:
                    for termo in enum.listar_todos():
                        # Remove hífens do termo coreano antes de comparar
                        termo_coreano = termo["coreano"].lower().replace("-", "")
                        if termo_coreano == termo_composto:
                            categoria = enum.__name__
                            if categoria not in termos_por_categoria:
                                termos_por_categoria[categoria] = []
                            termo_copy = termo.copy()
                            termo_copy["distancia"] = 0
                            termos_por_categoria[categoria].append(termo_copy)
                            ordem_termos.append((categoria, termo_copy))
                            palavras_processadas.update(palavras[i : i + 3])
                            i += 3
                            termo_encontrado = True
                            break
                    if termo_encontrado:
                        break

            # Se não encontrou termo de 3 palavras, tenta de 2
            if not termo_encontrado and i + 1 < len(palavras):
                termo_composto = " ".join(palavras[i : i + 2])
                for enum in TERMOS_ENUMS:
                    for termo in enum.listar_todos():
                        # Remove hífens do termo coreano antes de comparar
                        termo_coreano = termo["coreano"].lower().replace("-", "")
                        if termo_coreano == termo_composto:
                            categoria = enum.__name__
                            if categoria not in termos_por_categoria:
                                termos_por_categoria[categoria] = []
                            termo_copy = termo.copy()
                            termo_copy["distancia"] = 0
                            termos_por_categoria[categoria].append(termo_copy)
                            ordem_termos.append((categoria, termo_copy))
                            palavras_processadas.update(palavras[i : i + 2])
                            i += 2
                            termo_encontrado = True
                            break
                    if termo_encontrado:
                        break

            # Se não encontrou termo composto, tenta termo simples
            if not termo_encontrado:
                # Inicializa a menor distância encontrada para esta palavra
                menor_distancia = float("inf")
                termo_mais_proximo = None
                categoria_termo = None

                # Para cada enumeração, verifica se algum termo está próximo da palavra
                for enum in TERMOS_ENUMS:
                    for termo in enum.listar_todos():
                        # Remove hífens do termo coreano antes de comparar
                        termo_coreano = termo["coreano"].lower().replace("-", " ")
                        # Verifica se o termo está próximo da palavra
                        encontrou, distancia = self._calcular_similaridade(termo_coreano, palavra_atual)

                        # Se encontrou e a distância é menor que a menor distância encontrada até agora
                        if encontrou and distancia < menor_distancia:
                            menor_distancia = distancia
                            termo_mais_proximo = termo.copy()
                            termo_mais_proximo["distancia"] = distancia
                            categoria_termo = enum.__name__

                # Se encontrou um termo para esta palavra, armazena
                if termo_mais_proximo:
                    if categoria_termo not in termos_por_categoria:
                        termos_por_categoria[categoria_termo] = []
                    termos_por_categoria[categoria_termo].append(termo_mais_proximo)
                    ordem_termos.append((categoria_termo, termo_mais_proximo))
                    palavras_processadas.add(palavra_atual)

                i += 1

        # Adiciona a ordem aos termos encontrados
        self.ordem_termos = ordem_termos
        return termos_por_categoria

    def get_termos_encontrados(self) -> Dict[str, List[Dict[str, str]]]:
        """Retorna os termos encontrados na técnica."""
        return self.termos_encontrados

    def get_categorias_encontradas(self) -> List[str]:
        """Retorna as categorias de termos encontradas na técnica."""
        return list(self.termos_encontrados.keys())

    def get_todos_termos(self) -> List[Dict[str, str]]:
        """Retorna todos os termos encontrados, independente da categoria."""
        todos_termos = []
        for termos in self.termos_encontrados.values():
            todos_termos.extend(termos)
        return todos_termos

    def get_termos_ordenados(self) -> List[Tuple[str, Dict[str, str]]]:
        """Retorna os termos na ordem em que aparecem na técnica."""
        return self.ordem_termos

    def __str__(self) -> str:
        """Retorna uma representação em string da técnica."""
        return f"Técnica: {self.nome}"


# Exemplo de uso
if __name__ == "__main__":
    # Exemplo de uma técnica com erro de digitação
    tecnica = Tecnica("Apkubi momtong jireugi")

    # Exibe os termos encontrados
    print(f"Técnica: {tecnica.nome}")
    print("\nTermos encontrados:")

    for categoria, termos in tecnica.get_termos_encontrados().items():
        print(f"\n{categoria}:")
        for termo in termos:
            distancia = termo.get("distancia", 0)
            print(f"  - {termo['coreano']} ({termo['portugues']}) - Distância: {distancia}")
