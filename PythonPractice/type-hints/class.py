class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name}"


p1 = Person("Fadel", 20)
message = p1.greet()
print(message)
