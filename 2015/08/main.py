from utils import AOCSolution

class Day08(AOCSolution):
    def part1(self) -> None:
        count:int = 0
        for line in self.lines:
            count+=2
            index=1
            while index < len(line)-1:
                if line[index] == "\\":
                    if line[index+1] == "x":
                        count+=3
                        index+=4
                    else:
                        count+=1
                        index+=2
                else:
                    index+=1
        print(count)

    def part2(self) -> None:
        count:int = 0
        for line in self.lines:
            count+=2
            for char in line:
                if char == "\\" or char == "\"":
                    count+=1
        print(count)

if __name__ == "__main__":
    Day08().run()
