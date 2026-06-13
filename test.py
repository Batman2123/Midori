from src.datasources.news import NewsSource

news = NewsSource()
documents = news.find_documents()

for doc in documents:
    print(doc.text, doc.date, doc.url)