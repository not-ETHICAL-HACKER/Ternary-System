from typing import Any
# def align(a: str, b: str) -> tuple[str, str]:
#     while len(a) != len(b):
#         if len(a) > len(b):
#             b = "0" + b
#         elif len(a) < len(b):
#             a = "0" + a
#         else:
#             return a, b
#     return a, b


# class Ternary(str):
#     def __init__(self, num: int) -> None:
#         self.num: int = num
#         self.pos = "+"
#         self.trits: dict[int, str] = {-1: "-", 0: "0", 1: "+"}
#         self.OR = {
#     ('+', '+'): '+', ('+', '0'): '+', ('+', '-'): '0',
#     ('0', '+'): '+', ('0', '0'): '0', ('0', '-'): '-',
#     ('-', '+'): '0', ('-', '0'): '-', ('-', '-'): '-',
# }

#     def __repr__(self) -> str:
#         return self.trits[self.num]

#     def Convert(self) -> str:
#         final = "0t"
#         n = self.num
#         if n == 0:
#             return "0"
#         while n != 0:
#             r = n % 3
#             n = n // 3

#             if r == 2:
#                 r = -1
#                 n = n + 1

#             final += self.trits[r]
#         return final[::-1]


# class ternary(Ternary):
#     def __init__(self,t_num:str):
#         self.t_num = t_num
#     def convert(self) -> str:
#         self.ternary = Ternary(self.num).Convert()
#         return self.ternary

#     def T_OR(self, other: str) -> str:
#         a,b=align(self.t_num,other)
#         a = "".join(self.OR[(x, y)] for x, y in zip(a, b))
#         print(a)
#         return a

# print(ternary(ternary(50).convert()).T_OR("++----"))
#! Commented out bcs i implemented ternary horiibly and looking for better ideas but not deletin for structureb

def func_wrapper(func: Any) -> Any:
    def inner(*args: Any, **kwargs: Any) -> Any:
        print("Calling", func.__name__, end=" -> ")
        result = func(*args, **kwargs)
        return result
    return inner


@func_wrapper
def align(a: str, b: str) -> tuple[str, str]:
    length = max(len(a), len(b))
    return a.zfill(length), b.zfill(length)


ORDER = {"-": -1, "0": 0, "+": 1}
REVERSE = {-1: "-", 0: "0", 1: "+"}


class Ternary:
    ORDER = {"-": -1, "0": 0, "+": 1}
    REVERSE = {-1: "-", 0: "0", 1: "+"}

    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value

    @func_wrapper
    def t_or(self, T1: str, T2: str) -> str:
        a, b = align(T1, T2)
        result = ""
        for x, y in zip(a, b):
            result += REVERSE[max(ORDER[x], ORDER[y])]
        return result

    @func_wrapper
    def t_and(self, T1: str, T2: str) -> str:
        a, b = align(T1, T2)
        result = ""
        for x, y in zip(a, b):
            result += REVERSE[min(ORDER[x], ORDER[y])]
        return result

    @func_wrapper
    def t_not(self, T: str) -> str:
        mapping = {"+": "-", "-": "+", "0": "0"}
        return "".join(mapping[i] for i in T)

    @func_wrapper
    def t_nor(self, T1: str, T2: str) -> str:
        return self.t_not(self.t_or(T1, T2))

    @func_wrapper
    def t_nand(self, T1: str, T2: str) -> str:
        return self.t_not(self.t_and(T1, T2))

    @func_wrapper
    def inc(self, T: str) -> str:
        Val = [ORDER[x] for x in T]
        fin = [((Val[i]+2) % 3)-1 for i in range(len(Val))]
        return "".join(REVERSE[x] for x in fin)

    @func_wrapper
    def dec(self, T: str) -> str:
        Val = [ORDER[x] for x in T]
        fin = [((Val[i]) % 3)-1 for i in range(len(Val))]
        return "".join(REVERSE[x] for x in fin)

    @func_wrapper
    def full_add_trit(self, a: int, b: int, cin: int):
        s = a + b + cin

        if s > 1:
            return s - 3, 1
        elif s < -1:
            return s + 3, -1
        else:
            return s, 0

    @func_wrapper
    def t_add(self, T1: str, T2: str) -> str:
        a, b = align(T1, T2)
        V1 = [ORDER[x] for x in a]
        V2 = [ORDER[x] for x in b]

        carry = 0
        result: list[str] = []

        for i in reversed(range(len(V1))):
            s, carry = self.full_add_trit(V1[i], V2[i], carry)
            result.append(REVERSE[s])

        if carry:
            result.append(REVERSE[carry])

        return "".join(reversed(result))

    @func_wrapper
    def COR(self, T1: str, T2: str) -> str:
        a, b = align(T1, T2)
        result = ""
        for x, y in zip(a, b):
            if x == y:
                result += "0"
            else:
                result += REVERSE[ORDER[x] - ORDER[y]]
        return result

    @func_wrapper
    def Convert(self, num: int) -> str:
        final: str = ""
        n = num
        if n == 0:
            return "0"
        while n != 0:
            r = n % 3
            n = n // 3

            if r == 2:
                r = -1
                n = n + 1

            final += REVERSE[r]
        return final[::-1]


T = Ternary("+")
# Example usage:
print(T.t_or("++0--", "0+---"))
print(T.t_and("++0--", "0+---"))
print(T.t_not("++0--"))
print(T.t_nor("++0--", "0+---"))
print(T.t_nand("++0--", "0+---"))
print(T.inc("++0--"))
print(T.dec("++0--"))
print(T.t_add("++0--", "0+---"))
print(T.COR("++0--", "0+---"))
print(T.Convert(80))
