class Language: 
  def __init__(self, input):
    if hasattr(input, 'locale'):
    	self._locale = input.locale
    if hasattr(input, 'probability'):
    	self._probability = input.probability
    if hasattr(input, 'additionalProperties'):
    	self._additionalProperties = input.additionalProperties

  @property
  def locale(self):
  	return self._locale
  @locale.setter
  def locale(self, locale):
  	self._locale = locale

  @property
  def probability(self):
  	return self._probability
  @probability.setter
  def probability(self, probability):
  	self._probability = probability

  @property
  def additionalProperties(self):
  	return self._additionalProperties
  @additionalProperties.setter
  def additionalProperties(self, additionalProperties):
  	self._additionalProperties = additionalProperties
