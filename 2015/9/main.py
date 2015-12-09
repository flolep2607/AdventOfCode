# PART 1
def part1():
    cities:set[str] = set()
    dists:dict[tuple[str],int] = {}
    with open("input.txt", "r") as f:
        for line in f.readlines():
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
    
    return distance()


# PART 2

def part2():
    cities:set[str] = set()
    dists:dict[tuple[str],int] = {}
    with open("input.txt", "r") as f:
        for line in f.readlines():
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
    return distance()


print(part2())
