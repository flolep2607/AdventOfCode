from utils import AOCSolution

class Day05(AOCSolution):
    def _parse_data(self):
        inputs, *blocks = self.input.split("\n\n")

        inputs = list(map(int, inputs.split(":")[1].split()))
        transformers = []
        for block in blocks:
            transformers.append([])
            for line in block.splitlines()[1:]:
                value, start, size = line.split()
                transformers[-1].append((int(value), int(start), int(size)))
        return inputs, transformers

    def part1(self) -> None:
        def transformer(x, transformers):
            for value,start,size in transformers:
                if start <= x < start + size:
                    return value + x - start
            return x

        seeds, steps = self._parse_data()
        for step in steps:
            new_values = []
            for seed in seeds:
                new_values.append(transformer(seed, step))
            seeds = new_values
        print(min(seeds))

    def part2(self) -> None:
        seeds,steps = self._parse_data()
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

        print(min(seeds)[0])

if __name__ == "__main__":
    Day05().run()
