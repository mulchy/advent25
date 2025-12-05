from sys import stdin


def includes(start: int, end: int, value: int):
    return value >= start and value <= end


def parse(input: str):
    left, right = input.split("-")
    return int(left), int(right)


def solve(input: str):
    one, two = input.split("\n\n")
    ranges = [parse(r) for r in one.splitlines()]
    puzzle = [int(line) for line in two.splitlines()]

    part1 = sum(
        1
        for ingredient in puzzle
        if any(includes(left, right, ingredient) for left, right in ranges)
    )

    # todo unions of intervals
    # [[0,2]] + [4,5] = [[0,2], [4,5]]         disjoint -> new interval
    # [[0,2], [4,5]] + [0, 1] = [[0,2], [4,5]] subset -> no change
    # [[0,2], [4,5]] + [1, 3] = [[0,3], [4,5]] partial overlap -> extend existing interval
    # [[0,3], [4,5]] + [2, 4] = [[0, 5]]       fills gap -> remove old intervals, replace
    # other cases?
    start = min(left for left, _ in ranges)
    end = max(right for _, right in ranges)

    part2 = end - start

    return f"{part1}\n{part2}"


def main():
    print(solve(stdin.read()))


if __name__ == "__main__":
    main()
