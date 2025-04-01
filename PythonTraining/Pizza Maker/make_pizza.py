import pizza # Use this kind of import statement to import an entire module named module_name.py,
            # each function in the module is available.

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#When Python reads this file, the line import pizza tells Python to open the file pizza.py
# and copy all the functions from it into this program.

pizza.name_tester('alan')
pizza.name_tester('sasha','mike','tek')