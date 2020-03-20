import xml.etree.ElementTree as ET

class Showunits(ET.Element):

    def __init__(self, text):
        super(Showunits, self).__init__('showunits')

        self.text = text
