# 🤖 AutoML Analyst – LLM-Powered Data Assistant

AutoML Analyst is a local, open-source data assistant that uses a lightweight LLM (like Mistral via Ollama or Codestral) to help you explore and understand CSV datasets. Upload your data, run automated EDA, and chat with your dataset in plain English — all from a clean Streamlit UI.

---

## ✨ Features

- 📊 Automated dataset preview + EDA
- 💬 Ask natural language questions about your dataset
- 🧠 Powered by a local LLM (e.g., Mistral, Codestral)
- 🖥️ Streamlit-based UI, no web deployment needed
- 🔓 100% open-source, runs fully offline

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/LLM-Powered-Data-Assistant.git
cd LLM-Powered-Data-Assistant
````

### 2. Set Up Environment

Install dependencies (Python 3.9+ recommended):

```bash
pip install -r requirements.txt
```

Make sure Ollama is installed and running:

* [https://ollama.com](https://ollama.com)

You should have a local model like `mistral` or `codestral` installed:

```bash
ollama run mistral
# or
ollama run codestral
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 🧠 Example Queries

* Which column has the most missing values?
* How many unique values are in the "Gender" column?
* What is the average salary?
* Show me rows where "Team" is null.

---

## 💡 Tech Stack

* Python
* Streamlit
* Pandas, Seaborn, Matplotlib
* LangChain
* Ollama + Mistral or Codestral (LLMs)
* streamlit-chat

---

## 📁 Project Structure

```
├── app.py
├── agent_setup.py
├── utils/
│   ├── data_utils.py
│   ├── llm_utils.py
│   └── pandas_data_tool.py
├── screenshots/
├── requirements.txt
└── README.md
```

---

## 🛠️ Notes

* This tool is for **local/offline usage only** (no cloud APIs or data sharing).
* For best results, ask simple, structured questions based on your CSV.

---

## 🧪 License

MIT License. Free for personal and educational use.

---

## 🙌 Contributions

Feel free to fork, improve, and contribute via PRs!
