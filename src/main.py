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
    def __init__(self,t_num:str):
        self.t_num = t_num
    def convert(self) -> str:
        self.ternary = Ternary(self.num).Convert()
        return self.ternary

    def T_OR(self, other: str) -> str:
        a,b=align(self.t_num,other)
        a = "".join(self.OR[(x, y)] for x, y in zip(a, b))
        print(a)
        return a

print(ternary(ternary(50).convert()).T_OR("++----"))
