# 🧠 GenAI MCQ Generator

A Generative AI-based web app that takes **text or PDF input** and generates **Multiple Choice Questions (MCQs)** using **OpenAI's GPT-3.5-turbo**.
Built with **Streamlit**, this tool is ideal for students, educators, trainers, and ed-tech platforms looking to automate question generation for learning or assessments.

---

## 🚀 Features

- 📄 Accepts **.txt** or **.pdf** file input
- 🤖 Uses **GPT-3.5-turbo** for question generation
- 🧠 Automatically generates **MCQs** with 4 options and the correct answer
- 🌐 Clean and responsive **Streamlit interface**
- 📤 Displays output directly in the browser

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI)
- **OpenAI API (gpt-3.5-turbo)**
- **PyPDF2** for PDF text extraction
- **Git + GitHub** for version control
- Developed using **Jupyter Notebook** and **VS Code**

---

## 📁 Folder Structure
C:.
│   .env
│   .gitignore
│   data.txt
│   README.md
│   requirements.txt
│   Response.json
│   setup.py
│   StreamlitAPP.py
│   test.py
│
├───experiment
│       biology.csv
│       machinelearning.csv
│       mcq.ipynb
│
├───logs
├───mcqgenerator.egg-info
│       dependency_links.txt
│       PKG-INFO
│       requires.txt
│       SOURCES.txt
│       top_level.txt
│
└───src
    │   __init__.py
    │
    └───mcqgenerator
            logger.py
            MCQGenerator.py
            utils.py
            __init__.py

## 🔧 Setup Instructions

### ✅ Prerequisites

- Python 3.8+
- OpenAI API key
- Openai Base Url

- ### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/TanishaSahu03/MCQGEN1.git
cd MCQGEN1

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

🔑 Set API Key
Create a .env file and add your OpenAI key and Base Url

# Set filepath of files data.txt and Response.json

▶️ Run the App
bash
streamlit run app.py





