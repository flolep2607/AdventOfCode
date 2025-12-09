from utils import AOCSolution

class Day05(AOCSolution):
    def part1(self) -> None:
        count:int = 0
        voewls = "aeiou"
        bad_parts=["ab","cd","pq","xy"]
        for line in self.lines:
            count_voewls = 0
            consecutive = False
            bad = False
            for index,char in enumerate(line):
                if char in voewls:
                    count_voewls+=1
                if index>0 and char == line[index-1]:
                    consecutive = True
                if (line[index-1]+char) in bad_parts:
                    bad = True
            if count_voewls>=3 and consecutive and not bad:
                count+=1
        print(count)

    def part2(self) -> None:
        count:int = 0
        for line in self.lines:
            consecutive1 = False
            consecutive2 = False
            for index in range(len(line)):
                if not consecutive1:
                    for index2 in range(index+2,len(line)):
                        if line[index:index+2] == line[index2:index2+2]:
                            consecutive1=True
                            break
                if not consecutive2 and index<len(line)-2 and line[index] == line[index+2]:
                    consecutive2=True
                
            if consecutive1 and consecutive2:
                count+=1
        print(count)

if __name__ == "__main__":
    Day05().run()
