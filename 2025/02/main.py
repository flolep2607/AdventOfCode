from utils import AOCSolution

class Day02(AOCSolution):
    def is_invalid_part1(self, n):
        """
        Checks if a number is invalid for Part 1.
        An ID is invalid if it consists of a sequence of digits repeated exactly twice.
        """
        s = str(n)
        if len(s) % 2 != 0:
            return False
        mid = len(s) // 2
        return s[:mid] == s[mid:]

    def is_invalid_part2(self, n):
        """
        Checks if a number is invalid for Part 2.
        An ID is invalid if it is made only of some sequence of digits repeated at least twice.
        """
        s = str(n)
        length = len(s)
        # Try all possible pattern lengths from 1 up to len(s) // 2
        for pat_len in range(1, length // 2 + 1):
            if length % pat_len == 0:
                pattern = s[:pat_len]
                repeats = length // pat_len
                if pattern * repeats == s:
                    return True
        return False

    def parse_input(self):
        ranges_str = self.input.replace("\n", "").split(",")
        ranges = []
        for r_str in ranges_str:
            if not r_str:
                continue
            try:
                start_str, end_str = r_str.split("-")
                ranges.append((int(start_str), int(end_str)))
            except ValueError:
                print(f"Skipping malformed range: {r_str}")
        return ranges

    def part1(self) -> None:            
        parsed_ranges = self.parse_input()
        total_sum = 0
        for start, end in parsed_ranges:
            for num in range(start, end + 1):
                if self.is_invalid_part1(num):
                    total_sum += num
        print(f"Part 1 Solution: {total_sum}")

    def part2(self) -> None:
        parsed_ranges = self.parse_input()
        total_sum = 0
        for start, end in parsed_ranges:
            for num in range(start, end + 1):
                if self.is_invalid_part2(num):
                    total_sum += num
        print(f"Part 2 Solution: {total_sum}")


if __name__ == "__main__":
    Day02().run()
