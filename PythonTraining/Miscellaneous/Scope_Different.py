def my_func():
    z = 10  # Local scope
    print(z)

def num_func():
    print(z)

def outer():
    x = "enclosing"
    def inner():
        print(x)  # Accesses the enclosing scope
    inner()


x = "global"
def my_func():
    print(x)  # Accesses global scope


print(len("Python"))  # `len` comes from built-in scope

