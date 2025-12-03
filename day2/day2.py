with open("input.txt") as f:
    lines = f.readlines()

def determine_if_invalid_id(id):
    str_id = str(id)
    can_be_invalid = False
    for length in range(1, (len(str_id) // 2) + 1):
        if len(str_id) % length != 0:
            continue
        can_be_invalid = True
        start = 0
        sample = ""
        for i in range(len(str_id) // length):
            end = start + length
            if i == 0:
                sample = str_id[start:end]
            else:
                if str_id[start:end] != sample:
                    can_be_invalid = False
                    break
            start = end
        if can_be_invalid:
            break
    return can_be_invalid


invalid_id_total = 0
for line in lines:
    ids = line.split(",")
    for id in ids:
        start = int(id.split("-")[0])
        end = int(id.split("-")[1])
        for num in range(start, end + 1):
            if determine_if_invalid_id(num):
                invalid_id_total += num
                print(f"Invalid ID found: {num}")
print(f"Total of invalid IDs: {invalid_id_total}")            
