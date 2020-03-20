import xml.etree.ElementTree as ET
from name import Name
from unitgradingtype import Unitgradingtype
from unitpenalty import Unitpenalty
from showunits import Showunits
from unitsleft import Unitsleft

class Quiz(ET.Element):

    def __init__(self):
        super(Quiz, self).__init__('quiz')

    def add_question(self, question):
        self.append(question)
