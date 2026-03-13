from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled,NoTranscriptFound
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.retrievers import BaseRetriever
from langchain_huggingface import ChatHuggingFace
from dotenv import load_dotenv , find_dotenv
load_dotenv()

# Step 1 : Load Document  
video_id = "Ti5vfu9arXQ" # only the ID, not full URL
try:
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    transcript = transcript_list.find_transcript(["en"])

    transcript_data = transcript.fetch()

    if not transcript_data:
        raise ValueError("Empty transcript received")

    text = " ".join(chunk["text"] for chunk in transcript_data)
    print(text)

except Exception as e:
    print("Transcript fetch failed:", e)