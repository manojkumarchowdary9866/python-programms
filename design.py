def decorator(arg):
    def inner():
        print("*"*20)
        arg()

        
        print("*"*20)
    return inner
@decorator
def add():
    print("am first texter")
add()

@decorator
def text():
    print("am second texter")
text()
