def parse_data():
    with open("input.txt") as f:
        inputs, *blocks = f.read().split("\n\n")

    inputs = list(map(int, inputs.split(":")[1].split()))
    transformers = []
    for block in blocks:
        transformers.append([])
        for line in block.splitlines()[1:]:
            value, start, size = line.split()
            transformers[-1].append((int(value), int(start), int(size)))
    return inputs, transformers


# PART 1
def part1():
    def transformer(x, transformers):
        for value,start,size in transformers:
            if start <= x < start + size:
                return value + x - start
        return x

    seeds, steps = parse_data()
    for step in steps:
        new_values = []
        for seed in seeds:
            new_values.append(transformer(seed, step))
        seeds = new_values
    return min(seeds)


# PART 2
def part2():
    seeds,steps = parse_data()
    seeds = [
        (seeds[i], seeds[i]+seeds[i + 1])
        for i in range(0, len(seeds), 2)
    ]
    for step in steps:
        new_seeds = []
        while len(seeds)>0:
            seed_start,seed_end = seeds.pop(0)
            for value, start, size in step:
                accepted_min,accepted_max = max(seed_start,start),min(seed_end,start+size)
                if accepted_min < accepted_max:
                    new_seeds.append((accepted_min-start+value,accepted_max-start+value))
                    if accepted_min > seed_start:
                        seeds.append((seed_start,accepted_min))
                    if accepted_max < seed_end:
                        seeds.append((accepted_max,seed_end))
                    break
            else:
                new_seeds.append((seed_start,seed_end))
        seeds = new_seeds

    return min(seeds)[0]


print(part2())
