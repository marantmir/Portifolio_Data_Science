import streamlit as st
import pandas as pd

# Carregando o "cache" da página Inínio
df_dados = st.session_state["dados"]

# Cria o filtro de Regiões
regioes = df_dados['regiao'].value_counts().index
regiao = st.sidebar.selectbox("Região", regioes)

# Organiza em um dataframe os bairros a partir da região selecionada acima
df_bairros = df_dados[df_dados['regiao'] == regiao]

# Cria o filtro de Bairros
bairros = df_bairros['bairro'].value_counts().index
bairro = st.sidebar.selectbox("Bairro", bairros)

# Cria uma base de dados para visualizar apenas os pontos de coleta de acordo com o bairro
mostra_bairro = df_dados[df_dados["bairro"] == bairro]

# Seleciona apenas as colunas que deseja mostrar na tabela dos pontos de coletas
colunas = ['tiporesiduo', "endereco", "complemento", "observacao"]

# Cria uma base de dados para visualizar apenas os pontos de coleta de acordo com o bairro
mostra_bairro = df_dados[df_dados["bairro"] == bairro]

# Exibe as colunas na tela
st.dataframe(mostra_bairro[colunas], hide_index=True)