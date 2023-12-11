# PART 1
def part1():
    count:int = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            count+=2
            index=1
            while index < len(line)-1:
                if line[index] == "\\":
                    if line[index+1] == "x":
                        count+=3
                        index+=4
                    else:
                        count+=1
                        index+=2
                else:
                    index+=1
    return count


# PART 2
def part2():
    count:int = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            count+=2
            for char in line:
                if char == "\\" or char == "\"":
                    count+=1
    return count

print(part2())
