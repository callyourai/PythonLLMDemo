class ConversationPayload: 
  def __init__(self, input):
    if hasattr(input, 'id'):
    	self._id = input.id
    if hasattr(input, 'started'):
    	self._started = input.started
    if hasattr(input, 'userId'):
    	self._userId = input.userId
    if hasattr(input, 'agentId'):
    	self._agentId = input.agentId
    if hasattr(input, 'messages'):
    	self._messages = input.messages
    if hasattr(input, 'additionalProperties'):
    	self._additionalProperties = input.additionalProperties

  @property
  def id(self):
  	return self._id
  @id.setter
  def id(self, id):
  	self._id = id

  @property
  def started(self):
  	return self._started
  @started.setter
  def started(self, started):
  	self._started = started

  @property
  def userId(self):
  	return self._userId
  @userId.setter
  def userId(self, userId):
  	self._userId = userId

  @property
  def agentId(self):
  	return self._agentId
  @agentId.setter
  def agentId(self, agentId):
  	self._agentId = agentId

  @property
  def messages(self):
  	return self._messages
  @messages.setter
  def messages(self, messages):
  	self._messages = messages

  @property
  def additionalProperties(self):
  	return self._additionalProperties
  @additionalProperties.setter
  def additionalProperties(self, additionalProperties):
  	self._additionalProperties = additionalProperties
