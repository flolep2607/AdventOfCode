#PART 1
def part1():
    with open("input.txt", "r") as f:
        steps,_,*mape = f.read().splitlines()
    network = {}
    START="AAA"
    for line in mape:
        start,next = line.split(" = ")
        network[start] = next[1:-1].split(", ")
    index = 0
    while START != "ZZZ":
        for index,step in enumerate(steps,index+1):
            if step =="R":
                START = network[START][1]
            else:
                START = network[START][0]
            if START == "ZZZ":
                break
    print(network)
    return index
# PART 2
def part2():
    with open("input.txt", "r") as f:
        steps,_,*mape = f.read().splitlines()
    network = {}
    for line in mape:
        start,next = line.split(" = ")
        network[start] = next[1:-1].split(", ")
    STARTS=[point for point in network.keys() if point.endswith("A")]
    print("STARTS",STARTS)
    index = 0
    while not all([START.endswith("Z") for START in STARTS]):
        for index,step in enumerate(steps,index+1):
            for ghost in range(len(STARTS)):
                if step =="R":
                    STARTS[ghost] = network[STARTS[ghost]][1]
                else:
                    STARTS[ghost] = network[STARTS[ghost]][0]
            if all([START.endswith("Z") for START in STARTS]):
                break
    print(network)
    return index

print(part2())