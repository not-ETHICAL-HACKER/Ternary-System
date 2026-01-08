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
#! Commented out bcs i implemented ternary horiibly and looking for better ideas but not deletin for structure
def Wrapper(func:Any)->Any:
    def inner(*args:Any, **kwargs:Any)->Any:
        print("Calling", func.__name__,end=" -> ")
        result = func(*args, **kwargs)
        return result
    return inner

@Wrapper
def align(a: str, b: str) -> tuple[str, str]:
    while len(a) != len(b):
        if len(a) > len(b):
            b = "0" + b
        elif len(a) < len(b):
            a = "0" + a
        else:
            return a, b
    return a, b


ORDER = {"-": -1, "0": 0, "+": 1}
REVERSE = {-1: "-", 0: "0", 1: "+"}

@Wrapper
def t_or(T1: str, T2: str) -> str:
    a, b = align(T1, T2)
    result = ""
    for x, y in zip(a, b):
        result += REVERSE[max(ORDER[x], ORDER[y])]
    return result

@Wrapper
def t_and(T1: str, T2: str) -> str:
    a, b = align(T1, T2)
    result = ""
    for x, y in zip(a, b):
        result += REVERSE[min(ORDER[x], ORDER[y])]
    return result

@Wrapper
def t_not(T: str) -> str:
    result = ""
    for i in T:
        if i == "+":
            result += "-"
        elif i == "-":
            result += "+"
        else:
            result += "0"
    return result

@Wrapper
def t_nor(T1: str, T2: str) -> str:
    return t_not(t_or(T1, T2))

@Wrapper
def t_nand(T1: str, T2: str) -> str:
    return t_not(t_and(T1, T2))

@Wrapper
def inc(T: str) -> str:
    Val = [ORDER[x] for x in T]
    fin = [((Val[i]+2) % 3)-1 for i in range(len(Val))]
    return "".join(REVERSE[x] for x in fin)

@Wrapper
def dec(T: str) -> str:
    Val = [ORDER[x] for x in T]
    fin = [((Val[i]) % 3)-1 for i in range(len(Val))]
    return "".join(REVERSE[x] for x in fin)

@Wrapper
def full_add_trit(a: int, b: int, cin: int):
    s = a + b + cin

    if s > 1:
        return s - 3, 1
    elif s < -1:
        return s + 3, -1
    else:
        return s, 0

@Wrapper
def t_add(T1: str, T2: str) -> str:
    a, b = align(T1, T2)
    V1 = [ORDER[x] for x in a]
    V2 = [ORDER[x] for x in b]

    carry = 0
    result:list[str] = []

    for i in reversed(range(len(V1))):
        s, carry = full_add_trit(V1[i], V2[i], carry)
        result.append(REVERSE[s])

    if carry:
        result.append(REVERSE[carry])

    return "".join(reversed(result))

@Wrapper
def COR(T1: str, T2: str) -> str:
    a, b = align(T1, T2)
    result = ""
    for x, y in zip(a, b):
        if x == y:
            result += "0"
        else:
            result += REVERSE[ORDER[x] - ORDER[y]]
    return result
# Example usage:
print(t_or("++0--", "0+---"))
print(t_and("++0--", "0+---"))
print(t_not("++0--"))
print(t_nor("++0--", "0+---"))
print(t_nand("++0--", "0+---"))
print(inc("++0--"))
print(dec("++0--"))
print(t_add("++0--", "0+---"))
print(COR("++0--", "0+---"))

