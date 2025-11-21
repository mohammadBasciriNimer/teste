from pathlib import Path
import streamlit as st
from src.infra.auth.user import AuthUser
from src.settings.paths import SettingsPath



def show_page_login():
    st.set_page_config(page_title="House Rio",page_icon=SettingsPath.ASSETS_PATH /'rio_circulo.png',layout='centered')
    page_col = st.columns([3,1])

    st.image(image=SettingsPath.ASSETS_PATH /'image_login.png')

    with st.form('form_login',height='stretch') as form:
        st.subheader('Login',divider=True)
        username = st.text_input("Usuário",placeholder='Usuario Rio')
        password = st.text_input("Senha",placeholder='Senha Rio',type="password")
        submit_button = st.form_submit_button("Acessar","Acessar sistema",width='stretch',type='secondary')

        if submit_button:
            if not username or not password:
                st.error('Faltou preencher algum campo')
            else:
                user_valid, group_user = AuthUser.user_valid(username,password)
                if user_valid:
                    st.session_state["authenticated"] = True
                    st.session_state["username"] = username
                    st.session_state["group"] = group_user                    
                else:
                    st.error('Usuário ou senha inválido!')