import json

import sys
sys.path.append('../src')
import gen_rand_input
from question import Question
from subquestion import Subquestion
from answer import Answer
from quiz import Quiz
import xml.etree.ElementTree as ET

with open('../example/matching_config.json') as file:
    config = json.load(file)

    quiz = Quiz()

    for i in range(0, config['number_of_questions']):

        question = Question(config['type'])
        question.set_name(config['name'])


        input = gen_rand_input.gen_rand_input(config['input_parameters'])
        print(input)
        question.set_questiontext(config['questiontext'].format(*input))

        for q in config['questions']:
            module = __import__(q['answer'])

            answer = Answer(eval('module.' + q['answer'] + '(input)'))

            subquestion = Subquestion(q['question'], answer)
            question.add_subquestion(subquestion)

        quiz.add_question(question)

    tree = ET.ElementTree(quiz)

    tree.write(config['output_file'], 'utf-8')
