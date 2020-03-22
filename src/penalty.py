import xml.etree.ElementTree as ET

class Penalty(ET.Element):
    '''Penalty class for moodle questions penalty

    '''

    def __init__(self, text):
        super(Penalty, self).__init__('Penalty')

        self.text = str(text)
