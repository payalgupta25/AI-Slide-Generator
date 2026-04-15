# 🚀 Agentic-PPTGen: AI-Powered Slide Generator

**Agentic-PPTGen** is an intelligent automation system that transforms unstructured data—PDFs, CSVs, and Documents—into professional, structured PowerPoint presentations. By leveraging **LlamaIndex** and **Google Gemini**, the system "reads" your files, extracts core insights, and formats them into a ready-to-download deck.

---

## 🛠️ Tech Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **LLM Orchestration** | **LlamaIndex** | RAG (Retrieval-Augmented Generation) framework for context-aware analysis. |
| **Intelligence** | **Gemini 1.5 Flash** | High-speed reasoning for summarization and bullet-point generation. |
| **Frontend** | **Streamlit** | Interactive UI for seamless file management and generation. |
| **Embeddings** | **HuggingFace (BGE Small)** | Local, high-performance text vectorization for semantic search. |
| **File Parsing** | **PyMuPDF / Docx / Pandas** | Robust extraction across multiple data formats. |
| **PPTX Engine** | **python-pptx** | Programmatic slide creation and layout management. |

---

## 🧠 System Implementation

### 1. Multi-Modal Content Extraction
The `ContentExtractor` agent acts as the data specialist. It handles:
* **PDFs:** Deep text extraction using `fitz` (PyMuPDF).
* **Word (.docx):** Structured paragraph parsing via `python-docx`.
* **CSVs:** Data transformation from tabular formats into LLM-readable strings.

### 2. Semantic Summarization (RAG)
Unlike basic text-splitting, the `Summarizer` agent builds a **VectorStoreIndex**. It understands the *context* of your document, allowing the LLM to create logical slide titles and concise bullet points that capture the essence of the source material.

### 3. Automated Slide Engineering
The `SlideGenerator` converts AI-generated text into a physical file:
* **Auto-Formatting:** Generates a Title Slide followed by detailed content slides.
* **Smart Splitting:** Automatically detects if content is too long and splits it across multiple slides (e.g., "Part 1", "Part 2") to maintain readability.
* **Instant Export:** Provides a `.pptx` download link compatible with PowerPoint and Google Slides.

---

## 🏗️ Project Architecture

```bash
AGENTIC-PPTGEN/
├── src/
│   ├── agents/
│   │   ├── content_extractor.py  # File parsing logic
│   │   ├── slide_generator.py    # PPTX creation logic
│   │   └── summarizer.py         # LlamaIndex & Gemini logic
│   └── data/                     # Local storage for uploads
├── app.py                        # Main Streamlit UI & Entry Point
├── requirements.txt              # Dependency Manifest
└── runtime.txt                   # Environment config (Python 3.11)
```

## 🚀 Getting Started
### 1. Prerequisites
Python 3.11

Google AI (Gemini) API Key

### 2. Installation

```bash
# Clone the repository
git clone [https://github.com/payalgupta25/ai-slide-generator.git](https://github.com/payalgupta25/ai-slide-generator.git)

# Navigate to directory
cd ai-slide-generator

# Install dependencies
pip install -r requirements.txt

```

### 3. Environment Setup
Add your API key to a .env file or your Streamlit Cloud Secrets:

Plaintext
GOOGLE_API_KEY=your_gemini_api_key_here
### 4. Usage
Bash
streamlit run app.py
### 🛡️ About the Developer
Developed by Payal Gupta, a Full-Stack Developer and UI/UX Designer. This project demonstrates the intersection of Agentic Workflows and Automated Document Processing.
