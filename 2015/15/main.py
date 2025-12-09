from utils import AOCSolution
import re
import math
from typing import Iterable

class Day15(AOCSolution):
    def part1(self) -> None:
        regex = re.compile(
            r"capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)",
            re.MULTILINE,
        )
        max_val = 0
        ingredients = []
        for match in regex.finditer(self.input):
            cap, dur, fla, tex, cal = list(map(int, match.groups()))
            ingredients.append((cap, dur, fla, tex, cal))

        def repartitor(ingred:int, total:int) -> Iterable[list]:
            if ingred == 1:
                yield [total]
            else:
                for i in range(total+1):
                    for liste in repartitor(ingred - 1, total - i):
                        yield [i] + liste
        for liste in repartitor(len(ingredients), 100):
            vals=[0,0,0,0]
            for j in range(len(vals)):
                for i, ingredient in enumerate(ingredients):
                    vals[j] += liste[i] * ingredient[j]
                if vals[j] < 0:
                    vals[j] = 0
                    break
            if min(vals) == 0:
                continue
            val = math.prod(vals)
            if val > max_val:
                max_val = val
        print(max_val)

    def part2(self) -> None:
        regex = re.compile(
            r"capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)",
            re.MULTILINE,
        )
        max_val = 0
        ingredients = []
        for match in regex.finditer(self.input):
            cap, dur, fla, tex, cal = list(map(int, match.groups()))
            ingredients.append((cap, dur, fla, tex, cal))

        def repartitor(ingred:int, total:int) -> Iterable[list]:
            if ingred == 1:
                yield [total]
            else:
                for i in range(total+1):
                    for liste in repartitor(ingred - 1, total - i):
                        yield [i] + liste
        for liste in repartitor(len(ingredients), 100):
            vals=[0,0,0,0,0]
            for j in range(len(vals)):
                for i, ingredient in enumerate(ingredients):
                    vals[j] += liste[i] * ingredient[j]
                if vals[j] < 0:
                    vals[j] = 0
                    break
            if min(vals) == 0 or vals[-1] != 500:
                continue
            val = math.prod(vals[:-1])
            if val > max_val:
                max_val = val
        print(max_val)

if __name__ == "__main__":
    Day15().run()
