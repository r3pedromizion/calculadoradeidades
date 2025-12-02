import streamlit as st

# 🌈 --- ESTILO FOFO (CSS) ---
st.markdown("""
    <style>
        /* Fundo geral */
        body {
            background: #ffeef8;
        }

        /* Container principal */
        .stApp {
            background: linear-gradient(180deg, #fff6fd 0%, #ffe6f5 40%, #ffdef2 100%);
            padding: 20px;
        }

        /* Caixas de seleção e input */
        .stSelectbox, .stTextInput {
            background: #ffffff !important;
            border-radius: 12px !important;
            padding: 8px !important;
            border: 2px solid #ffb6d9 !important;
        }

        /* Botão fofinho */
        div.stButton > button {
            background-color: #ffb6d9;
            color: white;
            border-radius: 12px;
            padding: 10px 20px;
            border: none;
            font-size: 18px;
            font-weight: bold;
            box-shadow: 0px 3px 6px rgba(0,0,0,0.15);
        }

        /* Botão hover */
        div.stButton > button:hover {
            background-color: #ff9ccf;
            transform: scale(1.05);
        }

        /* Títulos */
        h1, h2, h3, h4 {
            color: #ff69b4;
            font-family: "Comic Sans MS", "Poppins", sans-serif;
        }

        /* Linhas divisórias */
        hr {
            border: 2px solid #ffb6d9;
        }
    </style>
""", unsafe_allow_html=True)



# -------------------- CLASSE RAÇA --------------------

class Raca:
    def __init__(self, nome, fator_de_conversao):
        self.nome = nome
        self.fator_de_conversao = fator_de_conversao

    def calcular_idade_humana(self, idade_real):
        try:
            idade_convertida_float = float(idade_real) * self.fator_de_conversao
            idade_convertida_int = int(round(idade_convertida_float))
            return idade_convertida_int
        except ValueError:
            return None


# -------------------- DADOS DAS RAÇAS --------------------

DICT_RACAS = {
    "Humano": 1.0,
    "Sereia/Tritão": 0.125,
    "Autômato": 1.0,
    "Celestial": 0.054,
    "Kemono": 0.1,
    "Draconato": 0.05,
    "Elfo": 0.076,
    "Vampiro Puro": 0.06,
    "Vampiro Transformado": 0.083,
    "Abissal": 0.04
}

# -------------------- INTERFACE STREAMLIT --------------------

st.title("🌸✨ Calculadora de Idades Inter-Raciais ✨🌸")
st.write("Converta idades entre raças mágicas de forma fofinha e fácil! 💖🧝‍♂️🐉")

st.subheader("🌟 Escolha as Raças")

raca_pai = st.selectbox("Raça do PAI/MÃE:", list(DICT_RACAS.keys()))
raca_filho = st.selectbox("Raça do FILHO:", list(DICT_RACAS.keys()))

obj_pai = Raca(raca_pai, DICT_RACAS[raca_pai])
obj_filho = Raca(raca_filho, DICT_RACAS[raca_filho])

st.subheader("🍼 Informe as Idades")

idade_pai = st.text_input(f"Idade real do {raca_pai} (PAI/MÃE):")
idade_filho = st.text_input(f"Idade real do {raca_filho} (FILHO):")

if st.button("✨ Calcular ✨"):
    idade_humana_pai = obj_pai.calcular_idade_humana(idade_pai)
    idade_humana_filho = obj_filho.calcular_idade_humana(idade_filho)

    if idade_humana_pai is None or idade_humana_filho is None:
        st.error("❌ Oops! Digite apenas números válidos! 💕")
    else:
        diferenca = abs(idade_humana_pai - idade_humana_filho)

        st.subheader("💞 Resultados 💞")

        st.write(f"### 👨‍👧 PAI/MÃE ({raca_pai})")
        st.write(f"- Idade Real: **{idade_pai} anos**")
        st.write(f"- Idade Humana Equivalente: **{idade_humana_pai} anos**")

        st.write(f"### 👶 FILHO ({raca_filho})")
        st.write(f"- Idade Real: **{idade_filho} anos**")
        st.write(f"- Idade Humana Equivalente: **{idade_humana_filho} anos**")

        st.markdown("---")
        st.write(f"## 🌼 Diferença de Idade Humana: **{diferenca} anos** 🌼")
        st.markdown("---")


