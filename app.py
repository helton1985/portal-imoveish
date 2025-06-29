
import streamlit as st
import json
from pathlib import Path

# Dados simulados
db_path = Path("db.json")
if not db_path.exists():
    with open(db_path, "w") as f:
        json.dump({"imoveis": [], "leads": []}, f)

with open(db_path, "r") as f:
    db = json.load(f)

# Login simples
st.set_page_config(page_title="CRM ImóveisH", layout="wide")
st.title("ImóveisH - CRM estilo Univen")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    user = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if user == "helton" and password == "Indira1986@":
            st.session_state.logged_in = True
        else:
            st.error("Usuário ou senha incorretos.")

def dashboard():
    st.subheader("📊 Dashboard")
    col1, col2 = st.columns(2)
    col1.metric("Total de Imóveis", len(db["imoveis"]))
    col2.metric("Total de Leads", len(db["leads"]))

def cadastrar_imovel():
    st.subheader("🏠 Cadastro de Imóvel")
    with st.form("form_imovel"):
        endereco = st.text_input("Endereço")
        valor = st.number_input("Valor de Venda", step=1000)
        cond = st.number_input("Condomínio", step=100)
        iptu = st.number_input("IPTU", step=50)
        submit = st.form_submit_button("Salvar")
        if submit:
            db["imoveis"].append({
                "endereco": endereco, "valor": valor,
                "condominio": cond, "iptu": iptu
            })
            with open(db_path, "w") as f:
                json.dump(db, f)
            st.success("Imóvel cadastrado com sucesso!")

    st.subheader("📋 Imóveis cadastrados")
    for imovel in db["imoveis"]:
        st.write(f'📍 {imovel["endereco"]} | 💰 R$ {imovel["valor"]}')
        url = f"https://wa.me/55?text=Tenho%20interesse%20no%20imóvel%20{imovel['endereco']}"
        st.markdown(f"[Enviar via WhatsApp]({url})", unsafe_allow_html=True)

def cadastrar_lead():
    st.subheader("🧑‍💼 Cadastro de Lead")
    with st.form("form_lead"):
        nome = st.text_input("Nome do Cliente")
        telefone = st.text_input("Telefone")
        interesse = st.text_input("Interesse")
        submit = st.form_submit_button("Salvar Lead")
        if submit:
            db["leads"].append({
                "nome": nome, "telefone": telefone,
                "interesse": interesse
            })
            with open(db_path, "w") as f:
                json.dump(db, f)
            st.success("Lead cadastrado!")

    st.subheader("📋 Leads cadastrados")
    for lead in db["leads"]:
        st.write(f'👤 {lead["nome"]} | 📞 {lead["telefone"]} | 🏡 {lead["interesse"]}')

if not st.session_state.logged_in:
    login()
else:
    menu = st.sidebar.selectbox("Menu", ["Dashboard", "Cadastro de Imóvel", "Cadastro de Lead"])
    if menu == "Dashboard":
        dashboard()
    elif menu == "Cadastro de Imóvel":
        cadastrar_imovel()
    elif menu == "Cadastro de Lead":
        cadastrar_lead()
