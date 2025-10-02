import streamlit as st
import pandas as pd

from mypackage.utils import square

st.title("🔧 Repro App with Editable Install")

st.write("This app is installed via `pip install -e .`")

nums = [1, 2, 3, 4]
data = pd.DataFrame({
    "numbers": nums,
    "squares": [square(x) for x in nums]
})

st.write("Here’s a dataframe using a helper from the package:")
st.dataframe(data)

