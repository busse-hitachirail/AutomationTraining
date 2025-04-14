#Assertion Claim
#assert a == b Assert that two values are equal.
#assert a != b Assert that two values are not equal.
#assert a Assert that a evaluates to True.
#assert not a Assert that a evaluates to False.
#Assert that an element is in a list.
#Assert that an element is not in a list.

class AnonymousSurvey:

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses =[]

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")








