import os
import shutil
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
from src.agents.slide_generator import SlideGenerator
from src.agents.content_extractor import ContentExtractor
from src.agents.summarizer import Summarizer

router = APIRouter()

upload_dir = "uploads/"

os.makedirs(upload_dir, exist_ok=True)

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Save the uploaded file to a temporary directory
    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"filename": file.filename, "message": "File uploaded successfully!"}

@router.get("/generate/")
async def generate_presentation():
    extractor = ContentExtractor(directory=upload_dir)
    extracted_content = extractor.extract_from_directory()

    summarizer = Summarizer()
    slide_generator = SlideGenerator(output_dir="output/")

    for filename, text in extracted_content.items():
        # Correctly await the async method
        summary = await summarizer.summarize_text(text)
        
        # Split by newlines to create bullet points for the slide generator
        summary_points = [p.strip() for p in summary.split("\n") if p.strip()]
        
        slide_generator.add_slide(filename, summary_points)

    pptx_path = os.path.join("output/", "generated_presentation.pptx")
    return {
        "message": "Presentation generated successfully!", 
        "download_url": f"/download/?filename={pptx_path}"
    }

@router.get("/download/")
async def download_presentation(filename: str):
    return FileResponse(filename, media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation", filename=filename)