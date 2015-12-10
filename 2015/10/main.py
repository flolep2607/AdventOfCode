input = "1113222113"
# PART 1
def part1():
    data=list(map(int,input))
    for _ in range(40):
        new_data = []
        i = 0
        while i < len(data):
            count = 1
            while i+1 < len(data) and data[i] == data[i+1]:
                count += 1
                i += 1
            new_data.append(count)
            new_data.append(data[i])
            i += 1
        data = new_data
    return len(data)


# PART 2

def part2():
    data=list(map(int,input))
    for _ in range(50):
        new_data = []
        i = 0
        while i < len(data):
            count = 1
            while i+1 < len(data) and data[i] == data[i+1]:
                count += 1
                i += 1
            new_data.append(count)
            new_data.append(data[i])
            i += 1
        data = new_data
    return len(data)


print(part2())
