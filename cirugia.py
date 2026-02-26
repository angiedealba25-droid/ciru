import streamlit as st
from datetime import datetime, timedelta
import time

# CONFIGURACIÓN
st.set_page_config(
    page_title="Dashboard Quirófano - Keralty",
    page_icon="🏥",
    layout="wide"
)

# -------- ESTILOS PREMIUM --------
st.markdown("""
<style>

/* Fondo azul oscuro tipo imagen */
.stApp {
    background: linear-gradient(135deg, #001f3f, #003566, #001f3f);
    background-attachment: fixed;
}

/* Header */
.header {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    padding: 20px;
    border-radius: 15px;
    color: white;
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}

/* Tarjetas */
.card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(10px);
    padding: 35px;
    border-radius: 20px;
    text-align: center;
    transition: 0.3s ease-in-out;
    border: 1px solid rgba(255,255,255,0.1);
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 10px 30px rgba(0, 198, 255, 0.5);
}

/* Etiquetas */
.label {
    font-size: 18px;
    color: #00c6ff;
    margin-bottom: 10px;
    font-weight: 600;
}

/* Números grandes con degradado */
.number {
    font-size: 56px;
    font-weight: bold;
    background: linear-gradient(90deg, #00c6ff, #0072ff, #001f3f);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Estado */
.status-ok {
    font-size: 42px;
    font-weight: bold;
    color: #00ffcc;
}

.status-delay {
    font-size: 42px;
    font-weight: bold;
    color: #ff4d4d;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 40px;
    color: #00c6ff;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# -------- HEADER --------
st.markdown('<div class="header">🏥 QUIRÓFANO 3 - KERALTY S.A</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------- LOGO --------
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Keralty_logo.svg/2560px-Keralty_logo.svg.png", width=220)

st.markdown("<br><br>", unsafe_allow_html=True)

# -------- INPUTS DINÁMICOS --------
col_input1, col_input2 = st.columns(2)

with col_input1:
    hora_inicio = st.time_input("Hora Inicio Cirugía", value=datetime.now().time())

with col_input2:
    duracion_estimada = st.number_input("Duración estimada (minutos)", min_value=30, max_value=600, value=90)

# -------- CÁLCULOS --------
fecha_actual = datetime.now().date()
inicio_datetime = datetime.combine(fecha_actual, hora_inicio)
hora_fin_estimada = inicio_datetime + timedelta(minutes=duracion_estimada)
hora_actual = datetime.now()

atraso = hora_actual > hora_fin_estimada

# -------- TARJETAS --------
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="label">Hora Inicio</div>
        <div class="number">{inicio_datetime.strftime("%H:%M:%S")}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="label">Quirófano</div>
        <div class="number">3</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="label">Hora Estimada Fin</div>
        <div class="number">{hora_fin_estimada.strftime("%H:%M:%S")}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    if atraso:
        st.markdown("""
        <div class="card">
            <div class="label">Estado Cirugía</div>
            <div class="status-delay">⚠ ATRASADO</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="card">
            <div class="label">Estado Cirugía</div>
            <div class="status-ok">✔ A TIEMPO</div>
        </div>
        """, unsafe_allow_html=True)

# -------- RELOJ EN TIEMPO REAL --------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
<div style='text-align:center; font-size:20px; color:#00c6ff;'>
Hora actual: {hora_actual.strftime("%H:%M:%S")}
</div>
""", unsafe_allow_html=True)

# -------- FOOTER --------
st.markdown('<div class="footer">Sistema Inteligente de Control Quirúrgico - Keralty S.A</div>', unsafe_allow_html=True)
