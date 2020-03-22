import xml.etree.ElementTree as ET

class Hidden(ET.Element):
    '''Hidden class for moodle questions penalty

    '''

    def __init__(self, text):
        super(Hidden, self).__init__('hidden')

        self.text = str(text)
