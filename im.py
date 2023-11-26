import chromadb
import jsonlines
client = chromadb.PersistentClient()
posts = client.get_or_create_collection(
    name = "posts"
)
ids_input=[str(i+1) for i in range(761)]



hn_dataset = []

with jsonlines.open("mo.jsonl") as f:
    for line in f.iter():
        hn_dataset.append(line["messages"][1]["content"])


posts.add(
    documents=hn_dataset,
    ids = ids_input
)


##############################################


