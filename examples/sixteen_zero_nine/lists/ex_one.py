def hinames(qq: str, /, *, name: str, age: int) -> None:
    print(f"Name: {name}, Age: {age}")


hinames("2", name="2", age=21)


def three_func() -> None:
    return one_func() or two_func()


def one_func() -> None:
    print(f"one")


def two_func() -> None:
    print(f"two")


print(three_func())
