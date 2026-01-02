class Ternary:
    def __init__(self, num: int) -> None:
        self.num: int = num
        self.pos = "+"
        self.trits: dict[int, str] = {-1: "-", 0: "0", 1: "+"}
    def __repr__(self)->str:
        return self.trits[self.num]
    def Convert(self)->str:
        final=""
        n=self.num
        if n == 0:
            return "0"
        while n!= 0:
            r = n % 3
            n = n // 3

            if r == 2:
                r = -1
                n = n + 1

            final+=self.trits[r]
        return final[::-1]

class ternary(Ternary):
    def convert(self) -> Ternary|str:
        return Ternary(self.num).Convert()


    def T_OR(self, other: Ternary) -> Ternary:
        pass


print(ternary(50).convert())