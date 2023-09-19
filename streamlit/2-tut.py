import streamlit as st
import random

if __name__ == '__main__':
    # to add text
    st.write('Hello, world')
    # to add button
    st.header('Trying button')
    if st.button('Say Hello'):
        st.write('Hi Hello there')
    else:
        st.write(f'Good bye: {random.randint(1, 100)}')

