from dotenv import load_dotenv
load_dotenv()

from src.datasources.news import NewsSource
from src.agents.analysis import AnalysisAgent
from src.models.database import DatabaseClient

news = NewsSource()
documents = news.find_documents()

agent = AnalysisAgent()
insights = agent.insights(documents[0])
database = DatabaseClient()
database.save_document(documents[0],insights)
print(insights)