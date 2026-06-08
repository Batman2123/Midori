from dotenv import load_dotenv
load_dotenv()
import anthropic
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "What are Japan's current carbon neutrality goals?"}
    ]
)
print(message.content[0].text)