import xml.etree.ElementTree as ET
from text import Text
from tolerance import Tolerance
from feedback import Feedback

class Answer(ET.Element):

    def __init__(self, answer, fraction = 100):
        super(Answer, self).__init__('answer')

        self.set('format', 'moodle_auto_format')
        self.set_fraction(str(fraction))

        self.append(Text(answer))



    def set_fraction(self, fraction='100'):
        self.set('fraction', fraction)

    def set_tolerance(self, tolerance):
        self.append(Tolerance(tolerance))

    def set_feedback(self, feedback):
        self.append(Feedback(feedback))
