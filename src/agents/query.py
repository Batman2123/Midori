import anthropic
from supabase import create_client
import os
from dotenv import load_dotenv
load_dotenv()


class QueryAgent():
    def __init__(self):
        self.anthropic = anthropic.Anthropic()
        self.supabase = create_client(os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY"))
    
    
    def query(self, question):

        response = (
            self.supabase.table("documents").select("insights").execute()
        )

        print(response.data)

        message = self.anthropic.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            messages=[
                {"role": "user", "content": "Using the following content " + str(response.data) + " answer this question: " + question}
                ] 
        )    
        return message.content[0].text
