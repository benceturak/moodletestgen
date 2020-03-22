import xml.etree.ElementTree as ET

class Generalfeedback(ET.Element):
    '''Generalfeedback class for moodle questions feedback

    '''

    def __init__(self, text):
        super(Generalfeedback, self).__init__('generalfeedback')

        self.text = text
