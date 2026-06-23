from supabase import create_client
from src.models.document import Document
import os
from dotenv import load_dotenv
load_dotenv()

class DatabaseClient():
    def __init__(self):
        self.client = create_client(os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY"))

    def save_document(self, doc, insight):

        self.client.table("documents").insert({
        "url": doc.url,
        "text": doc.text,
        "source": doc.source,
        "date": doc.date,
        "insights": insight,
        }).execute()