import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from transformers import pipeline  # ✅ Added BART

# Import audit functions
from healthcare_audit import audit_healthcare_policy
from labour_audit import audit_labour_policy
from corporate_audit import audit_corporate_policies

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize models
model = genai.GenerativeModel("gemini-2.5-flash")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # ✅ BART summarizer

# Streamlit UI
st.set_page_config(page_title="Policy Audit & Remedy System", layout="wide")
st.title("📑 Policy Audit & Remedy System")
st.write("Upload your policies and get a professional AI-audited compliance report.")

# Sidebar menu
audit_type = st.sidebar.selectbox(
    "Select Audit Type",
    ["Healthcare Audit", "Labour Audit", "Corporate Audit"]
)

# --- Healthcare Audit ---
if audit_type == "Healthcare Audit":
    st.subheader("🏥 Healthcare Policy Audit")
    uploaded_file = st.file_uploader("Upload your healthcare policy (PDF)", type=["pdf"])

    if uploaded_file:
        with st.spinner("Auditing healthcare policy..."):
            with open("temp_healthcare.pdf", "wb") as f:
                f.write(uploaded_file.read())

            results = audit_healthcare_policy("temp_healthcare.pdf")

            # Step 1: Summarize with BART
            bart_summary = summarizer(
                str(results), max_length=250, min_length=80, do_sample=False
            )[0]['summary_text']

            # Step 2: Refine with Gemini
            summary_prompt = f"""
            Rewrite this healthcare audit summary in under 200 words,
            highlighting compliance gaps, similarities, and remedies:\n\n{bart_summary}
            """
            response = model.generate_content(summary_prompt)

            st.success("Audit Completed ✅")
            st.write(response.text)

# --- Labour Audit ---
elif audit_type == "Labour Audit":
    st.subheader("⚖️ Labour Policy Audit")
    uploaded_file = st.file_uploader("Upload your labour document (PDF)", type=["pdf"])

    if uploaded_file:
        with st.spinner("Auditing labour policy..."):
            with open("temp_labour.pdf", "wb") as f:
                f.write(uploaded_file.read())

            results = audit_labour_policy("temp_labour.pdf")

            # Step 1: Summarize with BART
            bart_summary = summarizer(
                str(results), max_length=250, min_length=80, do_sample=False
            )[0]['summary_text']

            # Step 2: Refine with Gemini
            summary_prompt = f"""
            Rewrite this labour audit summary in under 200 words,
            highlighting compliance %, legal gaps, and remedies:\n\n{bart_summary}
            """
            response = model.generate_content(summary_prompt)

            st.success("Audit Completed ✅")
            st.write(response.text)

# --- Corporate Audit ---
elif audit_type == "Corporate Audit":
    st.subheader("🏢 Corporate Policy Comparison Audit")
    uploaded_file_a = st.file_uploader("Upload Company Policy A (PDF)", type=["pdf"], key="a")
    uploaded_file_b = st.file_uploader("Upload Company Policy B (PDF)", type=["pdf"], key="b")

    if uploaded_file_a and uploaded_file_b:
        with st.spinner("Comparing corporate policies..."):
            with open("temp_corp_a.pdf", "wb") as f:
                f.write(uploaded_file_a.read())
            with open("temp_corp_b.pdf", "wb") as f:
                f.write(uploaded_file_b.read())

            results = audit_corporate_policies("temp_corp_a.pdf", "temp_corp_b.pdf")

            # Step 1: Summarize with BART
            bart_summary = summarizer(
                str(results), max_length=250, min_length=80, do_sample=False
            )[0]['summary_text']

            # Step 2: Refine with Gemini
            summary_prompt = f"""
            Rewrite this corporate audit summary in under 200 words,
            highlighting similarity score, key conflicts, and alignment strategies:\n\n{bart_summary}
            """
            response = model.generate_content(summary_prompt)

            st.success("Audit Completed ✅")
            st.write(response.text)
