# PART 1
def part1():
    values: dict[str,int]= {}
    cables: dict[str,str]= {}
    def worker(target:str):
        if target.isdigit():
            return int(target)
        if target in values:
            return values[target]
        
        operation=cables[target]
        if operation.isdigit():
            return int(operation)
        elif "NOT" in operation:
            value = (~worker(operation[4:]))& 0xFFFF
        elif "AND" in operation:
            a,b = operation.split(" AND ")
            value = worker(a) & worker(b)
        elif "OR" in operation:
            a,b = operation.split(" OR ")
            value = worker(a) | worker(b)
        elif "LSHIFT" in operation:
            a,b = operation.split(" LSHIFT ")
            value = worker(a) << worker(b)
        elif "RSHIFT" in operation:
            a,b = operation.split(" RSHIFT ")
            value = (worker(a) >> worker(b)) & 0xFFFF
        else:
            value = worker(operation)
        values[target] = value
        return value
        
    with open("input.txt", "r") as f:
        for line in f:
            if line:
                operation,to = line.split(" -> ")
                cables[to.strip()] = operation.strip()
    return worker("a")


# PART 2
def part2():
    values: dict[str,int]= {}
    cables: dict[str,str]= {}
    def worker(target:str):
        if target.isdigit():
            return int(target)
        if target in values:
            return values[target]
        
        operation=cables[target]
        if operation.isdigit():
            return int(operation)
        elif "NOT" in operation:
            value = (~worker(operation[4:]))& 0xFFFF
        elif "AND" in operation:
            a,b = operation.split(" AND ")
            value = worker(a) & worker(b)
        elif "OR" in operation:
            a,b = operation.split(" OR ")
            value = worker(a) | worker(b)
        elif "LSHIFT" in operation:
            a,b = operation.split(" LSHIFT ")
            value = worker(a) << worker(b)
        elif "RSHIFT" in operation:
            a,b = operation.split(" RSHIFT ")
            value = (worker(a) >> worker(b)) & 0xFFFF
        else:
            value = worker(operation)
        values[target] = value
        return value
        
    with open("input.txt", "r") as f:
        for line in f:
            if line:
                operation,to = line.split(" -> ")
                cables[to.strip()] = operation.strip()
    values={"b":worker("a")}
    return worker("a")

print(part2())
