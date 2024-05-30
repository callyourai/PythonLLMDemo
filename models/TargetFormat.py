from pydantic import BaseModel, Field
from enum import Enum 

class TargetFormat(Enum): 
  TEXT = "Text"
  VIDEO = "Video"
  AUDIO = "Audio"
  AUDIO_STREAM = "AudioStream"
  OTHER = "Other"