import pytest
from PythonTraining.Unit_Testing.survey  import AnonymousSurvey
# It leads you toward explicit dependency declarations that are still reusable thanks to the availability of fixtures.
# pytest fixtures are functions that can create data, test doubles, or initialize system state for the test suite.
# Any test that wants to use a fixture must explicitly use this fixture function as an
#argument to the test function, so dependencies are always stated up front:
@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Hindi','French']
    for response in responses:
         language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
