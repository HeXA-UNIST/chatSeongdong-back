import openai
from apikey import OPEN_AI_KEY
openai.api_key = OPEN_AI_KEY
re = openai.FineTuningJob.create(training_file="file-fOHmOjb43Xt7XmwvhBCHj0yn", model="gpt-3.5-turbo-0613")
print(re)