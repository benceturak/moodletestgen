import xml.etree.ElementTree as ET

class Shuffleanswers(ET.Element):
    '''Shuffleanswers class for moodle questions

    '''

    def __init__(self, text):
        super(Shuffleanswers, self).__init__('shuffleansers')

        self.text = str(text).lower()
