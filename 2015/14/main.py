from utils import AOCSolution
import re

class Day14(AOCSolution):
    def part1(self) -> None:
        regex = re.compile(r" (\d+) km/s for (\d+) seconds, but then must rest for (\d+) ", re.MULTILINE)
        seconds = 2503
        max_dist = 0
        for match in regex.finditer(self.input):
            speed, time, waittime = list(map(int, match.groups()))
            dist = speed * (
                time * (seconds // (time + waittime))
                + min(time, seconds % (time + waittime))
            )
            # print(speed, time, waittime, dist) # Original had print
            max_dist = max(max_dist, dist)
        print(max_dist)

    def part2(self) -> None:
        regex = re.compile(r" (\d+) km/s for (\d+) seconds, but then must rest for (\d+) ", re.MULTILINE)
        reindeer = []
        for match in regex.finditer(self.input):
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
            
        print(max([r["pts"] for r in reindeer]))

if __name__ == "__main__":
    Day14().run()
