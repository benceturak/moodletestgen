import xml.etree.ElementTree as ET

class Incorrectfeedback(ET.Element):
    '''Incorrectfeedback class for moodle questions answer

    '''

    def __init__(self, text):
        super(Incorrectfeedback, self).__init__('incorrectfeedback')

        self.text = text
