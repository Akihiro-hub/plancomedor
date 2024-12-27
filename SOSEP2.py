import streamlit as st

# Secretsからパスワードを取得
PASSWORD = st.secrets["PASSWORD"]

# パスワード認証の処理
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "login_attempts" not in st.session_state:
    st.session_state.login_attempts = 0

def verificar_contraseña():
    contraseña_ingresada = st.text_input("Introduce la contraseña:", type="password")

    if st.button("Iniciar sesión"):
        if st.session_state.login_attempts >= 3:
            st.error("Has superado el número máximo de intentos. Acceso bloqueado.")
        elif contraseña_ingresada == PASSWORD:  # Secretsから取得したパスワードで認証
            st.session_state.authenticated = True
            st.success("¡Autenticación exitosa! Marque otra vez el botón 'Iniciar sesión'.")
        else:
            st.session_state.login_attempts += 1
            intentos_restantes = 3 - st.session_state.login_attempts
            st.error(f"Contraseña incorrecta. Te quedan {intentos_restantes} intento(s).")
        
        if st.session_state.login_attempts >= 3:
            st.error("Acceso bloqueado. Intenta más tarde.")

if st.session_state.authenticated:
    # 認証成功後に表示されるメインコンテンツ
    st.write("## :blue[Planificación del monto de ventas en un comedor]") 
    st.write("###### El monto de la venta de un restaurante, comedor o cafetería se puede estimar, en base al número de asientos, aplicando esta calculadora. :green[(GuateCrece)]")  
    
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("¿Cuánto asientos tiene el comedor?", 0, 1000, 20)
        b = st.number_input("Tasa de ocupación de los asientos por los clientes (%)", 0, 100, 50)
        c = st.number_input("Veces estimadas de rotación de los clientes al día", 1, 10, 3)
    
    with col2:
        d = st.number_input("Promedio estimado de la venta por cliente (GTQ)", 1, 1000, 40)
        e = st.number_input("Días de operación al mes (Días)", 1, 31, 25)
    st.write("###### :red[La tasa de ocupación puede ser 50%, ya que sólo dos personas pueden ocupar la mesa para cuatro personas. La rotacion de los clientes al día puede ser 4 o 5 veces, como 2 rotaciones a horas de almuerzo y 2 rotaciones a horas de cena.]")
    
    E = a*d*(b/100)*c
    
    if st.button("Estimar el monto de ventas"):
        st.write("##### Resultado del cálculo: Monto esperado de la venta diaria")
        st.text(E)
        st.write("##### Resultado del cálculo: Monto esperado de la venta mensual")
        st.text(E*e)
else:
    verificar_contraseña()

