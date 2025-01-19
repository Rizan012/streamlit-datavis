import pandas as pd
import numpy as np
import streamlit as st

st.title("Data Visualization")

upload = st.file_uploader("Upload CSV file", type="csv")

if upload:
    data = pd.read_csv(upload)

    st.header("Data-set head view:")
    st.table(data.head(5))

    st.header("Data-set described view:")
    st.table(data.describe())

    st.markdown("---")

    st.header("Statistical Analysis")

    num_col = data.select_dtypes(["int64", "float64"])
    cat_col = data.select_dtypes(["object"])
    opn = ["Mean", "Median", "Mode", "Max", "Min"]

    cat_op = st.multiselect("Select a categorical column", options=cat_col.columns)
    num_op = st.multiselect("Select a numeric column", options=num_col.columns)
    opn_op = st.selectbox("Select a statistical operation", options=opn)

    if opn_op in ["Mean", "Median", "Max", "Min"]:
        cat_op = []
        st.warning("Choose appropriate options.")

    if num_op and opn_op:
        stat_func = {
            "Mean": data[num_op].mean(),
            "Median": data[num_op].median(),
            "Max": data[num_op].max(),
            "Min": data[num_op].min(),
            "Mode": data[num_op].mode().iloc[0]  
        }

        st.table(stat_func.get(opn_op))


    if cat_op and num_op and opn_op:
        groupby_func = {
            "Mean": data.groupby(cat_op)[num_op].mean(),
            "Median": data.groupby(cat_op)[num_op].median(),
            "Max": data.groupby(cat_op)[num_op].max(),
            "Min": data.groupby(cat_op)[num_op].min(),
            "Mode": data.groupby(cat_op)[num_op].apply(lambda x: x.mode().iloc[0] if not x.mode().empty else None)  
        }
        st.table(groupby_func.get(opn_op))

    st.markdown("---")
