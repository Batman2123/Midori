"""from dotenv import load_dotenv
load_dotenv()

from src.datasources.news import NewsSource
from src.agents.analysis import AnalysisAgent
from src.models.database import DatabaseClient
from src.agents.query import QueryAgent

anal_agent = AnalysisAgent()
news_agent = NewsSource()
data_base = DatabaseClient()

documents = news_agent.find_documents()

for doc in documents:
    try:
        insight = (anal_agent.insights(doc))
        data_base.save_document(doc, insight)

    except Exception as e:
        print(f"Failed on {doc.url}: {e}")
        continue"""
from dotenv import load_dotenv
load_dotenv()

from src.agents.query import QueryAgent

query_agent = QueryAgent()
answer = query_agent.query("What are Japan's current environmental challenges?")
print(answer)
