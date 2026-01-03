def align(a: str, b: str) -> tuple[str, str]:
    while len(a) != len(b):
        if len(a) > len(b):
            b = "0" + b
        elif len(a) < len(b):
            a = "0" + a
        else:
            return a, b
    return a, b


class Ternary(str):
    def __init__(self, num: int) -> None:
        self.num: int = num
        self.pos = "+"
        self.trits: dict[int, str] = {-1: "-", 0: "0", 1: "+"}
        self.OR = {
    ('+', '+'): '+', ('+', '0'): '+', ('+', '-'): '0',
    ('0', '+'): '+', ('0', '0'): '0', ('0', '-'): '-',
    ('-', '+'): '0', ('-', '0'): '-', ('-', '-'): '-',
}

    def __repr__(self) -> str:
        return self.trits[self.num]

    def Convert(self) -> str:
        final = "0t"
        n = self.num
        if n == 0:
            return "0"
        while n != 0:
            r = n % 3
            n = n // 3

            if r == 2:
                r = -1
                n = n + 1

            final += self.trits[r]
        return final[::-1]


class ternary(Ternary):
    def convert(self) -> Ternary | str:
        self.ternary = Ternary(self.num).Convert()
        return self.ternary

    def __or__(self, other: Ternary | int) -> Ternary:
        a = self.ternary
        b = Ternary(other).Convert()
        a, b = align(a=a, b=b)
        a = [sign*3**i for i, sign in enumerate(a[::-1])]
        b = [sign*3**i for i, sign in enumerate(b[::-1])]

    def T_OR(self, other: str) -> Ternary | str:
        other = other[2:]
        self.ternary = self.ternary[2:]
        return max(other, self.ternary)


print(ternary(50).convert())
