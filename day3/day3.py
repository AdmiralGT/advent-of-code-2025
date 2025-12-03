def calculate_largest_2digit_joltage(batteries):
    highest_first_digit = -1
    highest_first_digit_index = -1
    highest_last_digit = -1
    for i, char in enumerate(batteries[:-1]):
        if int(char) > highest_first_digit:
            highest_first_digit = int(char)
            highest_first_digit_index = i
            highest_last_digit = -1
    for char in batteries[highest_first_digit_index + 1:]:
        if int(char) > highest_last_digit:
            highest_last_digit = int(char)
    if highest_first_digit == -1 or highest_last_digit == -1:
        raise Exception("Could not determine largest joltage")
    
    return highest_first_digit * 10 + highest_last_digit

def calculate_largest_joltage(batteries):
    digits = [-1] * 12
    digit_indices = [0] * 12
    # Go through each of the 12 digits
    for i, digit in enumerate(digits):
        highest_digit = digit
        highest_digit_index = digit_indices[i]
        initial_highest_digit_index = highest_digit_index
        # For this digit, go through the batteries to find the highest value
        for j, char in enumerate(batteries[initial_highest_digit_index:len(batteries) - (11 - i)]):
            if int(char) > highest_digit:
                highest_digit = int(char)
                highest_digit_index = j + initial_highest_digit_index
            digits[i] = highest_digit
            digit_indices[i] = highest_digit_index
            for k in range(i + 1, 12):
                digit_indices[k] = highest_digit_index + 1

    joltage = 0
    for i, d in enumerate(digits):
        joltage += d * (10 ** (11 - i))
    return joltage


with open("input.txt") as f:
    lines = f.readlines()

total_joltage = 0
for line in lines:
    total_joltage += calculate_largest_joltage(line.strip())

print(f"Total largest joltage from all lines: {total_joltage}")