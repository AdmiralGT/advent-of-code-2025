from day3 import calculate_largest_joltage, calculate_largest_2digit_joltage

# def test_calculate_largest_2digit_joltage():
#     assert calculate_largest_2digit_joltage("123456789") == 89
#     assert calculate_largest_2digit_joltage("987654321") == 98
#     assert calculate_largest_2digit_joltage("135792468") == 98
#     assert calculate_largest_2digit_joltage("246813579") == 89
#     assert calculate_largest_2digit_joltage("111222333") == 33
#     assert calculate_largest_2digit_joltage("999888777") == 99

def test_calculate_largest_joltage():
    assert calculate_largest_joltage("987654321111111") == 987654321111
    assert calculate_largest_joltage("811111111111119") == 811111111119
    assert calculate_largest_joltage("234234234234278") == 434234234278
    assert calculate_largest_joltage("818181911112111") == 888911112111
