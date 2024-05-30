from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class Language(BaseModel):
    locale: Optional[str] = Field(default=None, description="Language locale.")
    probability: Optional[float] = Field(default=None, description="Probability of language.")
    additionalProperties: Optional[Dict[Any, Any]] = Field(default=None)
