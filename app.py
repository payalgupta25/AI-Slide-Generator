import streamlit as st
import os
import asyncio
# Import your agent classes directly
from src.agents.content_extractor import ContentExtractor
from src.agents.summarizer import Summarizer
from src.agents.slide_generator import SlideGenerator

st.set_page_config(page_title="AI Slide Generator", layout="centered")
st.title("AI based Slide Generator")

upload_file = st.file_uploader("Upload a file", type=["txt", "pdf", "docx", "csv"])

if upload_file is not None:
    # 1. Save file locally in the cloud instance
    upload_dir = "uploads/"
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, upload_file.name)
    with open(file_path, "wb") as f:
        f.write(upload_file.getbuffer())
    
    st.success(f"File '{upload_file.name}' ready for processing!")

    num_slides = st.slider("Select number of slides", min_value=2, max_value=15, value=5)

    if st.button("Generate Slide"):
        with st.spinner("Analyzing content and generating PPTX..."):
            try:
                # 2. Run your Agent logic directly (No FastAPI call needed)
                extractor = ContentExtractor(directory=upload_dir)
                extracted_content = extractor.extract_from_directory()

                summarizer = Summarizer()
                slide_generator = SlideGenerator(output_dir="output/")

                for filename, text in extracted_content.items():
                    # Use asyncio.run to call your async summarizer
                    summary = asyncio.run(summarizer.summarize_text(text, num_slides=num_slides))
                    summary_points = [p.strip() for p in summary.split("\n") if p.strip()]
                    slide_generator.add_slide(filename, summary_points)

                pptx_path = "output/generated_presentation.pptx"
                
                # 3. Provide native Streamlit download button
                if os.path.exists(pptx_path):
                    with open(pptx_path, "rb") as f:
                        st.download_button(
                            label="📥 Download Presentation",
                            data=f,
                            file_name="generated_presentation.pptx",
                            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                        )
            except Exception as e:
                st.error(f"An error occurred: {e}")