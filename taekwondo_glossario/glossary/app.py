from typing import Dict, List

import Levenshtein
import streamlit as st

from taekwondo_glossario.faixas.faixa import GerenciadorFaixas
from taekwondo_glossario.glossary import TERMOS_ENUMS, get_all_terms
from taekwondo_glossario.glossary.tecnica import Tecnica

# Configurações de estilo da página
st.set_page_config(
    page_title="Glossário de Taekwondo",
    page_icon="🥋",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "About": "# Este é um glossário de termos do Taekwondo desenvolvido por @bernardohenz",
        "Report a bug": "https://github.com/bernardohenz/taekwondo/issues",
        "Get help": "https://github.com/bernardohenz/taekwondo",
    },
)

# Estilo CSS global
st.markdown(
    """
    <style>
    /* Estilo global para toda a página */
    html, body, .stApp {
        font-size: 1.3rem;
    }
    /* Ajuste para telas menores */
    @media (max-width: 768px) {
        html, body, .stApp {
            font-size: 1rem;
        }
    }
    /* Centraliza o conteúdo */
    .main .block-container {
        max-width: 1200px;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def calculate_levenshtein_distance(a: str, b: str) -> int:
    """Calcula a distância de Levenshtein entre duas strings."""
    return Levenshtein.distance(a.lower(), b.lower())


def search_terms(terms: List[Dict[str, str]], query: str, max_distance: int = 2) -> List[Dict[str, str]]:
    """Pesquisa termos que correspondam à query usando a distância de Levenshtein."""
    if not query:
        return terms

    query = query.lower()
    results = []

    for term in terms:
        # Calcula a distância de Levenshtein para cada campo
        coreano_distance = calculate_levenshtein_distance(query, term["coreano"])
        portugues_distance = calculate_levenshtein_distance(query, term["portugues"])

        # Verifica se algum campo está dentro da distância máxima permitida
        if coreano_distance <= max_distance or portugues_distance <= max_distance:
            # Usa a menor distância encontrada
            min_distance = min(coreano_distance, portugues_distance)
            term["distance"] = min_distance
            results.append(term)

    # Ordena os resultados por distância (menor distância primeiro)
    return sorted(results, key=lambda x: x["distance"])


def main():
    # Inicializa o estado da sessão se necessário
    if "search_query" not in st.session_state:
        st.session_state.search_query = ""
    if "tecnica_nome" not in st.session_state:
        st.session_state.tecnica_nome = ""
    if "mostrar_descricao" not in st.session_state:
        st.session_state.mostrar_descricao = True

    st.title("Glossário de Taekwondo")
    st.write("Consulte e pesquise termos do Taekwondo")

    # Sidebar para seleção de categoria e configurações
    st.sidebar.title("Configurações")

    # Checkbox para mostrar/ocultar descrições
    st.session_state.mostrar_descricao = st.sidebar.checkbox(
        "Mostrar descrições dos termos",
        value=st.session_state.mostrar_descricao,
        help="Quando desabilitado, mostra apenas a tradução dos termos",
    )

    # Criação de abas
    tab1, tab2, tab3 = st.tabs(["Termos", "Técnica", "Faixas"])

    # Aba de Termos
    with tab1:
        # Seleção de categoria
        categoria = st.sidebar.selectbox(
            "Selecione uma categoria:",
            ["Todos os Termos"] + [enum.__name__ for enum in TERMOS_ENUMS],
        )

        # Configuração da distância máxima de Levenshtein
        max_distance = st.sidebar.slider(
            "Distância máxima permitida:",
            min_value=0,
            max_value=5,
            value=2,
            step=1,
            help="Quanto maior o valor, mais tolerante será a busca a erros",
        )

        # Barra de pesquisa com atualização em tempo real
        search_query = st.text_input(
            "Pesquisar termo:",
            value=st.session_state.search_query,
            key="search_input",
            label_visibility="collapsed",
        )

        # Atualiza o estado da sessão com o novo valor da busca
        st.session_state.search_query = search_query

        # Obtém os termos baseado na categoria selecionada
        if categoria == "Todos os Termos":
            # Obtém todos os termos de todas as categorias
            all_terms = get_all_terms()
            # Combina todos os termos em uma única lista
            terms = []
            for categoria_termos in all_terms.values():
                terms.extend(categoria_termos)
        else:
            # Encontra a enumeração correspondente à categoria selecionada
            enum = next((e for e in TERMOS_ENUMS if e.__name__ == categoria), None)
            if enum:
                terms = enum.listar_todos()
            else:
                terms = []

        # Aplica a pesquisa se houver uma query
        if search_query:
            terms = search_terms(terms, search_query, max_distance)

        # Exibe os termos
        for term in terms:
            # Adiciona a distância ao título se estiver pesquisando
            title = f"{term['coreano']} ({term['portugues']})"
            if search_query and "distance" in term:
                # Não exibe a distância para o usuário
                pass

            with st.expander(title):
                if st.session_state.mostrar_descricao:
                    st.write("**Descrição:**")
                    st.write(term["descricao"])

    # Aba de Técnica
    with tab2:
        st.header("Análise de Técnica")
        st.write("Digite o nome completo da técnica para identificar os termos presentes nela.")

        # Campo para digitar o nome da técnica
        tecnica_nome = st.text_input(
            "Nome da técnica:",
            value=st.session_state.tecnica_nome,
            key="tecnica_input",
            placeholder="Ex: Apkubi momtong jireugi",
        )

        # Atualiza o estado da sessão com o novo valor
        st.session_state.tecnica_nome = tecnica_nome

        # Configuração da distância máxima de Levenshtein para a técnica
        tecnica_max_distance = st.slider(
            "Distância máxima permitida:",
            min_value=0,
            max_value=5,
            value=2,
            step=1,
            help="Quanto maior o valor, mais tolerante será a busca a erros de digitação",
        )

        # Botão para analisar a técnica
        if st.button("Analisar Técnica"):
            if tecnica_nome:
                # Cria uma instância da classe Tecnica
                tecnica = Tecnica(tecnica_nome, tecnica_max_distance)

                # Exibe o nome da técnica
                st.subheader(f"Técnica: {tecnica.nome}")

                # Obtém os termos encontrados
                termos_encontrados = tecnica.get_termos_encontrados()

                if termos_encontrados:
                    # Exibe os termos encontrados por categoria
                    for categoria, termos in termos_encontrados.items():
                        st.write(f"**{categoria}:**")
                        for termo in termos:
                            if st.session_state.mostrar_descricao:
                                st.write(f"- {termo['coreano']} - {termo['portugues']}")
                                st.write(f"  {termo['descricao']}")
                            else:
                                st.write(f"- {termo['coreano']} - {termo['portugues']}")
                else:
                    st.warning("Nenhum termo encontrado na técnica. Tente aumentar a distância máxima permitida.")
            else:
                st.warning("Por favor, digite o nome da técnica.")

    # Aba de Faixas
    with tab3:
        st.header("Técnicas por Faixa")
        st.write("Selecione uma faixa para visualizar suas técnicas.")

        # Inicializa o gerenciador de faixas
        gerenciador = GerenciadorFaixas()

        # Obtém todas as faixas disponíveis
        faixas = gerenciador.get_todas_faixas()

        # Função para extrair o número do GUB/DAN
        def extrair_grau(faixa):
            nome = faixa.nome
            if "GUB" in nome:
                return int(nome.split()[0])
            elif "DAN" in nome:
                return -int(nome.split()[0])  # DANs vêm depois dos GUBs
            return 0

        # Ordena as faixas por GUB/DAN de forma decrescente
        faixas_ordenadas = sorted(faixas, key=extrair_grau, reverse=True)

        # Cria uma lista de opções para o selectbox
        opcoes_faixas = [f"{faixa.cor} ({faixa.nome})" for faixa in faixas_ordenadas]

        # Seleção da faixa
        faixa_selecionada = st.selectbox(
            "Selecione uma faixa:",
            opcoes_faixas,
            index=0,
        )

        # Extrai a cor da faixa selecionada
        cor_faixa = faixa_selecionada.split(" (")[0].lower()

        # Obtém a faixa selecionada
        faixa = gerenciador.get_faixa(cor_faixa)

        # Exibe informações da faixa
        st.subheader(f"Faixa {faixa.cor} ({faixa.nome})")

        # Cria duas colunas para técnicas de braço e chute
        col1, col2 = st.columns(2)

        # Técnicas de braço
        with col1:
            st.write("**Técnicas de Braço:**")
            for tecnica in faixa.get_tecnicas_braco_objetos():
                with st.expander(tecnica.nome):
                    # Analisa a técnica para encontrar os termos
                    tecnica_analisada = tecnica.tecnica
                    termos_ordenados = tecnica_analisada.get_termos_ordenados()

                    if termos_ordenados:
                        # Exibe os termos na ordem em que aparecem
                        st.write("**Termos encontrados:**")
                        for categoria, termo in termos_ordenados:
                            if st.session_state.mostrar_descricao:
                                st.write(f"- {termo['coreano']} - {termo['portugues']}")
                                st.write(f"  {termo['descricao']}")
                            else:
                                st.write(f"- {termo['coreano']} - {termo['portugues']}")
                    else:
                        st.write("Nenhum termo encontrado nesta técnica.")

        # Técnicas de chute
        with col2:
            st.write("**Técnicas de Chute:**")
            for tecnica in faixa.get_tecnicas_chute_objetos():
                with st.expander(tecnica.nome):
                    # Analisa a técnica para encontrar os termos
                    tecnica_analisada = tecnica.tecnica
                    termos_ordenados = tecnica_analisada.get_termos_ordenados()

                    if termos_ordenados:
                        # Exibe os termos na ordem em que aparecem
                        st.write("**Termos encontrados:**")
                        for _, termo in termos_ordenados:
                            if st.session_state.mostrar_descricao:
                                st.write(f"- {termo['coreano']} - {termo['portugues']}")
                                st.write(f"  {termo['descricao']}")
                            else:
                                st.write(f"- {termo['coreano']} - {termo['portugues']}")
                    else:
                        st.write("Nenhum termo encontrado nesta técnica.")


if __name__ == "__main__":
    main()
