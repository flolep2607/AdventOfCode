from utils import AOCSolution
import json

class Day12(AOCSolution):
    def part1(self) -> None:
        data = json.loads(self.input)
        def sum_numbers(data):
            if isinstance(data, int):
                return data
            elif isinstance(data, list):
                return sum([sum_numbers(item) for item in data])
            elif isinstance(data, dict):
                return sum([sum_numbers(item) for item in data.values()])
            else:
                return 0

        print(sum_numbers(data))

    def part2(self) -> None:
        data = json.loads(self.input)
        def sum_numbers(data):
            if isinstance(data, int):
                return data
            elif isinstance(data, list):
                return sum([sum_numbers(item) for item in data])
            elif isinstance(data, dict):
                if "red" in data.values():
                    return 0
                return sum([sum_numbers(item) for item in data.values()])
            else:
                return 0

        print(sum_numbers(data))

if __name__ == "__main__":
    Day12().run()
