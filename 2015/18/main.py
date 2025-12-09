from utils import AOCSolution

class Day18(AOCSolution):
    def part1(self) -> None:
        grid:list[list[bool]] = []
        for line in self.lines:
            grid.append([c == "#" for c in line.strip()])
        
        def count_neighbors(grid:list[list[bool]],x:int,y:int) -> int:
            count = 0
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]):
                        if i != x or j != y:
                            if grid[i][j]:
                                count += 1
            return count
        def step(grid:list[list[bool]]) -> list[list[bool]]:
            new_grid:list[list[bool]] = []
            for i in range(len(grid)):
                new_grid.append([])
                for j in range(len(grid[i])):
                    count = count_neighbors(grid,i,j)
                    if grid[i][j]:
                        new_grid[i].append(count == 2 or count == 3)
                    else:
                        new_grid[i].append(count == 3)
            return new_grid
        
        for _ in range(100):
            grid = step(grid)
            # Visualization disabled for AOCSolution
            # for line in grid:
            #     print("".join(["#" if c else "." for c in line]))
            # print("=====")
        print(sum([sum(row) for row in grid]))

    def part2(self) -> None:
        grid:list[list[bool]] = []
        for line in self.lines:
            grid.append([c == "#" for c in line.strip()])
        
        def count_neighbors(grid:list[list[bool]],x:int,y:int) -> int:
            count = 0
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]):
                        if i != x or j != y:
                            if grid[i][j]:
                                count += 1
            return count
        def step(grid:list[list[bool]]) -> list[list[bool]]:
            new_grid:list[list[bool]] = []
            for i in range(len(grid)):
                new_grid.append([])
                for j in range(len(grid[i])):
                    count = count_neighbors(grid,i,j)
                    if grid[i][j]:
                        new_grid[i].append(count == 2 or count == 3)
                    else:
                        new_grid[i].append(count == 3)
            for i in [0,len(grid)-1]:
                for j in [0,len(grid[i])-1]:
                    new_grid[i][j] = True
            return new_grid
        
        # Initial corners stuck on for Part 2?
        # Original code did:
        # for _ in range(100):
        #   grid = step(grid)
        # And step() enforced corners at the END of step.
        # But wait, did it enforce them at start?
        # Original code Part 2:
        # Loop:
        #   grid = step(grid)
        # Inside step:
        #   compute new_grid based on old grid
        #   force corners on new_grid
        #   return new_grid
        # So the very first grid (read from file) might not have corners on?
        # The problem description says "Four lights... are stuck on".
        # If the input doesn't have them on, they should be turned on initially?
        # The original code DOES NOT turn them on initially before the first step, only after.
        # Wait, if the simulation rules apply, the corners are STUCK on, meaning they are always on.
        # If original code passed, it implies either input had them on, or the first step enforcement was sufficient.
        # I will stick to original logic: step() enforces corners on the RESULT.
        
        # Wait, I should verify if I need to force them initially.
        # Original code reading:
        # grid = [] ...
        # loop 100: grid = step(grid)
        # It never forced them on `grid` before loop.
        # Use exact logic.
        
        for _ in range(100):
            grid = step(grid)
        print(sum([sum(row) for row in grid]))

if __name__ == "__main__":
    Day18().run()
