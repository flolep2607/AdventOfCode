from utils import AOCSolution

class Day04(AOCSolution):
    def part1(self) -> None:
        count = 0
        for line in self.lines:
            usefullpart = line.split(":")[1]
            winner_numbers,numbers = usefullpart.split("|")
            winner_numbers,numbers = set(int(x) for x in winner_numbers.split()), set(int(x) for x in numbers.split())
            good=len(winner_numbers.intersection(numbers))
            if good>0:
                count+=2**(good-1)
        print(count)

    def part2(self) -> None:
        cards:list[int] = [1]
        for index,line in enumerate(self.lines):
            if len(cards) <= index:
                cards.append(1)
            usefullpart = line.split(":")[1]
            winner_numbers,numbers = usefullpart.split("|")
            winner_numbers,numbers = set(int(x) for x in winner_numbers.split()), set(int(x) for x in numbers.split())
            good=len(winner_numbers.intersection(numbers))
            # print(index,good)
            for i in range(1,good+1):
                while len(cards) <= index+i:
                    cards.append(1)
                # print("adding",index+i,"val:",cards[index])
                cards[index+i]+=cards[index]
        # print(cards)
        print(sum(cards))

if __name__ == "__main__":
    Day04().run()