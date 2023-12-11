from hashlib import md5

input = "ckczppom"

# PART 1
def part1():
    count:int = 0
    while not md5((input+str(count)).encode()).hexdigest().startswith("0"*5):
        count += 1
    return count


# PART 2
def part2():
    count:int = 0
    while not md5((input+str(count)).encode()).hexdigest().startswith("0"*6):
        count += 1
    return count

print(part2())
