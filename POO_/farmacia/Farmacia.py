import streamlit as st
from datetime import date
from functions.clientes import Cliente
from functions.laboratorios import Laboratorio
from functions.medicamentos import Medicamentos, Fitoterapicos, Quimioterapicos
from functions.vendas import Venda, VendaTemp

st.set_page_config(page_title="Farmacia E-commerce")

cont1 = st.container()

titulo_inicial = cont1.title('Olá! Bem vindo(a) a Farmacia')
subtitulo_inicial = cont1.subheader('selecione abaixo o que deseja fazer')

tab4, tab1, tab2, tab3 = st.tabs(["Registrar venda", "Cadastrar cliente", "Cadastrar laboratorio",
                                  "Cadastrar medicamento"])

cad_cliente_wind = tab1.container()

with cad_cliente_wind.form("cadastrar_cliente", clear_on_submit=True):
    nome_client_cad = st.text_input('Nome: ')
    data_nasc_client_cad = st.date_input('Data de nascimento: ', format="DD/MM/YYYY")
    data_nasc_client_cad = data_nasc_client_cad.strftime("%d/%m/%y")
    cpf_client_cad = st.text_input('CPF: ', max_chars=11)
    email_client_cad = st.text_input('E-mail: ')

    submitted = st.form_submit_button("CADASTRAR")
    if nome_client_cad and data_nasc_client_cad and cpf_client_cad and email_client_cad:
        if submitted:
            try:
                Cliente.cadastrar(nome_client_cad.title(), data_nasc_client_cad, cpf_client_cad, email_client_cad)
                st.success('Cadastro realizado')
            except:
                e = ValueError('CPF já cadastrado')
                st.exception(e)

    else:
        st.info('Preencha com todos os dados')

cad_lab_wind = tab2.container()

with cad_lab_wind.form("cadastrar_laboratorio", clear_on_submit=True):
    nome_lab_cad = st.text_input('Nome: ')
    endereco_lab_cad = st.text_input('Endereco: ')
    telefone_lab_cad = st.text_input('Telefone: ')
    cidade_lab_cad = st.text_input('Cidade: ')
    estado_lab_cad = st.text_input('Estado: ')

    submitted = st.form_submit_button("CADASTRAR")
    if nome_lab_cad and endereco_lab_cad and telefone_lab_cad and cidade_lab_cad and estado_lab_cad:
        if submitted:
            try:
                Laboratorio.cadastrar(nome_lab_cad.title(), endereco_lab_cad, telefone_lab_cad,
                                      cidade_lab_cad, estado_lab_cad)
                st.success('Cadastro realizado')
            except:
                e = ValueError('Laboratorio já cadastrado')
                st.exception(e)

    else:
        st.info('Preencha com todos os dados')

cad_medicamento_wind = tab3.container()
tipo_medicamento_cad = cad_medicamento_wind.radio('Tipo do medicamento: ', options=['Fitoterapico', 'Quimioterapico'],
                                                  horizontal=True)
if tipo_medicamento_cad == 'Quimioterapico':
    receita_medicamento_cad = cad_medicamento_wind.selectbox('precisa de receita: ', options=['Não', 'Sim'])

with (cad_medicamento_wind.form("cadastrar_medicamento", clear_on_submit=True)):
    nome_medicamento_cad = st.text_input('Nome: ')
    composto_medicamento_cad = st.text_input('composto: ')
    laboratorio_medicamento_cad = st.selectbox('laboratorio: ', options=list(Laboratorio.listar()))
    descricao_medicamento_cad = st.text_area('descricao: ')
    preco_medicamento_cad = st.number_input('preco: ', min_value=0.0)

    if tipo_medicamento_cad == 'Quimioterapico':
        submitted = st.form_submit_button("CADASTRAR Quimioterapico")
        if nome_medicamento_cad and composto_medicamento_cad and laboratorio_medicamento_cad \
                and descricao_medicamento_cad and preco_medicamento_cad:
            if submitted:
                try:
                    Quimioterapicos.cadastrar(nome_medicamento_cad.title(), composto_medicamento_cad.title(),
                                              laboratorio_medicamento_cad.title(), descricao_medicamento_cad,
                                              receita_medicamento_cad, preco_medicamento_cad)
                    st.success('Cadastro realizado')
                except:
                    e = ValueError('Medicamento já cadastrado')
                    st.exception(e)

        else:
            st.info('Preencha com todos os dados')
    if tipo_medicamento_cad == 'Fitoterapico':
        submitted = st.form_submit_button("CADASTRAR Fitoterapico")
        if nome_medicamento_cad and composto_medicamento_cad and laboratorio_medicamento_cad \
                and descricao_medicamento_cad and preco_medicamento_cad:
            if submitted:
                try:
                    Fitoterapicos.cadastrar(nome_medicamento_cad.title(), composto_medicamento_cad.title(),
                                            laboratorio_medicamento_cad.title(), descricao_medicamento_cad,
                                            preco_medicamento_cad)
                    st.success('Cadastro realizado')
                except:
                    e = ValueError('Medicamento já cadastrado')
                    st.exception(e)

        else:
            st.info('Preencha com todos os dados')

cad_venda_wind = tab4.container()

data_hoje = date.today()
data_hoje = data_hoje.strftime("%d/%m/%y")
data_venda = cad_venda_wind.text(f'Hoje é : {data_hoje}')
datacol, horacol = cad_venda_wind.columns(2)
data_select = datacol.date_input('Data da venda', format="DD/MM/YYYY")
data_select = data_select.strftime("%d/%m/%y")
hora_select = horacol.time_input('Horario da venda')
hora_select = hora_select.strftime("%H:%M")
cliente_select = cad_venda_wind.multiselect('CPF do cliente', options=Cliente.listar(), max_selections=1)
if cliente_select:
    cliente_select = cliente_select[0]
    medcol, quantcol = cad_venda_wind.columns([2, 1])
    medicamento_select = medcol.selectbox('Medicamento: ', options=Medicamentos.listar())

    with (quantcol.form("carrinho", clear_on_submit=False)):
        qtndcol, buttcol = st.columns(2)
        quantidade_select = qtndcol.number_input('Quantidade:', min_value=1)
        add_item_butt = buttcol.form_submit_button('Adicionar/Atualizar item')
        if add_item_butt:
            VendaTemp.registrar(cliente_select, data_select, hora_select, medicamento_select, quantidade_select, 100)

    with (cad_venda_wind.form("resgistro_venda", clear_on_submit=True)):
        resumo_venda = st.text_area('Resumo da venda', value=f'{VendaTemp.buscar(cliente_select)}')
        label_reg = st.text('Para efetivar a compra de acordo com o resumo da venda, basta clickar abaixo')
        registrar_venda = st.form_submit_button('REGISTRAR')
        if registrar_venda:
            Venda.registrar(cliente_select)
            st.success('Compra registrada')
