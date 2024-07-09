import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """test for the class anonymoussurvey"""
    def test_store_single_response(self):
        """test that single response is stored properly"""
        question = "what language did you first lern to speak? "
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

if __name__ == '__main__':
    unittest.main()