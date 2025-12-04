import streamlit as st
from PIL import Image

# --- ÍCONE NO TOPO ---
icon = Image.open("icon.png")
st.image(icon, width=100)

# --- ESTILO: “GRIMÓRIO REAL” (AZUL + DOURADO) ---
st.markdown("""
    <style>

        /* Fundo com pergaminho mágico */
        body {
            background: #f3efe4;
        }

        /* Container geral com textura suave */
        .stApp {
            background: linear-gradient(180deg, #fbf7ee 0%, #e8e0cf 40%, #f6f2e8 100%);
            padding: 20px;
            color: #2d2d2d;
            font-family: "Garamond", serif;
        }

        /* Títulos azul-royal */
        h1, h2, h3, h4 {
            color: #1c3f7c !important;
            text-shadow: 0px 0px 6px rgba(28,63,124,0.3);
            font-family: "Palatino Linotype", "Georgia", serif;
        }

        /* Ornamento dourado acima e abaixo do título */
        h1::before, h1::after {
            content: "";
            display: block;
            height: 3px;
            margin: 6px 0;
            background: linear-gradient(to right, transparent, #d8b46a, transparent);
        }

        /* Inputs com moldura dourada */
        .stTextInput > div > div > input {
            background: #ffffff !important;
            border-radius: 8px !important;
            border: 2px solid #d8b46a !important;
            padding: 8px !important;
        }

        /* Selectbox estilizado */
        .stSelectbox > div > div {
            background: #ffffff !important;
            border-radius: 8px !important;
            border: 2px solid #d8b46a !important;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
        }

        /* Botão dourado mágico */
        div.stButton > button {
            background-color: #d8b46a;
            color: #fff;
            border-radius: 10px;
            border: none;
            padding: 10px 22px;
            font-size: 18px;
            font-family: "Georgia", serif;
            font-weight: bold;
            box-shadow: 0px 3px 7px rgba(140,110,60,0.5),
                        inset 0px 0px 6px rgba(255,255,255,0.5);
            transition: 0.15s ease-in-out;
        }

        div.stButton > button:hover {
            background-color: #e5c787;
            transform: scale(1.05);
            box-shadow: 0px 4px 10px rgba(140,110,60,0.7),
                        inset 0px 0px 8px rgba(255,255,255,0.7);
        }

        /* Separadores estrelados */
        hr {
            border: 0;
            height: 2px;
            margin-top: 25px;
            margin-bottom: 25px;
            background: linear-gradient(to right, transparent, #d8b46a, transparent);
        }

        /* Card com moldura dourada */
        .royal-card {
            background: #fefcf7;
            border: 2px solid #d8b46a;
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 0 12px rgba(216,180,106,0.3);
            margin-top: 10px;
            margin-bottom: 10px;
        }

        /* Mensagem de erro estilizada */
        .stAlert {
            background: #fff3d6 !important;
            color: #7a5f32 !important;
            border-left: 5px solid #d8b46a !important;
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
st.caption("Um grimório real para converter idades entre raças fantásticas — com a elegância azul e dourada da realeza arcana.")

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
