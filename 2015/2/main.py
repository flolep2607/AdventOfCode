# PART 1
def part1():
    count:int = 0
    with open("input.txt", "r") as f:
        for line in f:
            w,h,l = [int(i) for i in line.split('x')]
            surface = 2*w*l + 2*l*h + 2*h*w
            slack = min(w*l, l*h, h*w)
            count += surface + slack
    return count


# PART 2
def part2():
    count:int = 0
    with open("input.txt", "r") as f:
        for line in f:
            w,h,l = [int(i) for i in line.split('x')]
            wrap = w*h*l
            bow = min(2*w+2*h, 2*l+2*h, 2*w+2*l)
            count += wrap + bow
    return count

print(part2())
