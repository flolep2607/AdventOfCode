from utils import AOCSolution
from collections import defaultdict

class Day07(AOCSolution):
    def part1(self) -> None:
        grid = [list(line) for line in self.lines]
        
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        
        # Find the starting position (S)
        start_col = None
        for c in range(cols):
            if grid[0][c] == 'S':
                start_col = c
                break
        
        # Track active beams as (row, col) - all beams move downward
        split_count = 0
        
        # Start with beam just below S
        active_beams = set()
        active_beams.add((0, start_col))  # Start at S position
        
        while active_beams:
            # Move all beams down one row
            next_beams = set()
            
            for row, col in active_beams:
                next_row = row + 1
                
                # Check if beam exits the grid
                if next_row >= rows:
                    continue
                
                cell = grid[next_row][col]
                
                if cell == '.' or cell == '|':
                    # Beam continues downward
                    next_beams.add((next_row, col))
                elif cell == '^':
                    # Beam hits a splitter - count this split
                    split_count += 1
                    
                    # Create two new beams: one left, one right
                    left_col = col - 1
                    right_col = col + 1
                    
                    if left_col >= 0:
                        next_beams.add((next_row, left_col))
                    if right_col < cols:
                        next_beams.add((next_row, right_col))
            
            active_beams = next_beams
        
        print(split_count)

    def part2(self) -> None:
        grid = [list(line) for line in self.lines]
        
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        
        # Find the starting position (S)
        start_col = None
        for c in range(cols):
            if grid[0][c] == 'S':
                start_col = c
                break
        
        # Start with 1 timeline at the S position
        active_timelines = defaultdict(int)
        active_timelines[(0, start_col)] = 1
        
        total_finished_timelines = 0
        
        while active_timelines:
            next_timelines = defaultdict(int)
            
            for (row, col), count in active_timelines.items():
                next_row = row + 1
                
                # Check if timeline exits the grid
                if next_row >= rows:
                    total_finished_timelines += count
                    continue
                
                cell = grid[next_row][col]
                
                if cell == '.' or cell == '|':
                    # Timeline continues downward
                    next_timelines[(next_row, col)] += count
                elif cell == '^':
                    # Timeline hits a splitter - each timeline branches into 2
                    left_col = col - 1
                    right_col = col + 1
                    
                    if left_col >= 0:
                        next_timelines[(next_row, left_col)] += count
                    if right_col < cols:
                        next_timelines[(next_row, right_col)] += count
            
            active_timelines = next_timelines
        
        print(total_finished_timelines)

if __name__ == '__main__':
    Day07().run()
