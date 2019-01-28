# pylint: disable=missing-docstring,invalid-name,too-few-public-methods,blacklisted-name


class Foo():

    def __init__(self, hello='hello'):
        self.hello = hello

    def meth(self, a: str, b: int) -> str:
        return self.hello + a*b


class Bar(Foo):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bar = 0

    def meth(self, a: str, b: int) -> str:
        self.bar += 1
        super().meth(a, b)


if __name__ == "__main__":
    foo = Bar()
    print(foo.meth('a', 2))
