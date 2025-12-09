from utils import AOCSolution
import re
import math

class Day02(AOCSolution):
    def part1(self) -> None:
        regex = re.compile(r"(\d+) (\w+)")
        BAG={
            "red": 12,
            "green": 13,
            "blue": 14,
        }
        count:int = 0
        for index,line in enumerate(self.lines):
            if all(int(match.group(1)) <= BAG[match.group(2)] for match in regex.finditer(line)):
                count += index+1
        print(count)

    def part2(self) -> None:
        regex = re.compile(r"(\d+) (\w+)")
        count:int = 0
        for line in self.lines:
            game:dict[str,int]={
                "red": 0,
                "green": 0,
                "blue": 0
            }
            for match in regex.finditer(line):
                game[match.group(2)] = max(game[match.group(2)], int(match.group(1)))
            count += math.prod(game.values())
        print(count)

if __name__ == "__main__":
    Day02().run()
