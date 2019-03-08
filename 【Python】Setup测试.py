
class AnonymousSurvey():

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print('\t' + '-' + response)

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = "What language did you first learn?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

        def test_single_response(self):
            self.my_survey.store_response(self.responses[0])
            self.assertIN(self.responses[0], self.my_survey.responses)

        def test_three_responses(self):

            for response in self.responses:
                self.my_survey.store_response(response)

            for response in self.responses:
                self.assertIn(response, self.my_survey.responses)


unittest.main()
