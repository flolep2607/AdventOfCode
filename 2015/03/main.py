from utils import AOCSolution

class Day03(AOCSolution):
    def part1(self) -> None:
        count:int = 0
        map_visited:dict[int,dict[int,bool]] = {}
        x,y = 0,0
        map_visited[0] = {0: True}
        count = 1
        
        count = 0
        map_visited = {}
        x, y = 0, 0
        
        for char in self.input:
            if char == '^':
                y += 1
            elif char == 'v':
                y -= 1
            elif char == '>':
                x += 1
            elif char == '<':
                x -= 1
            if x not in map_visited:
                map_visited[x] = {}
            if y not in map_visited[x]:
                map_visited[x][y] = True
                count += 1
        print(count)

    def part2(self) -> None:
        count:int = 0
        map_visited:dict[int,dict[int,bool]] = {}
        x,y = [0,0],[0,0]
        # Same check about initial position.
        # I will copy logic exactly.
        
        for index,char in enumerate(self.input):
            index=index%2
            if char == '^':
                y[index] += 1
            elif char == 'v':
                y[index] -= 1
            elif char == '>':
                x[index] += 1
            elif char == '<':
                x[index] -= 1
            if x[index] not in map_visited:
                map_visited[x[index]] = {}
            if y[index] not in map_visited[x[index]]:
                map_visited[x[index]][y[index]] = True
                count += 1
        print(count)

if __name__ == "__main__":
    Day03().run()
