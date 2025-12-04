import streamlit as st
from PIL import Image

# --- ÍCONE NO TOPO ---
icon = Image.open("icon.png")
st.markdown("""
<div class="icon-container">
    <img src="icon.png" width="90">
</div>
""", unsafe_allow_html=True)


# --- ESTILO DARK GRIMÓRIO REAL ---
st.markdown("""
<style>

    /* Fundo arcano profundo */
    body {
        background: #0d1021;
    }

    /* Container com leve textura e brilho suave */
    .stApp {
        background: linear-gradient(180deg, #121527 0%, #0d1021 60%, #101323 100%);
        padding: 20px;
        color: #eae6d9 !important;
        font-family: "Garamond", serif;
    }

    /* Títulos dourado + azul profundo */
    h1, h2, h3, h4 {
        color: #d8b46a !important;
        text-shadow: 0px 0px 8px rgba(216,180,106,0.45);
        font-family: "Palatino Linotype", "Georgia", serif;
    }

    /* Ornamento dourado acima e abaixo do título */
    h1::before, h1::after {
        content: "";
        display: block;
        height: 3px;
        margin: 8px 0;
        background: linear-gradient(to right, transparent, #d8b46a, transparent);
    }

    /* Texto comum */
    p, label, span, div {
        color: #eae6d9 !important;
    }

    /* Inputs */
    .stTextInput > div > div > input {
        background: #1a1d2f !important;
        border-radius: 8px !important;
        border: 2px solid #d8b46a !important;
        padding: 8px !important;
        color: #f5f2e8 !important;
        font-weight: 600;
    }

    /* Selectbox */
    .stSelectbox > div > div {
        background: #1a1d2f !important;
        border-radius: 8px !important;
        border: 2px solid #d8b46a !important;
        color: #f5f2e8 !important;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.4);
    }

    /* Dropdown menu */
    .css-26l3qy-menu, .stDropdown > div {
        background: #151726 !important;
        color: #f5f2e8 !important;
        border: 1px solid #d8b46a !important;
    }

    /* Botão dourado */
    div.stButton > button {
        background-color: #d8b46a;
        color: #0d1021;
        border-radius: 10px;
        border: none;
        padding: 10px 24px;
        font-size: 18px;
        font-family: "Georgia", serif;
        font-weight: bold;
        box-shadow: 0px 3px 10px rgba(216,180,106,0.5),
                    inset 0px 0px 6px rgba(255,255,255,0.5);
        transition: 0.15s ease-in-out;
    }

    div.stButton > button:hover {
        background-color: #e7ca90;
        transform: scale(1.05);
        box-shadow: 0px 5px 14px rgba(216,180,106,0.65);
    }

    /* Separadores dourados */
    hr {
        border: 0;
        height: 2px;
        margin-top: 25px;
        margin-bottom: 25px;
        background: linear-gradient(to right, transparent, #d8b46a, transparent);
    }

    /* Cards com moldura de grimório */
    .royal-card {
        background: #151726;
        border: 2px solid #d8b46a;
        border-radius: 12px;
        padding: 15px;
        color: #f1ede3 !important;
        box-shadow: 0 0 14px rgba(216,180,106,0.25);
        margin-top: 10px;
        margin-bottom: 10px;
    }

    /* Alertas */
    .stAlert {
        background: #3a2e14 !important;
        color: #f1ddae !important;
        border-left: 5px solid #d8b46a !important;
    }

    .icon-container {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    padding-left: 5px;
    margin-bottom: -10px;
}

</style>
""", unsafe_allow_html=True)



# -------------------- CLASSE --------------------

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


# -------------------- RAÇAS --------------------

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


# -------------------- INTERFACE --------------------

st.title("📘✨ Calculadora de Idades Inter-Raciais ✨📘")
st.caption("Uma ferramenta arcana para decifrar equivalências entre eras e raças — versão Grimório Real Dark.")

st.subheader("📜 Escolha as Raças")

raca_pai = st.selectbox("Raça do PAI/MÃE:", list(DICT_RACAS.keys()))
raca_filho = st.selectbox("Raça do FILHO:", list(DICT_RACAS.keys()))

obj_pai = Raca(raca_pai, DICT_RACAS[raca_pai])
obj_filho = Raca(raca_filho, DICT_RACAS[raca_filho])

st.subheader("🖋️ Informe as Idades")

idade_pai = st.text_input(f"Idade real do {raca_pai} (PAI/MÃE):")
idade_filho = st.text_input(f"Idade real do {raca_filho} (FILHO):")

if st.button("✨ Calcular"):
    idade_humana_pai = obj_pai.calcular_idade_humana(idade_pai)
    idade_humana_filho = obj_filho.calcular_idade_humana(idade_filho)

    if idade_humana_pai is None or idade_humana_filho is None:
        st.error("Por favor, insira apenas números válidos.")
    else:
        diferenca = abs(idade_humana_pai - idade_humana_filho)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("🏅 Resultados")

        st.markdown('<div class="royal-card">', unsafe_allow_html=True)
        st.write(f"### 👤 PAI/MÃE ({raca_pai})")
        st.write(f"- Idade Real: **{idade_pai} anos**")
        st.write(f"- Equivalente Humano: **{idade_humana_pai} anos**")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="royal-card">', unsafe_allow_html=True)
        st.write(f"### 👶 FILHO ({raca_filho})")
        st.write(f"- Idade Real: **{idade_filho} anos**")
        st.write(f"- Equivalente Humano: **{idade_humana_filho} anos**")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.write(f"## 👑 Diferença de Idade Humana: **{diferenca} anos** 👑")
        st.markdown("<hr>", unsafe_allow_html=True)

