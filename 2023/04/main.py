import re

regex = r"(\d+)"
#PART 1
def part1():
    count = 0
    with open("input.txt") as f:
        for line in f:
            usefullpart = line.split(":")[1]
            winner_numbers,numbers = usefullpart.split("|")
            winner_numbers,numbers = set(int(x) for x in winner_numbers.split()), set(int(x) for x in numbers.split())
            good=len(winner_numbers.intersection(numbers))
            if good>0:
                count+=2**(good-1)
    return count

# PART 2
def part2():
    cards:list[int] = [1]
    with open("input.txt") as f:
        for index,line in enumerate(f):
            if len(cards) <= index:
                cards.append(1)
            usefullpart = line.split(":")[1]
            winner_numbers,numbers = usefullpart.split("|")
            winner_numbers,numbers = set(int(x) for x in winner_numbers.split()), set(int(x) for x in numbers.split())
            good=len(winner_numbers.intersection(numbers))
            print(index,good)
            for i in range(1,good+1):
                while len(cards) <= index+i:
                    cards.append(1)
                print("adding",index+i,"val:",cards[index])
                cards[index+i]+=cards[index]
    print(cards)
    return sum(cards)

print(part2())