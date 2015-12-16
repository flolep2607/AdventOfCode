import re
from typing import Iterable

# Sue 1: goldfish: 9, cars: 0, samoyeds: 9
regex = re.compile(
    r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)",
    re.MULTILINE,
)

GOOD={
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

# PART 1
def part1():
    with open("input.txt", "r") as f:
        for match in regex.finditer(f.read()):
            if all(GOOD[match.group(i)] == int(match.group(i+1)) for i in range(2, 7, 2)):
                return match.group(1)


# PART 2
def part2():
    with open("input.txt", "r") as f:
        for match in regex.finditer(f.read()):
            good=True
            for group in range(2, 7, 2):
                if match.group(group) in ["cats", "trees"]:
                    if GOOD[match.group(group)] >= int(match.group(group+1)):
                        good=False
                elif match.group(group) in ["pomeranians", "goldfish"]:
                    if GOOD[match.group(group)] <= int(match.group(group+1)):
                        good=False
                elif GOOD[match.group(group)] != int(match.group(group+1)):
                    good=False
            if good:
                return match.group(1)


print(part2())
