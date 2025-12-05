from sys import stdin

type Point = tuple[int, int]


def parse(input: str):
    return {
        (row, col): char
        for row, line in enumerate(input.splitlines())
        for col, char in enumerate(line)
    }


def neighborhood(index: Point, grid: dict[Point, str]):
    row, col = index
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            try:
                yield grid[(row + i, col + j)]
            except KeyError:
                pass


def valid(index: Point, grid: dict[Point, str]):
    if grid[index] != "@":
        return False
    return sum(1 for char in neighborhood(index, grid) if char == "@") < 4


def solve(input: str):
    cols = input.find("\n")
    rows = len(input) // cols
    g = parse(input)

    part1 = sum(
        1
        for row in range(rows)
        for col in range(cols)
        if valid((row, col), g)
    )  # fmt: skip

    found = [
            (row, col)
            for row in range(rows)
            for col in range(cols)
            if valid((row, col), g)
        ]  # fmt: skip

    count = 0

    while found:
        count += len(found)

        for index in found:
            g[index] = "."

        found = [
            (row, col)
            for row in range(rows)
            for col in range(cols)
            if valid((row, col), g)
        ]

    part2 = count
    return f"{part1}\n{part2}"


def main():
    print(solve(stdin.read()))


if __name__ == "__main__":
    main()
