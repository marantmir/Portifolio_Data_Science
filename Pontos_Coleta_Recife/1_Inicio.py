
# Importa bibliotecas
import streamlit as st
import pandas as pd
import webbrowser as wb

# Configura detalhes da página
st.set_page_config(
    page_title="Início",
    page_icon="♻️"
)

# URL correta para acessar o arquivo CSV
DATA_URL = ("https://raw.githubusercontent.com/marantmir/tutorial-streamlit-pdcoletas/main/pontos-coleta-recife.csv")

# Lê o arquivo CSV
dados = pd.read_csv(DATA_URL)

# Constroi um "cache" dos dados
st.session_state["dados"] = dados

# Exibe o título
st.title("Pontos de coleta em Recife")

# Exibe o subtítulo
st.markdown(''' ### O Lixo é responsabilidade de todos''')

# Exibe texto explicativo longo
st.markdown('''Você já parou para pensar o que acontece com o lixo que sai da sua casa? E que o futuro desse material 
            depende muito da sua atitude? Quando o cidadão encaminha o lixo para a reciclagem, além de evitar mais acúmulo 
            de material nos aterros, garante que menos recursos naturais sejam extraídos para a fabricação de outros produtos e 
            contribui para a geração de emprego e renda de muitos trabalhadores¹.''')

# Exibe o texto falando sobre o gráfico abaixo
st.markdown('O gráfico abaixo mostra a quantidade de pontos de coleta por região.')

# Contando os pontos de coleta por região
qt_regiao = dados['regiao'].value_counts()

# Plotando um gráfico de barras com os dados
st.bar_chart(qt_regiao, color= '#006400')

# Transforma os dados de localização em float
dados['lat'] = dados['lat'].astype(float)
dados['lon'] = dados['lon'].astype(float)

#Plotando um mapa com os dados
st.map(dados)

# Organizando os botões na tela
col1, col2 = st.columns(2)

# Criando variáveis para os botões
btn1 = col1.button('Dados da prefeitura do Recife', use_container_width=True)
if btn1:
    wb.open_new_tab("http://dados.recife.pe.gov.br/dataset/destinacao-de-residuos-solidos")

btn2 = col2.button('Dados limpos', use_container_width=True)
if btn2:
    wb.open_new_tab("https://github.com/escola-de-dados/tutorial-streamlit-pdcoletas/blob/main/pontos-coleta-recife.csv")
