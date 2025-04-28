import os, openai, sys
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
question = " ".join(sys.argv[1:]) or "What is an AI agent?"
resp = openai.chat.completions.create(
        model="gpt-4.1-nano", 
        messages=[{"role":"user","content":question}]
)
print(resp.choices[0].message.content)