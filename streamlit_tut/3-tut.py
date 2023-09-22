import numpy as np
import altair as plt
import pandas as pd
import streamlit as st

if __name__ == '__main__':
    st.header('st.write')
    st.write('Hello,*world!* :sunglasses:')
    st.write(1234)
    df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
    st.write(df)
    st.write('Below is a DataFrame:', df, 'Above is a DataFrame')
    df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
    c = plt.Chart(df2).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
    )
    st.write(c)