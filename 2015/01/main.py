from utils import AOCSolution

class Day01(AOCSolution):
    def part1(self) -> None:
        count:int = 0
        for c in self.input:
            if c=='(':
                count+=1
            elif c==')':
                count-=1
        print(count)

    def part2(self) -> None:
        count:int = 0
        for index,c in enumerate(self.input):
            if c=='(':
                count+=1
            elif c==')':
                count-=1
            if count==-1:
                print(index+1)
                return

if __name__ == "__main__":
    Day01().run()
