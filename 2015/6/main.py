import numpy as np
import re

instruction_regex = re.compile(r"^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$")
# PART 1
def part1():
    count:int = 0
    matrix = np.zeros((1000,1000),dtype=bool)
    with open("input.txt", "r") as f:
        for line in f:
            instruction = instruction_regex.match(line)
            if instruction:
                instruction = instruction.groups()
                x1,y1,x2,y2 = [int(x) for x in instruction[1:]]
                if instruction[0] == "turn on":
                    matrix[x1:x2+1,y1:y2+1] = True
                elif instruction[0] == "turn off":
                    matrix[x1:x2+1,y1:y2+1] = False
                elif instruction[0] == "toggle":
                    matrix[x1:x2+1,y1:y2+1] = np.logical_not(matrix[x1:x2+1,y1:y2+1])
    count = np.sum(matrix)
    return count


# PART 2
def part2():
    count:int = 0
    matrix = np.zeros((1000,1000),dtype=int)
    with open("input.txt", "r") as f:
        for line in f:
            instruction = instruction_regex.match(line)
            if instruction:
                instruction = instruction.groups()
                x1,y1,x2,y2 = [int(x) for x in instruction[1:]]
                if instruction[0] == "turn on":
                    matrix[x1:x2+1,y1:y2+1] += 1
                elif instruction[0] == "turn off":
                    matrix[x1:x2+1,y1:y2+1] -= 1
                    matrix[matrix < 0] = 0
                elif instruction[0] == "toggle":
                    matrix[x1:x2+1,y1:y2+1] += 2
    count = np.sum(matrix)
    return count

print(part2())
