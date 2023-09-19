import streamlit as st

st.header('st.checkbox')
st.write('What would you like to order')

icecream = st.checkbox('icecream')
coffee = st.checkbox('coffee')
cola = st.checkbox('cola')

if icecream:
    st.write('Great, Here is some more 🍦')

if coffee:
    st.write('Great, Here is some more ☕')

if cola:
    st.write('Great, Here is some more  🥤')
             