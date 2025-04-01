def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


def name_tester(type_test,*names):
    print(f"\nWe will do {type_test} testing with following testers:")
    for name in names:
        print(f"-{name}")

