from src.datasources.base import DataSource
from src.models.document import Document
import requests
import os
from dotenv import load_dotenv
load_dotenv()




class NewsSource(DataSource):
    def __init__(self):
        self.source = "https://eventregistry.org/api/v1/article/getArticles"
    
    def find_documents(self):
        payload = {
            "action": "getArticles",
            "keyword": ["Japan", "environment", "carbon", "earthquake"],
            "keywordOper": "and",
            "lang": "eng",
            "articlesCount": 10,
            "resultType": "articles",
            "apiKey": os.environ.get("NEWS_API_KEY"),
            "forceMaxDataTimeWindow": 31
        }

        response = requests.post(self.source, json=payload)
        print(response.status_code, response.text)

        data = response.json()
        
        
        documents = []

        articles = data["articles"]["results"]
        for article in articles:
            title = article["title"]
            body = article["body"]
            url = article["url"]
            date = article["date"]
            curr_doc = Document(url=url, text=body, source="NewsAPI", date=date)
            documents.append(curr_doc)
        
        return documents

    




    def source_name(self):
        return "NEWSAPI"