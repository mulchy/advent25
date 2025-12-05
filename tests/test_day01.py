from advent.day01 import SpinHistory, parse, solve, spins, count_zeros

input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def test_parse():
    assert list(parse(input)) == [
        ("L", 68),
        ("L", 30),
        ("R", 48),
        ("L", 5),
        ("R", 60),
        ("L", 55),
        ("L", 1),
        ("L", 99),
        ("R", 14),
        ("L", 82),
    ]


def test_spins():
    assert (
        list(spins(parse(input)))
        == [
            SpinHistory(crossings=0, position=50),  # The dial starts by pointing at 50.
            SpinHistory(
                crossings=1, position=82
            ),  # The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
            SpinHistory(
                crossings=0, position=52
            ),  # The dial is rotated L30 to point at 52.
            SpinHistory(
                crossings=0, position=0
            ),  # The dial is rotated R48 to point at 0.
            SpinHistory(
                crossings=0, position=95
            ),  # The dial is rotated L5 to point at 95.
            SpinHistory(
                crossings=1, position=55
            ),  # The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
            SpinHistory(
                crossings=0, position=0
            ),  # The dial is rotated L55 to point at 0.
            SpinHistory(
                crossings=0, position=99
            ),  # The dial is rotated L1 to point at 99.
            SpinHistory(
                crossings=0, position=0
            ),  # The dial is rotated L99 to point at 0.
            SpinHistory(
                crossings=0, position=14
            ),  # The dial is rotated R14 to point at 14.
            SpinHistory(
                crossings=1, position=32
            ),  # The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
        ]
    )


def test_count_zeros():
    assert count_zeros(spins(parse(input))) == 3


def test_solve():
    assert solve(input) == "3\n6"
