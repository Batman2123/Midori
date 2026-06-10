class Document():

    def __init__(self, url, text, source, date=None):
        self.url = url
        self.text = text
        self.source = source
        self.date = date