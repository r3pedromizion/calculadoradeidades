import streamlit as st

# 🌙 --- ESTILO DARK OBSCURO (CSS) ---
st.markdown("""
    <style>
        /* Fundo geral */
        body {
            background: #0a0a0f;
        }

        /* Container principal */
        .stApp {
            background: linear-gradient(180deg, #0d0d16 0%, #12121f 50%, #0b0b14 100%);
            padding: 20px;
            color: #e3e3e3;
        }

        /* Títulos */
        h1, h2, h3, h4 {
            color: #a991ff !important;
            font-family: "Trebuchet MS", Arial, sans-serif;
            text-shadow: 0px 0px 8px #6e4cff;
        }

        /* Caixas de seleção e texto */
        .stSelectbox, .stTextInput {
            background: #1c1c29 !important;
            border-radius: 10px !important;
            padding: 8px !important;
            border: 2px solid #6e4cff !important;
        }

        /* Botão dark neon */
        div.stButton > button {
            background-color: #6e4cff;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
            font-size: 18px;
            font-weight: bold;
            box-shadow: 0px 0px 12px rgba(110, 76, 255, 0.6);
            transition: 0.2s ease-in-out;
        }

        /* Botão hover */
        div.stButton > button:hover {
            background-color: #8d74ff;
            transform: scale(1.05);
            box-shadow: 0px 0px 20px rgba(150, 120, 255, 0.8);
        }

        /* Texto principal */
        p, label {
            color: #d8d8e6 !important;
        }

        /* Linhas divisórias */
        hr {
            border: 1px solid #6e4cff;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        /* Caixa de mensagens de erro */
        .stAlert {
            background: #2d1a2f !important;
            border-left: 5px solid #b84cff !important;
            color: #f3d9ff !important;
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

st.title("🌙✨ Calculadora de Idades Inter-Raciais")
st.write("Entre nas sombras do conhecimento místico e descubra as idades equivalentes entre raças fantásticas. 🖤")

st.subheader("🦇 Escolha as Raças")

raca_pai = st.selectbox("Raça do PAI/MÃE:", list(DICT_RACAS.keys()))
raca_filho = st.selectbox("Raça do FILHO:", list(DICT_RACAS.keys()))

obj_pai = Raca(raca_pai, DICT_RACAS[raca_pai])
obj_filho = Raca(raca_filho, DICT_RACAS[raca_filho])

st.subheader("⌛ Informe as Idades")

idade_pai = st.text_input(f"Idade real do {raca_pai} (PAI/MÃE):")
idade_filho = st.text_input(f"Idade real do {raca_filho} (FILHO):")

if st.button("🔮 Calcular"):
    idade_humana_pai = obj_pai.calcular_idade_humana(idade_pai)
    idade_humana_filho = obj_filho.calcular_idade_humana(idade_filho)

    if idade_humana_pai is None or idade_humana_filho is None:
        st.error("⚠️ Insira apenas números válidos.")
    else:
        diferenca = abs(idade_humana_pai - idade_humana_filho)

        st.subheader("📜 Resultados")

        st.write(f"### 🕯️ PAI/MÃE ({raca_pai})")
        st.write(f"- Idade Real: **{idade_pai} anos**")
        st.write(f"- Equivalente Humano: **{idade_humana_pai} anos**")

        st.write(f"### 🔥 FILHO ({raca_filho})")
        st.write(f"- Idade Real: **{idade_filho} anos**")
        st.write(f"- Equivalente Humano: **{idade_humana_filho} anos**")

        st.markdown("---")
        st.write(f"## 🖤 Diferença de Idade Humana: **{diferenca} anos** 🖤")
        st.markdown("---")

