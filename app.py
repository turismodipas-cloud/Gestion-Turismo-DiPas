import streamlit as st
from datetime import datetime, timedelta

# Configuración de la página para que se vea bien en celulares
st.set_page_config(page_title="Turismo DiPas - Gestión", layout="centered")

st.title("🏨 Gestión de Turismo DiPas")
st.subheader("Panel de Control Profesional")

# --- 1. SELECCIÓN DE PROPIEDAD Y FOTOS ---
st.markdown("### 🏠 Propiedad")
propiedad = st.selectbox("Seleccione la cabaña/departamento:", 
    ["Santa Catalina - Cabaña 3 (Monoambiente)", 
     "Santa Catalina - Cabaña 4 (Grande)", 
     "San Jacinto - Monoambiente", 
     "Viamonte 1", 
     "Viamonte 6",
     "Bonett"])

# Simulación de galería (Aquí es donde usted subiría sus fotos)
if st.button("📸 Ver fotos de la propiedad"):
    st.info("Aquí se desplegaría la galería de imágenes del alojamiento seleccionado.")

# --- 2. PRECIOS Y FECHAS ---
st.markdown("### 📅 Reserva y Precios")
col1, col2 = st.columns(2)

with col1:
    fecha_ingreso = st.date_input("Fecha de Ingreso", datetime.now())
with col2:
    fecha_egreso = st.date_input("Fecha de Egreso", datetime.now() + timedelta(days=3))

noches = (fecha_egreso - fecha_ingreso).days
precio_por_noche = st.number_input("Precio por noche (en pesos argentinos)", value=120000, step=5000)

if noches > 0:
    total_estadia = noches * precio_por_noche
    st.success(f"**Total de la estadía por {noches} noches: {total_estadia:,} pesos argentinos**")
else:
    st.error("La fecha de egreso debe ser posterior a la de ingreso.")

# --- 3. DATOS DEL HUÉSPED Y ALERTAS ---
st.markdown("### 👤 Información del Cliente")
nombre_huesped = st.text_input("Nombre completo del huésped")
contacto = st.text_input("WhatsApp de contacto (ej: +549...)")

# Lógica de aviso de llegada
fecha_aviso = fecha_ingreso - timedelta(days=3)
st.warning(f"🔔 **Recordatorio:** Se debe dar aviso de llegada el día: {fecha_aviso.strftime('%d/%m/%Y')}")

# --- 4. GUARDAR ---
if st.button("💾 Registrar Reserva"):
    # Aquí el programa enviaría los datos a su base de datos privada
    st.balloons()
    st.write(f"Reserva confirmada para {nombre_huesped} en {propiedad}.")
