import xml.etree.ElementTree as ET
import sys
sys.path.append('../src')
from quiz import Quiz
from question import Question
from answer import Answer
from subquestion import Subquestion

quiz = Quiz()

q1 = Question('matching')

q1.set_name('A kérdés neve')

q1.set_questiontext('A kérédés szövege')

a1 = Answer('Ez egy válasz')
a2 = Answer('Ez egy válasz 1')
a3 = Answer('Ez egy válasz 2')
a4 = Answer('Ez egy válasz 3')

sq1 = Subquestion('Alkérdés 1', a1)
sq2 = Subquestion('Alkérdés 2', a2)
sq3 = Subquestion('Alkérdés 3', a3)
sq4 = Subquestion('Alkérdés 4', a4)


q1.add_subquestion(sq1)
q1.add_subquestion(sq2)
q1.add_subquestion(sq3)
q1.add_subquestion(sq4)

#q1.set_answer(a1)

quiz.add_question(q1)

tree = ET.ElementTree(quiz)

tree.write('../ppp.xml', 'utf-8')
