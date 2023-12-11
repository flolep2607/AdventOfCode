# PART 1
def part1():
    count:int = 0
    with open("input.txt", "r") as f:
        for c in f.read():
            if c=='(':
                count+=1
            elif c==')':
                count-=1
    return count


# PART 2
def part2():
    count:int = 0
    with open("input.txt", "r") as f:
        for index,c in enumerate(f.read()):
            if c=='(':
                count+=1
            elif c==')':
                count-=1
            if count==-1:
                return index+1

print(part2())
