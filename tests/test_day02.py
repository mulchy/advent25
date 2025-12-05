from advent.day02 import is_repeated_block, is_single_repeat, parse, solve


input = (
    "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
    "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
    "824824821-824824827,2121212118-2121212124"
)


def test_parse():
    assert list(parse(input)) == [
        (11, 22),
        (95, 115),
        (998, 1012),
        (1188511880, 1188511890),
        (222220, 222224),
        (1698522, 1698528),
        (446443, 446449),
        (38593856, 38593862),
        (565653, 565659),
        (824824821, 824824827),
        (2121212118, 2121212124),
    ]


def test_is_single_repeat():
    assert is_single_repeat(55)
    assert is_single_repeat(6464)
    assert is_single_repeat(123123)
    assert not is_single_repeat(111)
    assert not is_single_repeat(1112)


def test_is_repeated_block():
    assert is_repeated_block(55)
    assert is_repeated_block(6464)
    assert is_repeated_block(123123)
    assert is_repeated_block(123123123)
    assert is_repeated_block(12341234)
    assert is_repeated_block(1212121212)
    assert is_repeated_block(1111111)
    assert is_repeated_block(824824824)
    assert is_repeated_block(1188511885)
    assert not is_repeated_block(211111)
    assert not is_repeated_block(111211)
    assert not is_repeated_block(29518063)


def test_solve():
    assert solve(input) == "1227775554\n4174379265"
