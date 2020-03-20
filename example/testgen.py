
import sys
sys.path.append('../src')


from quiz import Quiz
import xml.etree.ElementTree as ET

#open config file
with open(sys.argv[1]) as file:

    #new quiz object
    quiz = Quiz(file)


    #generate questions
    quiz.gen_questions()

    #write quoiz to file in moodle XML format
    quiz.write()
