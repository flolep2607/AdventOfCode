from utils import AOCSolution
import numpy as np
import re

class Day06(AOCSolution):
    def part1(self) -> None:
        instruction_regex = re.compile(r"^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$")
        count:int = 0
        matrix = np.zeros((1000,1000),dtype=bool)
        for line in self.lines:
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
        print(count)

    def part2(self) -> None:
        instruction_regex = re.compile(r"^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$")
        count:int = 0
        matrix = np.zeros((1000,1000),dtype=int)
        for line in self.lines:
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
        print(count)

if __name__ == "__main__":
    Day06().run()
