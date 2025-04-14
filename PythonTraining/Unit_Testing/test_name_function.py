# it must start with test_.
# When we ask pytest to run the tests we’ve written,
# it will look for any file that begins with test_,
# and run all the tests it finds in that file.

from PythonTraining.Unit_Testing.name_function import get_formatted_name

def test_first_last_name():
     formatted_name = get_formatted_name('frank', 'erkel')
     assert formatted_name == 'Frank Erkel'


def test_first_last_middle_name():
     formatted_name = get_formatted_name(
        'frank', 'qamozart', 'erkel')
     assert formatted_name == 'Frank Qamozart Erkel' # Find the Bug







