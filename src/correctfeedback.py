import xml.etree.ElementTree as ET

class Correctfeedback(ET.Element):
    '''Correctfeedback class for moodle questions answer

    '''

    def __init__(self, text):
        super(Correctfeedback, self).__init__('correctfeedback')

        self.text = text
