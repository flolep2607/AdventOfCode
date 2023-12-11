#PART 1
def part1():
    with open("input.txt", "r") as f:
        times = [int(x) for x in f.readline().split(":")[1].split()]
        lengths = [int(x) for x in f.readline().split(":")[1].split()]
    count = 1
    for time,length in zip(times,lengths):
        over = 0
        for speed in range(1,time):
            dist = speed * (time - speed)
            if dist > length:
                over += 1
        count *= over
    return count

# PART 2
def part2():
    with open("input.txt", "r") as f:
        time = int(f.readline().split(":")[1].replace(" ",""))
        length = int(f.readline().split(":")[1].replace(" ",""))
    print(time,length)
    count = 0
    for speed in range(1,time):
        dist = speed * (time - speed)
        if dist > length:
            count += 1
    return count

print(part2())