from utils import AOCSolution

class Day06(AOCSolution):
    def part1(self) -> None:
        times = [int(x) for x in self.lines[0].split(":")[1].split()]
        lengths = [int(x) for x in self.lines[1].split(":")[1].split()]
        count = 1
        for time,length in zip(times,lengths):
            over = 0
            for speed in range(1,time):
                dist = speed * (time - speed)
                if dist > length:
                    over += 1
            count *= over
        print(count)

    def part2(self) -> None:
        time = int(self.lines[0].split(":")[1].replace(" ",""))
        length = int(self.lines[1].split(":")[1].replace(" ",""))
        # print(time,length)
        count = 0
        for speed in range(1,time):
            dist = speed * (time - speed)
            if dist > length:
                count += 1
        print(count)

if __name__ == "__main__":
    Day06().run()