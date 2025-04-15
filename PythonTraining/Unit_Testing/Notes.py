# When you write a function or a class, you can also write tests for that code.
# Testing proves that your code works as it’s supposed to in response to all the kinds of input
# it’s designed to receive.
# Test new code as you add it, to make sure your changes don’t break your program’s existing behavior.
# A third-party package is a library that’s developed outside the core Python language.

# Install Pytest on Pycharm
# https://www.jetbrains.com/help/pycharm/pytest.html (Instructions to install Pytest)
# PyCharm supports pytest, a fully functional testing framework.
#The following features are available:

#The dedicated test runner.
#Code completion for test subject and pytest fixtures.
#Code navigation.
#Detailed failing assert reports.
#Support for Python 2.7 and Python 3.5 and later.
#Multiprocessing test execution
#Python includes a tool called pip that’s used to install third-party packages.
# python -m pip install --upgrade pip
# python -m pip install --user pytest
# Meaning of -m = tells Python to locate the module specified by <module_name> in sys.path
# and run it as if it were a script — meaning, it executes the module's __main__ block if it has one.
# What do you do when a test fails? Assuming you’re checking the right conditions,
# a passing test means the function is behaving correctly and a failing test means
# there’s an error in the new code you wrote. So when a test fails, don’t change the test.
# If you do, your tests might pass, but any code that calls your function like the test does will suddenly stop working.
# Instead, fix the code that’s causing the test to fail.
# Examine the changes you just made to the function, and figure out how those changes broke the desired behavior.
# What is TDD: Test Driven Development - You write failing tests before development
# A unit test verifies that one specific aspect of a function’s behavior is correct.
# A test case is a collection of unit tests that together prove that a function
# behaves as it’s supposed to, within the full range of situations you expect
# it to handle.

#Home
"""11-1. City, Country: Write a function that accepts two parameters: a city name and a country name.
The function should return a single string of the form City, Country, such as Santiago, Chile.
Store the function in a module called city_functions.py, and
save this file in a new folder so pytest won’t try to run the tests we’ve already written.
Create a file called test_cities.py that tests the function you just wrote.
Write a function called test_city_country() to verify that calling your function with values such as 'santiago' and 'chile'
results in the correct string.
Run the test, and make sure test_city_country() passes. 11-2. Population:
Modify your function so it requires a third parameter, population.
It should now return a single string of the form City,
Country – population xxx, such as Santiago, Chile – population 5000000.
Run the test again, and make sure test_city_country() fails this time.
Modify the function so the population parameter is optional.
Run the test, and make sure test_city_country() passes again.
Write a second test called test_city_country_population()
that verifies you can call your function with the values 'santiago', 'chile', and 'population=5000000'.
Run the tests one more time, and make sure this new test passes.

 """








