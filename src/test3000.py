# pylint: disable=missing-docstring,invalid-name,too-few-public-methods

from abc import ABC, abstractmethod


class Foo(ABC):

    @abstractmethod
    def meth(self, a: str, b: int) -> str:
        pass


class FooImpl(Foo):
    def meth(self, a: str, b: int) -> str:
        return 'hello' + a*b


class InstrumentedFoo(Foo):

    def __init__(self, foo: Foo):
        self._foo = foo
        self._counter = 0

    def meth(self, a: str, b: int) -> str:
        self._counter += 1
        self._foo.meth(a, b)
        print(f'DEBUG: called total {self._counter} times')


if __name__ == "__main__":
    my_foo = InstrumentedFoo(FooImpl())

    print(my_foo.meth('a', 2))
