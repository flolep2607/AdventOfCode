from typing import Iterable

A=ord("a")

input = "hxbxwxba"
illegal_chars:list[int]=[ord("i")-A, ord("o")-A, ord("l")-A]
def gen_string(string: str) -> Iterable[str]:
    values=[ord(char)-A for char in string]
    while True:
        values[-1] += 1
        for i in range(len(values)-1, -1, -1):
            if values[i] > 25:
                values[i] = 0
                if values[i-1] in illegal_chars:
                    values[i-1] += 2
                else:
                    values[i-1] += 1
            else:
                break
        yield "".join([chr(value+A) for value in values])

# PART 1
def part1(_input):
    for password in gen_string(_input):
        increasing = False
        confusing = False
        pairs = 0
        last_pair_index = 0
        for i in range(len(password)):
            if (
                not increasing
                and i > 2
                and ord(password[i]) == ord(password[i - 1]) + 1
                and ord(password[i]) == ord(password[i - 2]) + 2
            ):
                increasing = True
            if (
                i > last_pair_index + 1
                and password[i] == password[i - 1]
            ):
                pairs += 1
                last_pair_index = i
                if pairs >= 2:
                    break
        if pairs >= 2 and increasing and not confusing:
            return password


# PART 2
def part2(_input):
    return part1(part1(_input))


print(part2(input))
