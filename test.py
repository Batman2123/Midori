from dotenv import load_dotenv
load_dotenv()

from src.datasources.news import NewsSource
from src.agents.analysis import AnalysisAgent

news = NewsSource()
documents = news.find_documents()

agent = AnalysisAgent()
insights = agent.insights(documents[0])
print(insights)