import streamlit as st
from datetime import time, datetime

if __name__ == '__main__':
    st.header('st.slider')
    st.subheader('Slider creating')
    age = st.slider('How old are you?', 0, 130, 25)
    st.write("I'm ", age, 'years old')

    # Example 2
    st.subheader('Range slider')
    value = st.slider('Select range of values', 0.0, 100.0, (25.0, 75.0))

    st.write('Value range', value)

    # Example 3
    st.subheader('Range time slider')
    appointment = st.slider('Schedule your appointment:',
                            value =(time(11,30), time(12, 45)))
    st.write("you're scheduler for:", appointment)

    # example 4
    st.subheader('Datatime slider')
    start_time = st.slider('When do you stat?', value=datetime(2023, 10, 2, 8, 50),
                           format="MM/DD/YYYY -hh:mm")
    st.write("start time:", start_time)


