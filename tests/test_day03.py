from advent.day03 import max_joltage, twelve_jolts


def test_max_joltage():
    assert 98 == max_joltage("987654321111111")
    assert 89 == max_joltage("811111111111119")
    assert 78 == max_joltage("234234234234278")
    assert 92 == max_joltage("818181911112111")


def test_twelve_jolts():
    assert 987654321111 == twelve_jolts("987654321111111")
    assert 811111111119 == twelve_jolts("811111111111119")
    assert 434234234278 == twelve_jolts("234234234234278")
    assert 888911112111 == twelve_jolts("818181911112111")
