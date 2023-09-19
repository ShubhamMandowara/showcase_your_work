import streamlit as st
import pandas as pd
import numpy as np
import time
if __name__ == "__main__":
    st.header('Its my first streamlit app!')
    st.write('Hello World!')
    output = st.button('All Set!')
    if output == True:
        st.write('All Good')
    df = pd.DataFrame()
    df['Names'] = ['joy', 'anni', 'kevi']
    df['Ages'] = [25, 23, 24]
    st.write(df)

    age = st.slider('How old are you?', 0, 130, 25)
    st.write('Age', age)

    st.header('line chart')
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.line_chart(chart_data)


    options = st.multiselect('what is your favorite colors',
                        ['Green', 'Red', 'Blue', 'yellow', 'orange'],
                        ['yellow', 'Green'])
    st.write(options)

    options_select = st.selectbox('what is your favorite colors', ('Green', 'Red', 'Blue', 'yellow', 'orange'))
    st.write(options_select)

    red_check = st.checkbox('Red')
    yellow_check = st.checkbox('Yellow')

    if red_check:
        st.write('I am Here on red check')
    if yellow_check:
        st.write('I am Here on yellow check')


    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete+1)

    st.sidebar.header('I am here on sidebar header')
    redclick = st.sidebar.button('red click')
    st.sidebar.write(redclick)