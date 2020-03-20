import xml.etree.ElementTree as ET
from name import Name
from unitgradingtype import Unitgradingtype
from unitpenalty import Unitpenalty
from showunits import Showunits
from unitsleft import Unitsleft
from questiontext import  Questiontext

class Question(ET.Element):

    def __init__(self, type):
        super(Question, self).__init__('question')

        self.set_type(type)

        self.set_unitgradingtype('0')
        self.set_unitpenalty('0')
        self.set_showunits('3')
        self.set_unitsleft('0')

    def set_questiontext(self, text):
        self.append(Questiontext(text))

    def set_name(self, name):
        self.append(Name(name))

    def set_type(self,type):
        self.set('type', type)

    def set_unitgradingtype(self,text):
        self.append(Unitgradingtype(text))

    def set_unitpenalty(self,text):
        self.append(Unitpenalty(text))

    def set_showunits(self,text):
        self.append(Showunits(text))

    def set_unitsleft(self,text):
        self.append(Unitsleft(text))

    def set_answer(self, answer):
        self.append(answer)

    def add_subquestion(self, subquestion):
        self.append(subquestion)
