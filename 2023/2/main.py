import re
import math
# Game 1: 1 red, 5 blue, 10 green; 5 green, 6 blue, 12 red; 4 red, 10 blue, 4 green
regex = re.compile(r"(\d+) (\w+)")

BAG={
    "red": 12,
    "green": 13,
    "blue": 14,
}
# PART 1
def part1():
    count:int = 0
    with open("input.txt", "r") as f:
        for index,line in enumerate(f):
            if all(int(match.group(1)) <= BAG[match.group(2)] for match in regex.finditer(line)):
                count += index+1
    return count


# PART 2
def part2():
    count:int = 0
    with open("input.txt", "r") as f:
        for line in f:
            game:dict[str,int]={
                "red": 0,
                "green": 0,
                "blue": 0
            }
            for match in regex.finditer(line):
                game[match.group(2)] = max(game[match.group(2)], int(match.group(1)))
            count += math.prod(game.values())
    return count

print(part2())
