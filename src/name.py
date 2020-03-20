import xml.etree.ElementTree as ET
from text import Text

class Name(ET.Element):

    def __init__(self, name):
        super(Name, self).__init__('name')

        self.append(Text(name))
