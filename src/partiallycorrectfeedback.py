import xml.etree.ElementTree as ET

class Partiallycorrectfeedback(ET.Element):
    '''Partiallycorrectfeedback class for moodle questions answer

    '''

    def __init__(self, text):
        super(Partiallycorrectfeedback, self).__init__('partiallycorrectfeedback')

        self.text = text
