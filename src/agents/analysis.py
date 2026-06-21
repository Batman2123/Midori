from src.models.document import Document
import anthropic


class AnalysisAgent():
    def __init__(self):
        self.client = anthropic.Anthropic()
    
    
    def insights(self, doc):
        message = self.client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            messages=[
                {"role": "user", "content": "Provide a summary of the following text including its significance to Japanese Environmental/energy policy and impact, its connection to global goals and impact, its significance toward natural disasters (i.e. earthquakes) and energy disasters if applicable, why this information matters, (the 'SO what?!'), and the type of content the document falls under \n\nArticle:\n" + doc.text}
            ] 
        )    
        return message.content[0].text
            

        