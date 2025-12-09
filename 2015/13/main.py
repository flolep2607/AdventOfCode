from utils import AOCSolution
import re
from itertools import permutations

class Day13(AOCSolution):
    def part1(self) -> None:
        regex = re.compile(
            r"([^ ]+) would (lose|gain) (\d+) happiness units by sitting next to ([^\.]+)."
        )
        invites: dict[str, dict[str, int]] = {}
        for line in self.lines:
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

        print(max(calculate_happiness(names) for names in permutations(invites.keys())))

    def part2(self) -> None:
        regex = re.compile(
            r"([^ ]+) would (lose|gain) (\d+) happiness units by sitting next to ([^\.]+)."
        )
        invites: dict[str or bool, dict[str, int]] = {False:{}}
        # Note: False is used as "Me" in the original code? 
        # original code: invites = {False:{}} ... 
        # "name1 not in invites" logic works.
        # But wait, original code iterates self.input lines and ADDS to invites.
        # So invites starts with {False:{}}.
        
        for line in self.lines:
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

        print(max(calculate_happiness(names) for names in permutations(invites.keys())))

if __name__ == "__main__":
    Day13().run()
