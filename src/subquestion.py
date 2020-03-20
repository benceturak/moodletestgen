import xml.etree.ElementTree as ET
from name import Name
from unitgradingtype import Unitgradingtype
from unitpenalty import Unitpenalty
from showunits import Showunits
from unitsleft import Unitsleft
from text import Text

class Subquestion(ET.Element):

    def __init__(self, question, answer):
        super(Subquestion, self).__init__('subquestion')

        self.set('format', 'html')
        self.append(Text(question))
        self.append(answer)



    def set_unitgradingtype(self,text):
        self.append(Unitgradingtype(text))

    def set_unitpenalty(self,text):
        self.append(Unitpenalty(text))

    def set_showunits(self,text):
        self.append(Showunits(text))

    def set_unitsleft(self,text):
        self.append(Unitsleft(text))
