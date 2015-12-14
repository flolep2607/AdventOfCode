import re

regex = re.compile(r" (\d+) km/s for (\d+) seconds, but then must rest for (\d+) ", re.MULTILINE)


# PART 1
def part1():
    seconds = 2503
    max_dist = 0
    with open("input.txt", "r") as f:
        for match in regex.finditer(f.read()):
            speed, time, waittime = list(map(int, match.groups()))
            dist = speed * (
                time * (seconds // (time + waittime))
                + min(time, seconds % (time + waittime))
            )
            print(speed, time, waittime, dist)
            max_dist = max(max_dist, dist)
    return max_dist


# PART 2
def part2():
    reindeer = []
    with open("input.txt", "r") as f:
        for match in regex.finditer(f.read()):
            speed, time, waittime = list(map(int, match.groups()))
            reindeer.append({
                "speed":speed, 
                "time":time, 
                "waittime":waittime,
                "running":True,
                "state_time":0,
                "pts":0,
                "dist":0
            })
    for i in range(2503):
        for r in reindeer:
            if r["running"]:
                r["dist"] += r["speed"]
                r["state_time"] += 1
                if r["state_time"] == r["time"]:
                    r["state_time"] = 0
                    r["running"] = False
            else:
                r["state_time"] += 1
                if r["state_time"] == r["waittime"]:
                    r["state_time"] = 0
                    r["running"] = True
        max_dist = max([r["dist"] for r in reindeer])
        for r in reindeer:
            if r["dist"] == max_dist:
                r["pts"] += 1
        
    return max([r["pts"] for r in reindeer])


print(part2())
