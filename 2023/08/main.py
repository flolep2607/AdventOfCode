from utils import AOCSolution

class Day08(AOCSolution):
    def part1(self) -> None:
        # self.lines already splits by lines
        steps = self.lines[0]
        # self.lines[1] is empty string if file has newline, or self.input.splitlines() behavior?
        # original used f.read().splitlines().
        # self.lines = self.input.split("\n") in base.py.
        # So yes, lines[1] is likely empty.
        mape = self.lines[2:]
        # Note: mapping might have empty lines at end? base.py strips input.
        
        network = {}
        START="AAA"
        for line in mape:
            if not line: continue
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
        # print(network)
        print(index)

    def part2(self) -> None:
        steps = self.lines[0]
        mape = self.lines[2:]
        network = {}
        for line in mape:
            if not line: continue
            start,next = line.split(" = ")
            network[start] = next[1:-1].split(", ")
        STARTS=[point for point in network.keys() if point.endswith("A")]
        # print("STARTS",STARTS)
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
        # print(network)
        print(index)

if __name__ == "__main__":
    Day08().run()