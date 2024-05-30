from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from models.Language import Language
from models.Destination import Destination
from models.DestinationParams import DestinationParams
from models.TargetFormat import TargetFormat
from models.MessageAuthor import MessageAuthor

class MessagePayload(BaseModel):
    id: Optional[str] = Field(default=None, description="Unique identifier for the message.")
    timestamp: Optional[float] = Field(default=None, description="Timestamp of the message.")
    userId: Optional[str] = Field(default=None, description="Unique identifier for the user.")
    message: Optional[str] = Field(default=None, description="Content of the message.")
    agentId: Optional[str] = Field(default=None, description="Unique identifier for the agent.")
    language: Optional[Language] = Field(default=None)
    destination: Optional[Destination] = Field(default=None, description="Where the answer shall be sent to.")
    destinationParams: Optional[DestinationParams] = Field(default=None)
    targetFormat: Optional[TargetFormat] = Field(default=None, description="Target format of the message content.")
    author: Optional[MessageAuthor] = Field(default=None, description="Who created the message.")
    additionalProperties: Optional[Dict[Any, Any]] = Field(default=None)