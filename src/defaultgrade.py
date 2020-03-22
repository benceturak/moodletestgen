import xml.etree.ElementTree as ET

class Defaultgrade(ET.Element):
    '''Defaultgrade class for moodle questions feedback

    '''

    def __init__(self, text):
        super(Defaultgrade, self).__init__('deafaultgrade')

        self.text = str(text)
