# Taekwondo Glossário

Aplicação web que ajuda a entender os termos em coreano usados no Taekwondo. O aplicativo permite:

- Buscar termos em coreano e ver suas traduções
- Entender o significado de técnicas através da análise de seus componentes
- Explorar termos por categorias (bases, ações, direções, etc.)
- Ver descrições detalhadas dos termos

## Como usar

1. Acesse a aplicação através do link do Streamlit Cloud
2. Use a barra lateral para navegar entre as diferentes seções:
   - Termos: Busca e visualização de termos individuais
   - Técnica: Análise de técnicas compostas
   - Faixas: Informações sobre graduações

## Tecnologias utilizadas

- Python
- Streamlit
- Levenshtein (para busca aproximada de termos)

## Instalação local

1. Clone o repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a aplicação:
   ```bash
   streamlit run taekwondo/glossary/app.py
   ```