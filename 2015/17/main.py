from utils import AOCSolution

class Day17(AOCSolution):
    def part1(self) -> None:
        EGGNOG=150
        containers = [int(line) for line in self.lines]
        containers.sort(reverse=True)
        def recurse(contain:list[int],liters:int) -> int:
            if liters == 0:
                return 1
            else:
                count = 0
                for i, container in enumerate(contain):
                    if container <= liters:
                        count+= recurse(contain[i+1:], liters-container)
                return count
        
        print(recurse(containers,EGGNOG))

    def part2(self) -> None:
        EGGNOG=150
        containers = [int(line) for line in self.lines]
        containers.sort(reverse=True)
        def recurse(contain:list[int],liters:int) -> tuple[int,int]:
            if liters == 0:
                return 1,1
            else:
                min_depth = -1
                count = 0
                for i, container in enumerate(contain):
                    if container <= liters:
                        depth,temp_count = recurse(contain[i+1:], liters-container)
                        if depth > 0:
                            if min_depth == -1:
                                min_depth = depth
                                count = temp_count
                            elif depth < min_depth:
                                min_depth = depth
                                count = temp_count
                            elif depth == min_depth:
                                count += temp_count
                return (1+min_depth,count)
        
        print(recurse(containers,EGGNOG)[1])

if __name__ == "__main__":
    Day17().run()
