from utils import AOCSolution
from hashlib import md5

class Day04(AOCSolution):
    def part1(self) -> None:
        input_str = "ckczppom"
        count:int = 0
        while not md5((input_str+str(count)).encode()).hexdigest().startswith("0"*5):
            count += 1
        print(count)

    def part2(self) -> None:
        input_str = "ckczppom"
        count:int = 0
        while not md5((input_str+str(count)).encode()).hexdigest().startswith("0"*6):
            count += 1
        print(count)

if __name__ == "__main__":
    Day04().run()
