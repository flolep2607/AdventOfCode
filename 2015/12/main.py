import json
# PART 1
def part1():
    with open("input.txt", "r") as f:
        data = json.load(f)
    def sum_numbers(data):
        if isinstance(data, int):
            return data
        elif isinstance(data, list):
            return sum([sum_numbers(item) for item in data])
        elif isinstance(data, dict):
            return sum([sum_numbers(item) for item in data.values()])
        else:
            return 0

    return sum_numbers(data)


# PART 2
def part2():
    with open("input.txt", "r") as f:
        data = json.load(f)
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

    return sum_numbers(data)


print(part2())
