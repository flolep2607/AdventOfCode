from utils import AOCSolution

class Day05(AOCSolution):
    def part1(self) -> None:
        # Split by empty line to separate ranges from ingredient IDs
        parts = self.input.strip().split('\n\n')
        range_lines = parts[0].split('\n')
        ingredient_lines = parts[1].split('\n')
        
        # Parse ranges
        ranges = []
        for line in range_lines:
            start, end = line.split('-')
            ranges.append((int(start), int(end)))
        
        # Parse ingredient IDs
        ingredients = [int(line) for line in ingredient_lines]
        
        # Count fresh ingredients
        fresh_count = 0
        for ingredient in ingredients:
            for start, end in ranges:
                if start <= ingredient <= end:
                    fresh_count += 1
                    break  # Only need to find one matching range
        
        print(f"Part 1: {fresh_count}")

    def part2(self) -> None:
        # Split by empty line to separate ranges from ingredient IDs
        parts = self.input.strip().split('\n\n')
        range_lines = parts[0].split('\n')
        
        # Parse ranges
        ranges = []
        for line in range_lines:
            start, end = line.split('-')
            ranges.append((int(start), int(end)))
        
        # Sort ranges by start
        ranges.sort()
        
        # Merge overlapping ranges
        merged = [ranges[0]]
        for start, end in ranges[1:]:
            last_start, last_end = merged[-1]
            if start <= last_end + 1:  # Overlapping or adjacent
                merged[-1] = (last_start, max(last_end, end))
            else:
                merged.append((start, end))
        
        # Count total unique IDs
        total = sum(end - start + 1 for start, end in merged)
        
        print(f"Part 2: {total}")

if __name__ == "__main__":
    Day05().run()
