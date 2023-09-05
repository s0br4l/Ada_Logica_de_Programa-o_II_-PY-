import streamlit as st

from functions.vendas import Venda

st.set_page_config(page_title="Vendas - Farmacia")

cont1 = st.container()

titulo_inicial = cont1.title('Historico de vendas')

cont2 = st.container()
if Venda.lista_vendas:
    exibe1 = cont2.text_area('tx', label_visibility="hidden", value=f'{Venda.listar()}', height=550)

