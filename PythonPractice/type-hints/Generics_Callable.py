from typing import TypeVar, Generic, Callable

T = TypeVar("T")


class Container(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value


def execute_function(func: Callable[[int], str], value: int) -> str:
    return func(value)


def number_to_text(num: int) -> str:
    return f"The number is {num}"


print(execute_function(number_to_text, 10))
