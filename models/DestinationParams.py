class DestinationParams: 
  def __init__(self, input):
    if hasattr(input, 'strings'):
    	self._strings = input.strings
    if hasattr(input, 'additionalProperties'):
    	self._additionalProperties = input.additionalProperties

  @property
  def strings(self):
  	return self._strings
  @strings.setter
  def strings(self, strings):
  	self._strings = strings

  @property
  def additionalProperties(self):
  	return self._additionalProperties
  @additionalProperties.setter
  def additionalProperties(self, additionalProperties):
  	self._additionalProperties = additionalProperties
