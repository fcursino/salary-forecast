import streamlit as st
import json
import requests

# título da aplicação
st.title("Modelo de Predição de Salário")

# inputs do usuário
st.write("Quantos meses o profissional está na empressa?")
tempo_na_empresa = st.slider("Meses", min_value=1, max_value=120, value=60, step=1)

st.write("Qual o nível do profissional na empressa?")
nivel_na_empresa = st.slider("Nível", min_value=1, max_value=10, value=5, step=1)

# preparar dados para a API
input_features = {
    'tempo_na_empresa': tempo_na_empresa,
    'nivel_na_empresa': nivel_na_empresa
}

# criar um botão e capturar um evento deste botão para disparar a API
if st.button('Estimar Salário'):
    res = requests.post(url='http://localhost:8000/predict', data=json.dumps(input_features))
    res_json = json.loads(res.text)
    salario_em_reais = round(res_json['salario_em_reais'], 2)
    st.subheader(f'O salário estimado é de R$ {salario_em_reais}')