import openai
from apikey import OPEN_AI_KEY

openai.api_key = OPEN_AI_KEY
t = openai.File.create(
  file=open("mydata.jsonl", "rb"),
  purpose='fine-tune'
)

print(t)
