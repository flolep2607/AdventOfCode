import re
from itertools import permutations

regex = re.compile(
    r"([^ ]+) would (lose|gain) (\d+) happiness units by sitting next to ([^\.]+)."
)


# PART 1
def part1():
    invites: dict[str, dict[str, int]] = {}
    with open("input.txt", "r") as f:
        for line in f:
            match = regex.match(line)
            if match:
                name1 = match.group(1)
                name2 = match.group(4)
                if name1 not in invites:
                    invites[name1] = {}
                invites[name1][name2] = int(match.group(3)) * (
                    -1 if match.group(2) == "lose" else 1
                )

    def calculate_happiness(names: list[str] = []) -> int:
        happiness: int = 0
        for i in range(len(names)):
            happiness += (
                invites[names[i]][names[(i + 1) % len(names)]]
                + invites[names[(i + 1) % len(names)]][names[i]]
            )
        return happiness

    return max(calculate_happiness(names) for names in permutations(invites.keys()))


# PART 2
def part2():
    invites: dict[str or bool, dict[str, int]] = {False:{}}
    with open("input.txt", "r") as f:
        for line in f:
            match = regex.match(line)
            if match:
                name1 = match.group(1)
                name2 = match.group(4)
                if name1 not in invites:
                    invites[name1] = {}
                invites[name1][name2] = int(match.group(3)) * (
                    -1 if match.group(2) == "lose" else 1
                )

    def calculate_happiness(names: list[str or bool] = []) -> int:
        happiness: int = 0
        for i in range(len(names)):
            next = names[(i + 1) % len(names)]
            current = names[i]
            if current == False or next == False:
                continue
            happiness += (
                invites[current][next]
                + invites[next][current]
            )
        return happiness

    return max(calculate_happiness(names) for names in permutations(invites.keys()))


print(part2())
