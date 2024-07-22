from fastapi import FastAPI, HTTPException, Query, Depends, Header
from pydantic import BaseModel
from typing import List, Optional
import scholarly
import os

app = FastAPI()

class SearchQuery(BaseModel):
    query: str
    sources: Optional[List[str]] = None

API_KEY = os.getenv("API_KEY")

def get_api_key(api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

@app.get("/search", summary="Search Google Scholar", description="Search Google Scholar with an optional source filter", dependencies=[Depends(get_api_key)])
async def search(query: str, sources: Optional[List[str]] = Query(None, description="List of sources to filter by")):
    """
    Search Google Scholar with an optional source filter.

    - **query**: The search query string.
    - **sources**: Optional list of sources to filter the search results by.
    """
    try:
        search_query = query
        if sources:
            source_query = ' OR '.join([f'source:{source}' for source in sources])
            search_query += f' {source_query}'
        search_results = scholarly.search_pubs(search_query)
        results = [result.bib for result in search_results]
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
