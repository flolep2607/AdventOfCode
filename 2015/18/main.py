EGGNOG=150
# PART 1
def part1():
    grid:list[list[bool]] = []
    for line in open("input.txt", "r").readlines():
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
        for line in grid:
            print("".join(["#" if c else "." for c in line]))
        print("=====")
    return sum([sum(row) for row in grid])

# PART 2
def part2():
    grid:list[list[bool]] = []
    for line in open("input.txt", "r").readlines():
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
    
    for _ in range(100):
        grid = step(grid)
        print(_+1)
        for line in grid:
            print("".join(["#" if c else "." for c in line]))
        print("=====")
    return sum([sum(row) for row in grid])


print(part2())
