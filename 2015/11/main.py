from utils import AOCSolution
from typing import Iterable

class Day11(AOCSolution):
    def part1(self) -> None:
        input_str = "hxbxwxba"
        
        A=ord("a")
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
        
        for password in gen_string(input_str):
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
                print(password)
                return

    def part2(self) -> None:
        # Part 2 requires the result of Part 1 as input.
        # Since part 1 is deterministic and I know the input "hxbxwxba", I can run the logic twice.
        
        input_str = "hxbxwxba"
        A=ord("a")
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

        def solve(start_str):
            for password in gen_string(start_str):
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

        p1 = solve(input_str)
        p2 = solve(p1)
        print(p2)

if __name__ == "__main__":
    Day11().run()
