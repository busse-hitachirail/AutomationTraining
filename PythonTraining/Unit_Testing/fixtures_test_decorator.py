import pytest # we have to import pytest as we are using a decorator defined in pytest
from PythonTraining.Unit_Testing.survey import AnonymousSurvey

"""A fixture in pytest is a reusable piece of setup code that runs before (and optionally after) your tests. 
It’s a way to prepare test context or dependencies, like:
Creating data
Opening files
Connecting to databases
Initializing objects
Mocking APIs
You define a fixture using the @pytest.fixture is called a decorator.
"""
@pytest.fixture
def language_survey():
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

# When a parameter in a test function matches the name of a function with the @pytest.fixture decorator,
# the fixture will be run automatically and the return value will be passed to the test function.


def test_store_single_response(language_survey):
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses

