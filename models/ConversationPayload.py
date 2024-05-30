from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from models.MessagePayload import MessagePayload

class ConversationPayload(BaseModel):
    id: Optional[str] = Field(default=None, description="Unique identifier for the conversation.")
    started: Optional[float] = Field(default=None, description="Timestamp when the conversation started.")
    userId: Optional[str] = Field(default=None, description="Unique identifier of the user holding the conversation.")
    agentId: Optional[str] = Field(default=None, description="Unique identifier of the agent of the conversation.")
    messages: Optional[List[MessagePayload]] = Field(default=None, description="List of messages in the conversation.")
    additionalProperties: Optional[Dict[Any, Any]] = Field(default=None)
