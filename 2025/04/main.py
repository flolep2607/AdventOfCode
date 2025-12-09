from utils import AOCSolution

class Day04(AOCSolution):
    def solve_logic(self):
        grid = [list(line.strip()) for line in self.lines]
        
        rows = len(grid)
        cols = len(grid[0])
        total_removed = 0

        while True:
            to_remove = []
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == '@':
                        neighbor_rolls = 0
                        for dr in [-1, 0, 1]:
                            for dc in [-1, 0, 1]:
                                if dr == 0 and dc == 0:
                                    continue
                                
                                nr, nc = r + dr, c + dc
                                
                                if 0 <= nr < rows and 0 <= nc < cols:
                                    if grid[nr][nc] == '@':
                                        neighbor_rolls += 1
                        
                        if neighbor_rolls < 4:
                            to_remove.append((r, c))
            
            if not to_remove:
                break
                
            total_removed += len(to_remove)
            
            # Apply removals
            for r, c in to_remove:
                grid[r][c] = '.'
                
        return total_removed

    def part1(self) -> None:
        print(self.solve_logic())

    def part2(self) -> None:
        print(self.solve_logic())

if __name__ == "__main__":
    Day04().run()
