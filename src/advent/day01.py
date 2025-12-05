from sys import stdin
from dataclasses import dataclass
from typing import Iterable


@dataclass
class SpinHistory:
    crossings: int
    position: int


def parse(input: str):
    for word in input.splitlines():
        yield (word[0], int(word[1:]))


def spins(input: Iterable[tuple[str, int]]):
    position = 50
    crossings = 0
    yield SpinHistory(crossings, position)

    for direction, magnitude in input:
        revolutions, delta = divmod(magnitude, 100)
        crossings = abs(revolutions)
        if direction == "L":
            crossings += 1 if position != 0 and delta > position else 0
            position = (position - delta) % 100
        if direction == "R":
            crossings += 1 if position != 0 and delta > (100 - position) else 0
            position = (position + delta) % 100

        yield SpinHistory(crossings, position)


def count_zeros(input: Iterable[SpinHistory]):
    return sum(1 for h in input if h.position == 0)


def count_crossings(input: Iterable[SpinHistory]):
    count = 0
    for h in input:
        if h.position == 0:
            count += 1
        count += h.crossings
    return count


def solve(input: str):
    history = list(spins(parse(input)))
    part1 = count_zeros(history)
    part2 = count_crossings(history)
    return f"{part1}\n{part2}"


def main():
    print(solve(stdin.read()))


if __name__ == "__main__":
    main()
