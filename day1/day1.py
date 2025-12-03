with open("input.txt") as f:
    lines = f.readlines()

quotient = 0
pos = 50
password = 0

for line in lines:
    direction = line[0]
    distance = int(line[1:])
    # If we're making several revolutions, just add those directly
    quotient, distance = divmod(distance, 100)
    password += quotient

    # If we started on the zero point and are turning left, we lose one position because the quotient will add in back.
    if pos == 0 and direction == 'L':
        password -= 1

    if direction == 'L':
        pos -= distance
    elif direction == 'R':
        pos += distance
    quotient, pos = divmod(pos, 100)
    password += abs(quotient)
    if pos == 0 and quotient == 0:
        password += 1
    print(f"Line: {line.strip()}, Position: {pos}, Quotient: {quotient}, Password: {password}")

print(f"Final Position: {pos}, Password: {password}")