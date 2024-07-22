from pydantic import BaseModel
from typing import List, Optional

class SearchQuery(BaseModel):
    query: str
    sources: Optional[List[str]] = None
