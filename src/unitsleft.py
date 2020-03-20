import xml.etree.ElementTree as ET

class Unitsleft(ET.Element):

    def __init__(self, text):
        super(Unitsleft, self).__init__('unitsleft')

        self.text = text
