from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class DestinationParams(BaseModel):
    strings: Optional[List[str]] = Field(default=None, description="List of destination parameter strings.")
    additionalProperties: Optional[Dict[Any, Any]] = Field(default=None)