import streamlit as st
import pandas as pd
from utils.data_utils import preview_dataset, show_eda
from agent_setup import create_agent
from streamlit_chat import message

st.set_page_config(page_title="AutoML Analyst", layout="wide")

st.markdown("""
# 🤖 AutoML Analyst  
*LLM-Powered Exploratory Data Assistant*
""")

st.markdown("""
Upload a CSV and interact with your data using natural language.  
Get automated visualizations, correlation matrices, and more.
""")

with st.sidebar:
    st.header("📁 Upload Data")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        st.success("✅ File uploaded successfully.")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    tab1, tab2, tab3 = st.tabs(["🔍 Preview", "📊 EDA", "💬 Chat"])

    with tab1:
        preview_dataset(df)

    with tab2:
        st.markdown("### Exploratory Data Analysis")
        corr_method = st.selectbox("Select correlation method", ["pearson", "spearman", "kendall"])
        show_eda(df, method=corr_method)

    with tab3:
        agent = create_agent(df)
        st.markdown("### Ask Questions About Your Data")
        st.info("Example: *Which column has the most missing values?*")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        user_input = st.text_input("Your question:")
        if user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            with st.spinner("Thinking..."):
                response = agent.run(user_input)
            st.session_state.chat_history.append({"role": "assistant", "content": response})

        for i, msg in enumerate(st.session_state.chat_history):
            key = f"chat_{i}"
            if msg["role"] == "user":
                message(msg["content"], is_user=True, key=key)
            else:
                message(msg["content"], is_user=False, key=key)
else:
    st.info("Please upload a CSV file to get started.")
