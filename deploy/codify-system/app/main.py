from fastapi import FastAPI, Request
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from app.model import get_embedding

app = FastAPI()
client = QdrantClient(host="localhost", port=6333)

COLLECTION_NAME = "codify_system"

@app.on_event("startup")
def init_qdrant():
    from qdrant_client.models import VectorParams, Distance
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )

@app.post("/add/")
async def add_item(request: Request):
    data = await request.json()
    vector = get_embedding(data["text"])
    payload = data.get("payload", {})
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[PointStruct(id=data["id"], vector=vector, payload=payload)]
    )
    return {"status": "inserted"}

@app.post("/search/")
async def search_item(request: Request):
    data = await request.json()
    vector = get_embedding(data["text"])
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        limit=3,
        with_payload=True,
    )
    return {"matches": [r.payload for r in results]}
