import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Slide Generator", layout="centered")

st.title("AI based Slide Generator")
st.write("Upload a file or enter text to generate a slide.")

upload_file = st.file_uploader("Upload a file", type=["txt", "pdf", "docx", "csv"])

if upload_file is not None:
    st.success("File uploaded successfully!")

    files={"file":upload_file}
    upload_response = requests.post(f"{BASE_URL}/upload/", files=files)

    if upload_response.status_code == 200:
        st.write("File uploaded successfully!")

    if st.button("Generate Slide"):
        generate_response = requests.get(f"{BASE_URL}/generate/")

        if generate_response.status_code == 200:
            st.success("Presentation generated successfully!")
            download_url = f"{BASE_URL}/download/?filename=output/generated_presentation.pptx"
            st.markdown(f"[Download Presentation]({download_url})", unsafe_allow_html=True)
        else:
            st.error("Failed to generate presentation.")
else:
    st.error("Please upload a file or enter text.")
