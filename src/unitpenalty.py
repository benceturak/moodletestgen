import xml.etree.ElementTree as ET

class Unitpenalty(ET.Element):

    def __init__(self, text):
        super(Unitpenalty, self).__init__('unitpenalty')

        self.text = text
