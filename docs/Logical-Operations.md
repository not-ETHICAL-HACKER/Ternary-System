# Logical Operations

This file is context for the ternary system's logical operations

## Syntax

| Symbol | Meaning | Order |
|:------:|:-------:|:-----:|
| `+` | True | Highest |
| `0` | Neutral | Middle |
| `-` | False | Lowest |

## OR Operation

| Symbols | **+** | **0** | **-**  |
|:-------:|:-----:|:-----:|-------:|
| **+** | `+` | `+` | `+` |
| **0** | `+` | `0` | `0` |
| **-** | `+` | `0` | `-` |

> `OR(a,b) = max(a,b)`

## AND Operation

| Symbols | **+** | **0** | **-**  |
|:-------:|:-----:|:-----:|-------:|
| **+** | `+` | `0` | `-` |
| **0** | `0` | `0` | `-` |
| **-** | `-` | `-` | `-` |

> `AND(a,b) = min(a,b)`

## NOT Operation

|Symbols|Output|
|:-----:|:--------:|
|**+**|`-`|
|**0**|`0`|
|**-**|`+`|

> `NOT(a) = -a`
> `NOT(NOT(a)) = a`

## NOR Operation

| Symbols | **+** | **0** | **-**  |
|:-------:|:-----:|:-----:|-------:|
| **+** | `-` | `-` | `-` |
| **0** | `-` | `0` | `0` |
| **-** | `-` | `0` | `+` |

> `NOR(a,b) = -max(a,b)`

## NAND Operation

| Symbols | **+** | **0** | **-**  |
|:-------:|:-----:|:-----:|-------:|
| **+** | `-` | `0` | `+` |
| **0** | `0` | `0` | `+` |
| **-** | `+` | `+` | `+` |

> `NAND(a,b) = -min(a,b)`

## INC Operation

| Symbols | Output |
|:-------:|:-----:|
| **+** | `-` |
| **0** | `+` |
| **-** | `0` |

> `INC(a) = ((a + 2) % 3) - 1`

## DEC Operation

| Symbols | Output |
|:-------:|:-----:|
| **+** | `0` |
| **0** | `-` |
| **-** | `+` |

> `DEC(a) = ((a + 1) % 3) - 1`

## ADD Operation

| Symbols | **+** | **0** | **-**  |
|:-------:|:-----:|:-----:|-------:|
| **+** | `-` | `+` | `0` |
| **0** | `+` | `0` | `-` |
| **-** | `0` | `-` | `+` |

> `ADD(a,b) = (a + b) % 3`

## CAR Operation

| Symbols | **+** | **0** | **-**  |
|:-------:|:-----:|:-----:|-------:|
| **+** | `+` | `0` | `0` |
| **0** | `0` | `0` | `0` |
| **-** | `0` | `0` | `-` |

> `CARRY(a,b)` is + if `a + b > 1`, - if `a + b < -1`, and 0 otherwise.

## COR Operation

| Symbols | **+** | **0** | **-**  |
|:-------:|:-----:|:-----:|-------:|
| **+** | `0` | `+` | `+` |
| **0** | `-` | `0` | `+` |
| **-** | `-` | `-` | `0` |

> COR is a directional comparison operator.
> `Equal inputs` yield `0`.
> When `inputs differ`, the output indicates whether the row operand is greater (+)
> or less (-) than the column operand `under the ordering - < 0 < +`.
> This rule folows ROW - Column
> `COR(a,b) = sign(a - b)`
> `COR(a,b) = -COR(b,a)`
> COR =>> `Comparater Order Relation`