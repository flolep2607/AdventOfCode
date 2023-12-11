# PART 1
def part1():
    count:int = 0
    map:dict[int,dict[int,bool]] = {}
    x,y = 0,0
    with open("input.txt", "r") as f:
        for char in f.read():
            if char == '^':
                y += 1
            elif char == 'v':
                y -= 1
            elif char == '>':
                x += 1
            elif char == '<':
                x -= 1
            if x not in map:
                map[x] = {}
            if y not in map[x]:
                map[x][y] = True
                count += 1
    return count


# PART 2
def part2():
    count:int = 0
    map:dict[int,dict[int,bool]] = {}
    x,y = [0,0],[0,0]
    with open("input.txt", "r") as f:
        for index,char in enumerate(f.read()):
            index=index%2
            if char == '^':
                y[index] += 1
            elif char == 'v':
                y[index] -= 1
            elif char == '>':
                x[index] += 1
            elif char == '<':
                x[index] -= 1
            if x[index] not in map:
                map[x[index]] = {}
            if y[index] not in map[x[index]]:
                map[x[index]][y[index]] = True
                count += 1
    return count

print(part2())
