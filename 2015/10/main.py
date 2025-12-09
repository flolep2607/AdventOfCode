from utils import AOCSolution

class Day10(AOCSolution):
    def part1(self) -> None:
        input_str = "1113222113"
        data=list(map(int,input_str))
        for _ in range(40):
            new_data = []
            i = 0
            while i < len(data):
                count = 1
                while i+1 < len(data) and data[i] == data[i+1]:
                    count += 1
                    i += 1
                new_data.append(count)
                new_data.append(data[i])
                i += 1
            data = new_data
        print(len(data))

    def part2(self) -> None:
        input_str = "1113222113"
        data=list(map(int,input_str))
        for _ in range(50):
            new_data = []
            i = 0
            while i < len(data):
                count = 1
                while i+1 < len(data) and data[i] == data[i+1]:
                    count += 1
                    i += 1
                new_data.append(count)
                new_data.append(data[i])
                i += 1
            data = new_data
        print(len(data))

if __name__ == "__main__":
    Day10().run()
