from utils import AOCSolution

class Day03(AOCSolution):
    def get_max_subsequence(self, bank, length):
        """
        Finds the largest number formed by a subsequence of `length` digits.
        """
        result = []
        current_idx = 0
        remaining_needed = length
        
        while remaining_needed > 0:
            limit = len(bank) - remaining_needed + 1
            
            if current_idx >= limit:
                break
                
            window = bank[current_idx : limit]
            
            best_digit = max(window)
            
            result.append(best_digit)
            
            offset = window.find(best_digit)
            current_idx += offset + 1
            remaining_needed -= 1
            
        return int("".join(result))

    def part1(self) -> None:
        total_p1 = 0
        for line in self.lines:
            if not line.strip():
                continue
            bank = line.strip()
            total_p1 += self.get_max_subsequence(bank, 2)
        print(f"Part 1 Solution: {total_p1}")

    def part2(self) -> None:
        total_p2 = 0
        for line in self.lines:
            if not line.strip():
                continue
            bank = line.strip()
            total_p2 += self.get_max_subsequence(bank, 12)
        print(f"Part 2 Solution: {total_p2}")


if __name__ == "__main__":
    Day03().run()
