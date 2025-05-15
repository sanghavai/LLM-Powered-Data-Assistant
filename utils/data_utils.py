import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def preview_dataset(df):
    st.subheader("Dataset preview")
    st.write(df.head())

    st.subheader("Basic info")
    st.write(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")

    st.subheader("Column names")
    st.write(df.columns.tolist())

    st.subheader("Missing values")
    missing = df.isnull().sum()
    st.write(missing[missing > 0])


def show_eda(df, method="pearson"):
    st.subheader("📈 Univariate Distributions")
    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    num_cols = 2  # Number of plots per row
    rows = [numeric_cols[i:i + num_cols] for i in range(0, len(numeric_cols), num_cols)]

    for row in rows:
        cols = st.columns(len(row))
        for i, col_name in enumerate(row):
            with cols[i]:
                st.markdown(f"**{col_name}**")
                fig, ax = plt.subplots()
                sns.histplot(df[col_name].dropna(), kde=True, ax=ax)
                st.pyplot(fig)

    # Wrap correlation matrix in expander
    with st.expander("🔗 Correlation Matrix"):
        st.write(f"**Method:** `{method}`")

        if len(numeric_cols) >= 2:
            corr = df[numeric_cols].corr(method=method)

            fig, ax = plt.subplots(figsize=(6, 4))
            sns.heatmap(
                corr,
                annot=True,
                fmt=".2f",
                cmap="coolwarm",
                linewidths=0.5,
                linecolor='gray',
                annot_kws={"size": 8},
                cbar_kws={'shrink': 0.5}
            )
            plt.xticks(rotation=45, fontsize=8)
            plt.yticks(rotation=0, fontsize=8)
            st.pyplot(fig)
        else:
            st.info("Not enough numeric columns for correlation matrix.")
