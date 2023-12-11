# PART 1
def part1():
    count:int = 0
    with open("input.txt", "r") as f:
        for line in f:
            first: int = -1
            last: int = -1
            # complexity: O(n)
            for letter in line:
                if letter.isdigit():
                    if first == -1:
                        first = int(letter)
                    last = int(letter)
            count += first * 10 + last
    return count


# PART 2
def part2():
    count:int = 0
    numbers: list[str]= ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    def getNumber(part: str) -> int or None:
        for i,number in enumerate(numbers):
            if part.startswith(number):
                return i
    with open("input.txt", "r") as f:
        for line in f:
            first: int = -1
            last: int = -1
            # complexity: O(n)
            for i in range(len(line)):
                if line[i].isdigit():
                    if first == -1:
                        first = int(line[i])
                    last = int(line[i])
                else:
                    number=getNumber(line[i:])
                    if number is not None:
                        if first == -1:
                            first = number
                        last = number
            count += first * 10 + last
    return count

print(part2())
