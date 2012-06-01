class AbstractGenerator(object):
      def __init__(self, generator_name):
        self.generator_name = generator_name
      
        
class RandomDataGenerator(AbstractConnector):
      def __init__(self, generator_name):
        super(RandomDataGenerator, self).__init__(generator_name)
