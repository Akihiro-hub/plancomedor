import streamlit as st

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


