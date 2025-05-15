import streamlit as st
import pandas as pd
from utils.data_utils import preview_dataset, show_eda
from agent_setup import create_agent
from streamlit_chat import message

st.set_page_config(page_title="AutoML Analyst", layout="wide")

st.title("🤖 AutoML Analyst - LLM Powered Data Assistant")

uploaded_file = st.file_uploader("Upload your csv file", type=['csv'])

if uploaded_file:
    st.success('File uploaded successfully!')
    df = pd.read_csv(uploaded_file)
    preview_dataset(df)

    if st.button("Run EDA"):
        st.session_state.show_eda = True

    if st.session_state.get("show_eda", False):
        if "corr_method" not in st.session_state:
            st.session_state.corr_method = "pearson"

        st.session_state.corr_method = st.selectbox(
            "Choose correlation method", ["pearson", "spearman", "kendall"],
            index=["pearson", "spearman", "kendall"].index(st.session_state.corr_method),
            key="corr_method_selectbox"
        )

        show_eda(df, method=st.session_state.corr_method)

    agent = create_agent(df)

    st.markdown("### 💬 Chat with Your Dataset")
    st.markdown("""
    <div style='padding: 1rem; background-color: #808080; border-radius: 10px; margin-bottom: 1rem;'>
    🤖 <b>I am your AutoML Analyst</b> – a local LLM agent who can answer questions based on the dataset you uploaded.  <br>
    Please ask <b>only dataset-related questions</b>. For example:
    <ul>
      <li>Which column has the most missing values?</li>
      <li>How many unique values does 'Gender' have?</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Ask something about your dataset:")

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        with st.spinner("Thinking..."):
            response = agent.run(user_input)

        st.session_state.chat_history.append({"role": "assistant", "content": response})

    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            message(msg["content"], is_user=True, key=msg["content"] + "_user")
        else:
            message(msg["content"], is_user=False, key=msg["content"] + "_ai")
