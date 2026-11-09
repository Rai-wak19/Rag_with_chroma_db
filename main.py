import uuid
import chromadb

client = chromadb.Client()
collection = client.create_collection(name="astu")

with open("astu.txt","r", encoding="utf-8") as f :
    astu: list[str] = f.read().splitlines()

collection.add(
    ids =[str(uuid.uuid4()) for _ in astu],
    documents = astu ,
    metadatas = [{"line": line } for line in range (len(astu))]
)

results = collection.query(
    query_texts = [
        "what can you tell me about dormitory ? "
    ]
)

for i,query_results in  enumerate(results["documents"]):
    print(f"\n Query {i}")
    print("\n".join (query_results))