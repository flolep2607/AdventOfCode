from utils import AOCSolution
import re

class Day16(AOCSolution):
    def part1(self) -> None:
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
        for match in regex.finditer(self.input):
            if all(GOOD[match.group(i)] == int(match.group(i+1)) for i in range(2, 7, 2)):
                print(match.group(1))
                return

    def part2(self) -> None:
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
        for match in regex.finditer(self.input):
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
                print(match.group(1))
                return

if __name__ == "__main__":
    Day16().run()
