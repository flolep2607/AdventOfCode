from utils import AOCSolution
import re

class Day03(AOCSolution):
    def part1(self) -> None:
        regex = r"(\d+)"
        count = 0
        values:dict[list[dict[str,int]]] = {}
        def adjacent(x_mid,y_mid,values):
            # print(x_mid,y_mid)
            adjacent_values=[]
            for x in range(x_mid-1,x_mid+2):
                for y in range(y_mid-1,y_mid+2):
                    if x == x_mid and y == y_mid:
                        continue
                    if values.get(y):
                        # temp_values = values[y].copy()
                        # need to remove the value from values when append to adjacent_values
                        for value in values[y]:
                            if value["x_start"] <= x <= value["x_end"]:
                                adjacent_values.append(value["value"])
                                values[y].remove(value)
                        # values[y] = temp_values
            # print(adjacent_values)
            return adjacent_values
        
        # First Pass
        for y,line in enumerate(self.lines):
            line = line.strip()
            values[y] = []
            matches = re.finditer(regex, line, re.MULTILINE)
            for match in matches:
                values[y].append({
                    "value": int(match.group()),
                    "x_start": match.start(),
                    "x_end": match.end()-1,
                    "y": y
                })
        
        # Second Pass
        for y,line in enumerate(self.lines):
            line = line.strip()
            for x,char in enumerate(line):
                if char not in ".0123456789":
                    count+=sum(adjacent(x,y,values))
        print(count)

    def part2(self) -> None:
        regex = r"(\d+)"
        count = 0
        values:dict[list[dict[str,int]]] = {}
        def adjacent(x_mid,y_mid,values):
            # print(x_mid,y_mid)
            adjacent_values=[]
            for x in range(x_mid-1,x_mid+2):
                for y in range(y_mid-1,y_mid+2):
                    if x == x_mid and y == y_mid:
                        continue
                    if values.get(y):
                        # temp_values = values[y].copy()
                        # need to remove the value from values when append to adjacent_values
                        for value in values[y]:
                            if value["x_start"] <= x <= value["x_end"]:
                                adjacent_values.append(value["value"])
                                values[y].remove(value)
                        # values[y] = temp_values
            # print(adjacent_values)
            return adjacent_values
            
        # First Pass
        for y,line in enumerate(self.lines):
            line = line.strip()
            values[y] = []
            matches = re.finditer(regex, line, re.MULTILINE)
            for match in matches:
                values[y].append({
                    "value": int(match.group()),
                    "x_start": match.start(),
                    "x_end": match.end()-1,
                    "y": y
                })
        
        # Second Pass
        for y,line in enumerate(self.lines):
            line = line.strip()
            for x,char in enumerate(line):
                if char not in ".0123456789":
                    adj = adjacent(x,y,values)
                    if char == "*" and len(adj)==2:
                        # print("x",adj[0],adj[1])
                        count += adj[0]*adj[1]
        print(count)

if __name__ == "__main__":
    Day03().run()