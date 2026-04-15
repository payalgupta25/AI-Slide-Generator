import os
import asyncio
from dotenv import load_dotenv

from llama_index.core import VectorStoreIndex, Document
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.settings import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


class Summarizer:
    def __init__(self):
        Settings.llm = GoogleGenAI(
            model="gemini-2.5-flash",
            api_key=GOOGLE_API_KEY
        )

        Settings.embed_model = HuggingFaceEmbedding(
            model_name="BAAI/bge-small-en-v1.5"
        )

    async def summarize_text(self, text):
        documents = [Document(text=text)]
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine()

        response = await query_engine.aquery(
            "Convert this into structured PowerPoint slides with title and bullet points"
        )

        return str(response)


if __name__ == "__main__":
    text = """
    Slide_Number | Title | Subtitle | Bullet_1 | Bullet_2 | Bullet_3 | Image_Path
    1 | Introduction | Overview of the Project | Project background | Objectives | Scope | images/intro.png
    2 | Problem Statement | What issue are we solving? | Current challenges | User pain points | Impact | images/problem.png
    3 | Solution | How our solution works | Architecture overview | Key features | Technology stack | images/solution.png
    4 | Conclusion | Final Thoughts | Summary | Future scope | Thank you | images/conclusion.png
    """

    summarizer = Summarizer()
    summary = asyncio.run(summarizer.summarize_text(text))

    print("\n **Summary:**\n")
    print(summary)