from sys import stdin


def parse(input: str):
    return input.splitlines()


def max_joltage(bank: str):
    for i in range(9, 0, -1):
        found = bank.find(str(i))
        if found != -1:
            for j in range(9, 0, -1):
                next = bank.find(str(j), found + 1)
                if next != -1:
                    return int(str(i) + str(j))
    return 0


def biggest_digit_in_sub_sequence(s: str, remaining: int):
    for digit in range(9, 0, -1):
        if (i := s.find(str(digit), 0, len(s) - remaining)) != -1:
            return digit, s[i + 1 :]
    return -1, ""


def twelve_jolts(s: str):
    digits: list[int] = []
    for i in range(12, 0, -1):
        d, s = biggest_digit_in_sub_sequence(s, i - 1)
        digits.append(d)
    return int("".join(str(d) for d in digits))


def solve(input: str):
    lines = parse(input)
    part1 = sum(max_joltage(line) for line in lines)
    part2 = sum(twelve_jolts(line) for line in lines)
    return f"{part1}\n{part2}"


def main():
    print(solve(stdin.read()))


if __name__ == "__main__":
    main()
