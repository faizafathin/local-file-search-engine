from whoosh.qparser import MultifieldParser
from whoosh.index import open_dir

def search(query, index_dir="data/index"):
    ix = open_dir(index_dir)
    parser = MultifieldParser(["content", "filename"], schema=ix.schema)
    results = []
    with ix.searcher() as searcher:
        q = parser.parse(query)
        for hit in searcher.search(q, limit=20):
            results.append({
                "path": hit["path"],
                "tags": hit.get("tags", "")
            })
    return results
