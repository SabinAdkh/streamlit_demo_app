import numpy as np
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


st.header("st.write")
st.subheader("sub header")
st.caption("This is caption")
st.text("I'm writing some texts")
st.code("code")
st.latex("latex")
# Example 1

st.write("Hello, *world* :laughing:")

# Example 2

st.write(1234)

# Example env3

df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
st.write(df)
st.write("Below is a DataFrame:", df, "Above is a DataFrame.")


df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(df2)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.write(c)
