def my_func():
    x = 10  # Local scope
    print(x)

def outer():
    x = "enclosing"
    def inner():
        print(x)  # Accesses the enclosing scope
    inner()


x = "global"
def my_func():
    print(x)  # Accesses global scope


print(len("Python"))  # `len` comes from built-in scope

