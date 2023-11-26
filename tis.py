import jsonlines
import im
result = im.posts.query(
    query_texts=["성동구의 장애인"],
    n_results=1
)

result_query = result["documents"][0][0]
chat_bot = None
with jsonlines.open("mo.jsonl") as f:
    for line in f.iter():
        if line["messages"][1]["content"] == result_query:
            chat_bot = line["messages"][0]["content"]

print(chat_bot)