import os
import pandas as pd
import fitz
from docx import Document
from llama_index.core import SimpleDirectoryReader


class ContentExtractor:
    def __init__(self, directory="data/"):
        self.directory = directory

    def extract_text_from_txt(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    
    def extract_text_from_pdf(self, file_path):
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text("text")+"\n"
        return text
    
    def extract_text_from_docx(self, file_path):
        doc = Document(file_path)
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        return text
    

    def extract_text_from_csv(self, file_path):
        df = pd.read_csv(file_path)
        text = df.to_string(index=False)
        return text
    
    def extract_from_file(self, file_path):
        _, ext = os.path.splitext(file_path)
        if ext == ".txt":
            return self.extract_text_from_txt(file_path)
        elif ext == ".pdf":
            return self.extract_text_from_pdf(file_path)
        elif ext == ".docx":
            return self.extract_text_from_docx(file_path)
        elif ext == ".csv":
            return self.extract_text_from_csv(file_path)
        else:
            raise ValueError(f"Unsupported file format: {ext}")
        
    
    def extract_from_directory(self):
        extracted_data = {}
        if not os.path.exists(self.directory):
            raise FileNotFoundError(f"Directory not found: {self.directory}")
        
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                try:
                    extracted_data[filename] = self.extract_from_file(file_path)

                except Exception as e:
                    print(f"Error extracting content from {file_path}: {e}")
        return extracted_data
    

if __name__ == "__main__":
    content_extractor = ContentExtractor(directory="data/")
    extracted_data = content_extractor.extract_from_directory()

    for file, content in extracted_data.items():
        print(f"\n Extracted content from {file}: \n {content[:500]}....\n")
        