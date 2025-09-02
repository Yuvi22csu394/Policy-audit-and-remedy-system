📑 Policy Audit & Remedy System

An AI-powered compliance auditing tool that analyzes organizational policies across Healthcare, Labour, and Corporate domains.
It compares uploaded policy documents against reference standards, detects compliance gaps, and generates professional audit summaries with BART (Hugging Face Transformers) and Gemini models.

🚀 Features

🏥 Healthcare Audit – Analyze healthcare policies against compliance requirements.

⚖️ Labour Audit – Detect non-compliance with labour codes and wage acts.

🏢 Corporate Audit – Compare two corporate policies to identify conflicts and alignment opportunities.

📊 AI-Powered Summarization –

BART (transformer-based NLP model) → Creates structured summaries of raw audit results.

Gemini → Refines output into a professional, compliance-report style.

📂 PDF/Text Support – Upload your own policies for instant audit.

🌐 Streamlit UI – Simple, interactive, and ready for deployment.

🛠️ Tech Stack

Frontend: Streamlit

NLP Models: Hugging Face facebook/bart-large-cnn, Sentence Transformers (all-MiniLM-L6-v2)

LLM: Google Gemini 2.5 Flash

Libraries: transformers, sentence-transformers, scikit-learn, pdfplumber, numpy, pandas

📂 Project Structure
.
├── main.py                  # Streamlit UI entrypoint
├── healthcare_audit.py      # Healthcare policy auditing logic
├── labour_audit.py          # Labour policy auditing logic
├── corporate_audit.py       # Corporate policy comparison
├── requirements.txt         # Dependencies
├── .streamlit/
│   └── secrets.toml         # API key storage (not in GitHub)
└── README.md

⚙️ Installation & Setup
1. Clone Repository
git clone https://github.com/yourusername/policy-audit-system.git
cd policy-audit-system

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

3. Install Dependencies
pip install -r requirements.txt

4. Configure API Key

Create a .streamlit/secrets.toml file (⚠️ don’t commit to GitHub):

GEMINI_API_KEY = "your_google_gemini_api_key_here"

5. Run Locally
streamlit run main.py

🌐 Deployment (Streamlit Cloud)

Push this repo to GitHub

Go to Streamlit Cloud
 → New App

Connect your repo and select main.py

Add your GEMINI_API_KEY in Streamlit → Secrets Manager

Deploy and share your app 🚀

📊 Example Outputs
✅ Healthcare Audit

Highlights compliance %

Detects missing provisions (e.g., maternity leave, workplace safety)

Suggests remedies

✅ Labour Audit

Reports compliance score against Labour Code + Minimum Wages Act

Recommends wage adjustments and policy updates

✅ Corporate Audit

Compares two policies → returns similarity score (%)

Flags conflicts & proposes alignment strategies

⚠️ Notes

Uploaded PDFs must be under 200MB (Streamlit limit).

Your Gemini API quota will be used by all visitors.

For a fully open-source demo, disable Gemini and use only Hugging Face models.

📜 License

MIT License © 2025 – Yuvraj Mudgil
