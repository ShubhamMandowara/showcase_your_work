import streamlit as st

st.header('st.selectbox')
option = st.selectbox('what is your favorite color', ('blue', 'green', 'red'))
st.write('Your favorite color', option)


st.header('st.multiselect')
options = st.multiselect('what is your favorite colors',
                        ['Green', 'Red', 'Blue', 'yellow', 'orange'],
                        ['yellow', 'Green'])

st.write('Your favorite colors', options)