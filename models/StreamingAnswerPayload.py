from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from models.Language import Language
from models.Destination import Destination
from models.DestinationParams import DestinationParams
from models.TargetFormat import TargetFormat
from models.MessageAuthor import MessageAuthor

class StreamingAnswerPayload(BaseModel): 
  id: Optional[str] = Field(alias='''Unique identifier for the message.''', default=None)
  timestamp: Optional[float] = Field(alias='''Timestamp of the message.''', default=None)
  userId: Optional[str] = Field(alias='''Unique identifier for the user.''', default=None)
  message: Optional[str] = Field(alias='''Content of the message.''', default=None)
  agentId: Optional[str] = Field(alias='''Unique identifier for the agent.''', default=None)
  language: Optional[Language] = Field(default=None)
  destination: Optional[Destination] = Field(alias='''Where the answer shall be sent to.''', default=None)
  destinationParams: Optional[DestinationParams] = Field(default=None)
  targetFormat: Optional[TargetFormat] = Field(alias='''Target format of the message content.''', default=None)
  author: Optional[MessageAuthor] = Field(alias='''Who created the message.''', default=None)
  completed: Optional[bool] = Field(alias='''Flag to indicate if the streaming is completed.''', default=None)
  additionalProperties: Optional[dict[Any, Any]] = Field(default=None)
