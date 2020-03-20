import xml.etree.ElementTree as ET

class Tolerance(ET.Element):

    def __init__(self, text):
        super(Tolerance, self).__init__('tolerance')

        self.text = text
