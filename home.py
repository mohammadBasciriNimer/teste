import streamlit as st
from interfaces.screens.users import login

def toggle_navbar(show: bool):
    if show:
        st.markdown("""
        <style>
            [data-testid="stSidebar"] { display: block !important; }
            [data-testid="stSidebarNav"] { display: block !important; }
            [data-testid="collapsedControl"] { display: block !important; }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
            [data-testid="stSidebar"] { display: none !important; }
            [data-testid="stSidebarNav"] { display: none !important; }
            [data-testid="collapsedControl"] { display: none !important; }
        </style>
        """, unsafe_allow_html=True)

def main():
    st.session_state.setdefault("authenticated", False)
    st.session_state.setdefault("username", "")
    st.session_state.setdefault("group", "")

    if st.session_state["authenticated"]:
        grupos_usuario = set(st.session_state.get("group", []))

        toggle_navbar(True)
        pages = {}

        pages['🏠 Bem-Vindo'] = [
            st.Page(
                page='interfaces/screens/home.py',
                title='Home',
                url_path='dataengine',
                default=True
            )]

        if 'acesso_ti' in grupos_usuario or 'Autenticacao_Housesrio_Fiscal' in grupos_usuario:
            pages['🧾 Fiscal'] =  [
                st.Page(
                    page='interfaces/screens/invoices/consulta_envio_email_nfs.py',
                    title='Envio Nota Fiscal Serviço',
                    url_path='consulta-nota-fiscal-servico-email'
                ),
                st.Page(
                    page='interfaces/screens/invoices/consulta_nfs.py',
                    title='Notas Fiscais Serviço',
                    url_path='notas-fiscais-servico'
                )]                                

        if 'acesso_ti' in st.session_state["group"]:
            pages["💻 TI"] = [
                st.Page(
                    page='interfaces/screens/invoices/settings_send_nfs.py',
                    title='Configuração',
                    url_path='configuracao-nfs'            
                )]

        pg = st.navigation(pages=pages, position='sidebar')

        with st.sidebar:
            if st.button("🚪 Sair", width='stretch', type='primary'):
                st.session_state["authenticated"] = False
                st.session_state["username"] = ""
                st.session_state["group"] = ""
                st.query_params.clear()
                st.rerun()

        pg.run()

    else:
        toggle_navbar(False)
        login.show_page_login()

    if __name__ == "__main__":
        # query = st.query_params
        # token = query.get('token')
        
        main()