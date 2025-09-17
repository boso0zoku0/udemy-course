def hinames(qq: str, /, *, name: str, age: int):
    print(f'Name: {name}, Age: {age}')
    

hinames("2", name="2", age=21)


def three_func():
    return one_func(), two_func()
three_func()

def one_func():
    print(f'one')


def two_func():
    print(f'two')

print(three_func())