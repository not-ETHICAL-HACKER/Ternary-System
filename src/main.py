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


def t_or(T1: str, T2: str) -> str:
    a, b = align(T1, T2)
    result = ""
    for x, y in zip(a, b):
        result += REVERSE[max(ORDER[x], ORDER[y])]
    return result


def t_and(T1: str, T2: str) -> str:
    a, b = align(T1, T2)
    result = ""
    for x, y in zip(a, b):
        result += REVERSE[min(ORDER[x], ORDER[y])]
    return result


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

def t_nor(T1: str, T2: str) -> str:
    return t_not(t_or(T1, T2))
def t_nand(T1: str, T2: str) -> str:
    return t_not(t_and(T1, T2))
def inc(T:str)->str:
    Val = [ORDER[x] for x in T]
    fin = [((Val[i]+2)%3)-1 for i in range(len(Val))]
    return "".join(REVERSE[x] for x in fin)
def dec(T:str)->str:
    Val = [ORDER[x] for x in T]
    fin = [((Val[i]-1)%3)-1 for i in range(len(Val))]
    return "".join(REVERSE[x] for x in fin)
def t_Add(T1:str,T2:str)->str:
    a,b=align(T1,T2)
    Val1 = [ORDER[x] for x in a]
    Val2 = [ORDER[x] for x in b]
    fin = [((Val1[i]+Val2[i])%3)-1 for i in range(len(Val1))]
    return "".join(REVERSE[x] for x in fin)
def CAR(T1:str,T2:str)->str:
    a,b=align(T1,T2)
    Val1 = [ORDER[x] for x in a]
    Val2 = [ORDER[x] for x in b]
    fin = [1 if (Val1[i]+Val2[i])>2 else 0 for i in range(len(Val1))]
    return "".join(REVERSE[x] for x in fin)
#def COR
# Example usage:

print(t_or("++0--", "0+---"))
print(t_and("++0--", "0+---"))
print(t_not("++0--"))
print(t_nor("++0--", "0+---"))
print(t_nand("++0--", "0+---"))
print(inc("++0--"))
print(dec("++0--"))
print(t_Add("++0--", "0+---"))
print(CAR("++0--", "0+---"))