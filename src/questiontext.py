import xml.etree.ElementTree as ET

from text import Text

class Questiontext(ET.Element):

    def __init__(self, text):
        super(Questiontext, self).__init__('questiontext')

        self.set('format', 'html')

        self.append(Text(text))#CDATA!!!!
