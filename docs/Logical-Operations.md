# Logical Operations

This file is context for the ternary system's logical operations

## Precedence

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

## AND Operation

| Symbols | **+** | **0** | **-**  |
|:-------:|:-----:|:-----:|-------:|
| **+** | `+` | `0` | `-` |
| **0** | `0` | `0` | `-` |
| **-** | `-` | `-` | `-` |

## NOT Operation

|Symbols|Output|
|:-----:|:--------:|
|**+**|`-`|
|**0**|`0`|
|**-**|`+`|

## NOR Operation

| Symbols | **+** | **0** | **-**  |
|:-------:|:-----:|:-----:|-------:|
| **+** | `-` | `-` | `-` |
| **0** | `-` | `0` | `0` |
| **-** | `-` | `0` | `+` |

## NAND Operation

| Symbols | **+** | **0** | **-**  |
|:-------:|:-----:|:-----:|-------:|
| **+** | `-` | `0` | `+` |
| **0** | `0` | `0` | `+` |
| **-** | `+` | `+` | `+` |

## XOR Operation

| Symbols | **+** | **0** | **-**  |
|:-------:|:-----:|:-----:|-------:|
| **+** | `0` | `-` | `-` |
| **0** | `-` | `0` | `-` |
| **-** | `+` | `+` | `0` |

> XOR is defined as a symmetric difference operator where equal inputs yield `0`,
> and unequal inputs yield a value biased toward disagreement.