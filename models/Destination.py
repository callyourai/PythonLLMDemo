from pydantic import BaseModel, Field
from enum import Enum 
class Destination(Enum): 
  CHAT = "Chat"
  CALL = "Call"
  VIDEO = "Video"
  OTHER = "Other"