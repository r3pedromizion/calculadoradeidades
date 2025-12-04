import streamlit as st

# --- CSS PARA CENTRALIZAR QUALQUER st.image() ---
st.markdown("""
<style>
    .centered-image img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
</style>
""", unsafe_allow_html=True)

# --- ÍCONE CENTRALIZADO ---
st.markdown('<div class="centered-image">', unsafe_allow_html=True)
st.image("icon.png", width=110)
st.markdown('</div>', unsafe_allow_html=True)

# --- ESTILO DARK GRIMÓRIO REAL ---
st.markdown("""
<style>

    body {
        background: #0d1021;
    }

    .stApp {
        background: linear-gradient(180deg, #121527 0%, #0d1021 60%, #101323 100%);
        padding: 20px;
        color: #eae6d9 !important;
        font-family: "Garamond", serif;
    }

    h1, h2, h3, h4 {
        color: #d8b46a !important;
        text-shadow: 0px 0px 8px rgba(216,180,106,0.45);
        font-family: "Palatino Linotype", "Georgia", serif;
    }

    h1::before, h1::after {
        content: "";
        display: block;
        height: 3px;
        margin: 8px 0;
        background: linear-gradient(to right, transparent, #d8b46a, transparent);
    }

    p, label, span, div {
        color: #eae6d9 !important;
    }

    .stTextInput > div > div > input {
        background: #1a1d2f !important;
        border-radius: 8px !important;
        border: 2px solid #d8b46a !important;
        padding: 8px !important;
        color: #f5f2e8 !important;
        font-weight: 600;
    }

    .stSelectbox > div > div {
        background: #1a1d2f !important;
        border-radius: 8px !important;
        border: 2px solid #d8b46a !important;
        color: #f5f2e8 !important;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.4);
    }

    .css-26l3qy-menu, .stDropdown > div {
        background: #151726 !important;
        color: #f5f2e8 !important;
        border: 1px solid #d8b46a !important;
    }

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

    hr {
        border: 0;
        height: 2px;
        margin-top: 25px;
        margin-bottom: 25px;
        background: linear-gradient(to right, transparent, #d8b46a, transparent);
    }

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

    .stAlert {
        background: #3a2e14 !important;
        color: #f1ddae !important;
        border-left: 5px solid #d8b46a !important;
    }

</style>
""", unsafe_allow_html=True)


# -------------------- LÓGICA DAS RAÇAS --------------------

class Raca:
    def __init__(self, nome, fator):
        self.nome = nome
        self.fator = fator

    def converter(self, idade_real):
        try:
            return int(round(float(idade_real) * self.fator))
        except:
            return None


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
st.caption("Uma ferramenta arcana para traduzir equivalências de idade entre raças — Grimório Real Dark Edition.")

st.subheader("📜 Escolha as Raças")

raca_pai = st.selectbox("Raça do PAI/MÃE:", list(DICT_RACAS.keys()))
raca_filho = st.selectbox("Raça do FILHO:", list(DICT_RACAS.keys()))

obj_pai = Raca(raca_pai, DICT_RACAS[raca_pai])
obj_filho = Raca(raca_filho, DICT_RACAS[raca_filho])

st.subheader("🖋️ Informe as Idades")

idade_pai = st.text_input(f"Idade real do {raca_pai} (PAI/MÃE):")
idade_filho = st.text_input(f"Idade real do {raca_filho} (FILHO):")

if st.button("✨ Calcular"):
    idade_conv_pai = obj_pai.converter(idade_pai)
    idade_conv_filho = obj_filho.converter(idade_filho)

    if idade_conv_pai is None or idade_conv_filho is None:
        st.error("Por favor, insira apenas números válidos.")
    else:
        dif = abs(idade_conv_pai - idade_conv_filho)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("🏅 Resultados")

        st.markdown('<div class="royal-card">', unsafe_allow_html=True)
        st.write(f"### 👤 PAI/MÃE ({raca_pai})")
        st.write(f"- Idade Real: **{idade_pai} anos**")
        st.write(f"- Equivalente Humano: **{idade_conv_pai} anos**")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="royal-card">', unsafe_allow_html=True)
        st.write(f"### 👶 FILHO ({raca_filho})")
        st.write(f"- Idade Real: **{idade_filho} anos**")
        st.write(f"- Equivalente Humano: **{idade_conv_filho} anos**")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.write(f"## 👑 Diferença de Idade Humana: **{dif} anos** 👑")
        st.markdown("<hr>", unsafe_allow_html=True)
