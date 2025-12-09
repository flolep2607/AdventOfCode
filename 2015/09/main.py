from utils import AOCSolution

class Day09(AOCSolution):
    def part1(self) -> None:
        cities:set[str] = set()
        dists:dict[tuple[str],int] = {}
        for line in self.lines:
            _cities,dist = line.split("=")
            start_city,end_city = [i.strip() for i in _cities.split("to")]
            dists[(start_city,end_city)] = int(dist)
            cities.add(start_city)
            cities.add(end_city)
    
        def distance(done:list[str]=[]) -> int:
            if len(done) == len(cities):
                calculated_dist:int = 0
                for i in range(len(done)-1):
                    if (done[i],done[i+1]) in dists:
                        calculated_dist += dists[(done[i],done[i+1])]
                    else:
                        calculated_dist += dists[(done[i+1],done[i])]
                return calculated_dist
            best_dist:int = -1
            for city in cities:
                if city not in done:
                    dist = distance(done+[city])
                    if best_dist == -1 or dist < best_dist:
                        best_dist = dist
            return best_dist
    
        print(distance())

    def part2(self) -> None:
        cities:set[str] = set()
        dists:dict[tuple[str],int] = {}
        for line in self.lines:
            _cities,dist = line.split("=")
            start_city,end_city = [i.strip() for i in _cities.split("to")]
            dists[(start_city,end_city)] = int(dist)
            cities.add(start_city)
            cities.add(end_city)
    
        def distance(done:list[str]=[]) -> int:
            if len(done) == len(cities):
                calculated_dist:int = 0
                for i in range(len(done)-1):
                    if (done[i],done[i+1]) in dists:
                        calculated_dist += dists[(done[i],done[i+1])]
                    else:
                        calculated_dist += dists[(done[i+1],done[i])]
                return calculated_dist
            best_dist:int = -1
            for city in cities:
                if city not in done:
                    dist = distance(done+[city])
                    if best_dist == -1 or dist > best_dist:
                        best_dist = dist
            return best_dist
        print(distance())

if __name__ == "__main__":
    Day09().run()
