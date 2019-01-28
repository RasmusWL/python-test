# pylint: disable=missing-docstring,invalid-name,too-few-public-methods,blacklisted-name


class Foo():

    def meth(self, a: str, b: int) -> str:
        'hello' + a*b


if __name__ == "__main__":
    foo = Foo()
    print(foo.meth('a', 2))
