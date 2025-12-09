from utils import AOCSolution

class Day01(AOCSolution):
    def part1(self) -> None:
        current_pos = 50
        zero_count = 0

        for line in self.lines:
            line = line.strip()
            if not line:
                continue
            
            direction = line[0]
            distance = int(line[1:])

            if direction == 'R':
                current_pos = (current_pos + distance) % 100
            elif direction == 'L':
                current_pos = (current_pos - distance) % 100
            
            if current_pos == 0:
                zero_count += 1
                
        print(f"Part 1 Password: {zero_count}")

    def part2(self) -> None:
        current_pos = 50
        zero_count = 0

        for line in self.lines:
            line = line.strip()
            if not line:
                continue
            
            direction = line[0]
            distance = int(line[1:])

            if direction == 'R':
                new_pos = current_pos + distance
                zero_count += (new_pos // 100) - (current_pos // 100)
                current_pos = new_pos
            elif direction == 'L':
                new_pos = current_pos - distance
                zero_count += ((current_pos - 1) // 100) - ((new_pos - 1) // 100)
                current_pos = new_pos
                
        print(f"Part 2 Password: {zero_count}")

if __name__ == "__main__":
    Day01().run()
