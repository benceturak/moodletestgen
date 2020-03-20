import xml.etree.ElementTree as ET

class Text(ET.Element):

    def __init__(self, text):
        super(Text, self).__init__('text')

        self.text = str(text)
