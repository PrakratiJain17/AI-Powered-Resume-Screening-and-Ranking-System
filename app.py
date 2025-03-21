import streamlit as st
import pandas as pd
from utils.text_extraction import extract_text_from_pdf
from utils.rank_resumes import rank_resumes

# Set page configuration
st.set_page_config(
    page_title="AI Resume Screening & Ranking",
    page_icon="📄",
    layout="wide"
)

# Custom CSS for Styling & Alignment Fix
st.markdown(
    """
    <style>
        /* Full Page Background */
        .stApp {
            background-color: #0B3D91; /* Dark Blue */
            color: white;
        }

        /* Header Title */
        h1 {
            text-align: center;
            color: white;
            font-size: 34px;
            font-weight: bold;
        }

        /* Section Headers */
        h2 {
            color: white;
            font-size: 24px;
            font-weight: bold;
        }

        /* Job Description & Upload Resume Containers */
        .container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 30px;
            width: 100%;
        }

        /* Ensuring Equal Height for Both Sections */
        .box {
            width: 48%;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.2);
        }

        /* Text Area Styling */
        .stTextArea textarea {
            font-size: 18px !important;
            border-radius: 8px !important;
            border: 2px solid #FFD700 !important;
            background-color: white !important;
            color: black !important;
            height: 200px !important;
        }

        /* Style File Uploader - White Background & Larger Font */
        .stFileUploader {
            background-color: white !important;
            border-radius: 8px !important;
            padding: 12px;
            border: 2px solid #FFD700 !important;
        }

        /* Change File Uploader Label Color & Font Size */
        .stFileUploader label {
            color: white !important;
            font-size: 20px !important;
            font-weight: bold !important;
        }

        /* Style Buttons */
        .stButton>button {
            width: 100%;
            border-radius: 8px;
            background-color: #FFD700 !important;
            color: black !important;
            font-size: 18px !important;
            font-weight: bold;
        }

        /* Error Message Styling */
        .error-message {
            color: #FF6347;
            font-size: 16px;
            font-weight: bold;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<h1>📄 AI Resume Screening & Ranking System</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Using st.columns() for Perfect Alignment
col1, col2 = st.columns(2)

with col1:
    st.header("📝 Job Description")
    job_description = st.text_area("", height=200, placeholder="Type or paste job description here...")

with col2:
    st.header("📤 Upload Resumes")
    st.markdown('<p style="font-size: 16px; font-weight: bold; color: White;">📎 You can upload multiple resumes</p>', unsafe_allow_html=True)
    uploaded_files = st.file_uploader("", type=['pdf'], accept_multiple_files=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Rank Resumes Button (Always Visible)
if st.button("📊 Rank Resumes"):
    error_message = None
    
    # Check for missing inputs
    if not job_description and not uploaded_files:
        error_message = "⚠️ Please provide both a job description and upload at least one resume."
    elif not job_description:
        error_message = "⚠️ Please provide a job description."
    elif not uploaded_files:
        error_message = "⚠️ Please upload at least one resume."
    
    if error_message:
        st.markdown(f'<p class="error-message">{error_message}</p>', unsafe_allow_html=True)
    else:
        # If both inputs are present, proceed with the ranking process
        resumes_text = [extract_text_from_pdf(file) for file in uploaded_files]
        filenames = [file.name for file in uploaded_files]

        # Rank Resumes
        ranked_resumes = rank_resumes(job_description, resumes_text, filenames)

        # Display Results
        st.markdown("<h2>🏆 Ranked Resumes</h2>", unsafe_allow_html=True)
        results_df = pd.DataFrame(ranked_resumes)[["rank", "resume", "score"]].rename(columns={"rank": "Rank", "resume": "Resume", "score": "Score"})
        st.dataframe(results_df, use_container_width=True)
