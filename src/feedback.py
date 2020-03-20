import xml.etree.ElementTree as ET
from text import Text

class Feedback(ET.Element):

    def __init__(self, text):
        super(Feedback, self).__init__('feedback')

        self.append(Text(text))

        self.set('format', 'html')
