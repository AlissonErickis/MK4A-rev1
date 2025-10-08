import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Checklist de Inspeção Visual - Pintura MK4A")

# Defeitos possíveis
tipos_defeitos = [
    "Arranhões", "Bolhas", "Escorrimento", "Falha de Pintura", "Marca de Rolo",
    "Olho de Peixe", "Ondulação", "Poros", "Rugosidade", "Sujeira", "Outros"
]

# Regiões simuladas (exemplo baseado na estrutura da planilha)
regioes = {
    "CASCA WW": list(range(1, 21)),
    "CASCA LW": list(range(21, 41)),
    "BORDA DE ATAQUE": list(range(41, 61)),
    "BORDA DE FUGA": list(range(61, 81)),
    "OUTROS": [81]
}

# Layout em colunas por região
for regiao, posicoes in regioes.items():
    st.subheader(f"Região: {regiao}")
    cols = st.columns(4)
    for i, posicao in enumerate(posicoes):
        with cols[i % 4]:
            st.markdown(f"**Posição {posicao}**")
            st.selectbox(f"Tipo de Defeito {posicao}", ["Nenhum"] + tipos_defeitos, key=f"defeito_{posicao}")
            st.text_input(f"Observação {posicao}", key=f"obs_{posicao}")
            st.checkbox(f"Inspecionado", key=f"check_{posicao}")
