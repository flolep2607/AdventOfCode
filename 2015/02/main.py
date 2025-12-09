from utils import AOCSolution

class Day02(AOCSolution):
    def part1(self) -> None:
        count:int = 0
        for line in self.lines:
            w,h,l = [int(i) for i in line.split('x')]
            surface = 2*w*l + 2*l*h + 2*h*w
            slack = min(w*l, l*h, h*w)
            count += surface + slack
        print(count)

    def part2(self) -> None:
        count:int = 0
        for line in self.lines:
            w,h,l = [int(i) for i in line.split('x')]
            wrap = w*h*l
            bow = min(2*w+2*h, 2*l+2*h, 2*w+2*l)
            count += wrap + bow
        print(count)

if __name__ == "__main__":
    Day02().run()
