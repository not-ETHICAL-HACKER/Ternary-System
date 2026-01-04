# Ternary > Binary

This repository explores the implementation of ternary number systems in software, with the long-term goal of informing potential hardware designs.

This project does **not** claim that modern ternary systems are inherently superior to binary systems in practice.  
Instead, it investigates the **theoretical limits of information representation and compression**, motivated by the fact that the most efficient radix in information theory is the irrational base *e*.  
Since base *e* is not physically realizable, base-3 (ternary) is the most efficient practical integer approximation.

## Binary

Computers all over the world use the binary system.
in the binary system the computer uses `0` and `1` as truth values

-`0` represents the `off` state of electrical appliances,
-`1` represents the `on` state of electrical appliances.

This system really stuck with the world because of its simplicity and its cheap cost implementation in hardware

## Ternary

Soviets used the `ternary` system for their computers.

These computers were more efficient in processing data than their `binary` counterparts and often outperformed bitwise computers.  
This is because the soviets used the `balanced ternary` system.  
The components of the `balanced ternary` system.

- `+1`
- `0`
- `-1`

## Theory

1 **Trit** stores log₂(3) ≈ 1.585 bits of information while 1 **Bit** log₂(2) = 1 bit of information.

So ,in theory ternary system is more efficient in storing information.
A single **trit** has three possible states, whereas a **bit** has two.

In information-theoretic terms:

- 1 bit stores 1 bit of information
- 1 trit stores log₂(3) ≈ 1.585 bits of information

This makes ternary systems theoretically more information-dense than binary,
and base-3 is mathematically optimal among integer bases.

## Design Decisions

This project intentionally takes several liberties for experimentation and clarity.

A **chomp** is defined as **9 balanced ternary digits (trits)**, forming a fixed-width ternary word:

- 9 trits = \(3^9 = 19,683\) representable states as opposed to the 256 representable states of 1 Byte
- structured as three 3-trit groups
- conceptually analogous to the 8-bit byte in binary systems

A **chip** is defined as **3 balanced ternary digits (trits)**, forming a fixed-width ternary word:

- 3 trits = \(3^3 = 27\) representable states as opposed to the 16 representable states of 1 Nibble
- structured as three 3-trit groups
- conceptually analogous to the 4-bit Nibble in binary systems

The term *chomp* and *chip* is a project-specific abstraction and is not a proposed standard.

## Documentation

- [Logical Operations](docs/Logical-Operations.md)
- [Progenitor](docs/Progenitor.md)
