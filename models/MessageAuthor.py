from pydantic import BaseModel, Field
from enum import Enum 

class MessageAuthor(Enum): 
  USER = "User"
  AGENT = "Agent"
  OTHER = "Other"