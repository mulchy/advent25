from sys import stdin
from typing import Iterable


def parse(input: str):
    for line in input.split(","):
        start, end = line.split("-")
        yield int(start), int(end)


# this gives them backwards, but doesn't matter for this problem
def digits(n: int):
    while n > 0:
        n, d = divmod(n, 10)
        yield d


def is_single_repeat(n: int):
    ds = list(digits(n))
    length = len(ds)
    if length % 2 != 0:
        return False

    half = length // 2

    return ds[0:half] == ds[half:]


def is_repeated_block(n: int):
    ds = list(digits(n))
    length = len(ds)

    for chunk_size in range(1, length):
        if length % chunk_size != 0:
            continue

        first_chunk = ds[:chunk_size]

        start = chunk_size
        stop = length
        step = chunk_size

        chunks = (ds[i : i + chunk_size] for i in range(start, stop, step))

        if all(first_chunk == next_chunk for next_chunk in chunks):
            return True

    return False


def is_single_repeat_in_ranges(ranges: Iterable[tuple[int, int]]):
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_single_repeat(n):
                yield n


def is_repeated_block_in_ranges(ranges: Iterable[tuple[int, int]]):
    for start, end in ranges:
        for n in range(start, end + 1):
            if is_repeated_block(n):
                yield n


def solve(input: str):
    ranges = list(parse(input))
    part1 = sum(is_single_repeat_in_ranges(ranges))
    part2 = sum(is_repeated_block_in_ranges(ranges))
    return f"{part1}\n{part2}"


def main():
    print(solve(stdin.read()))


if __name__ == "__main__":
    main()
