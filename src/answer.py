import xml.etree.ElementTree as ET
from text import Text
from tolerance import Tolerance
from feedback import Feedback

class Answer(ET.Element):
    '''Answer class for moodle questions answer
        :param answer: answer of question (str)
        :param fraction: facttion of questions grade (int) (percent)
    '''

    def __init__(self, answer, fraction = 100, tolerance = 0.001):
        super(Answer, self).__init__('answer')

        self.set('format', 'moodle_auto_format')
        self.set_fraction(str(fraction))
        self.set_tolerance(str(tolerance))

        self.append(Text(answer))



    def set_fraction(self, fraction='100'):
        self.set('fraction', fraction)

    def set_tolerance(self, tolerance):
        '''set answers tolerance
            :param tolerance: tolerance of answer
        '''
        self.append(Tolerance(tolerance))

    def set_feedback(self, feedback):
        '''set answers feedback
            :param feedback: feedback of answer (str)

        '''
        self.append(Feedback(feedback))
