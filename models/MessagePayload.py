class MessagePayload: 
  def __init__(self, input):
    if hasattr(input, 'id'):
    	self._id = input.id
    if hasattr(input, 'timestamp'):
    	self._timestamp = input.timestamp
    if hasattr(input, 'userId'):
    	self._userId = input.userId
    if hasattr(input, 'message'):
    	self._message = input.message
    if hasattr(input, 'agentId'):
    	self._agentId = input.agentId
    if hasattr(input, 'language'):
    	self._language = input.language
    if hasattr(input, 'destination'):
    	self._destination = input.destination
    if hasattr(input, 'destinationParams'):
    	self._destinationParams = input.destinationParams
    if hasattr(input, 'targetFormat'):
    	self._targetFormat = input.targetFormat
    if hasattr(input, 'author'):
    	self._author = input.author
    if hasattr(input, 'additionalProperties'):
    	self._additionalProperties = input.additionalProperties

  @property
  def id(self):
  	return self._id
  @id.setter
  def id(self, id):
  	self._id = id

  @property
  def timestamp(self):
  	return self._timestamp
  @timestamp.setter
  def timestamp(self, timestamp):
  	self._timestamp = timestamp

  @property
  def userId(self):
  	return self._userId
  @userId.setter
  def userId(self, userId):
  	self._userId = userId

  @property
  def message(self):
  	return self._message
  @message.setter
  def message(self, message):
  	self._message = message

  @property
  def agentId(self):
  	return self._agentId
  @agentId.setter
  def agentId(self, agentId):
  	self._agentId = agentId

  @property
  def language(self):
  	return self._language
  @language.setter
  def language(self, language):
  	self._language = language

  @property
  def destination(self):
  	return self._destination
  @destination.setter
  def destination(self, destination):
  	self._destination = destination

  @property
  def destinationParams(self):
  	return self._destinationParams
  @destinationParams.setter
  def destinationParams(self, destinationParams):
  	self._destinationParams = destinationParams

  @property
  def targetFormat(self):
  	return self._targetFormat
  @targetFormat.setter
  def targetFormat(self, targetFormat):
  	self._targetFormat = targetFormat

  @property
  def author(self):
  	return self._author
  @author.setter
  def author(self, author):
  	self._author = author

  @property
  def additionalProperties(self):
  	return self._additionalProperties
  @additionalProperties.setter
  def additionalProperties(self, additionalProperties):
  	self._additionalProperties = additionalProperties
