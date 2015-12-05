# PART 1
def part1():
    count:int = 0
    voewls = "aeiou"
    bad_parts=["ab","cd","pq","xy"]
    with open("input.txt", "r") as f:
        for line in f:
            count_voewls = 0
            consecutive = False
            bad = False
            for index,char in enumerate(line):
                if char in voewls:
                    count_voewls+=1
                if index>0 and char == line[index-1]:
                    consecutive = True
                if (line[index-1]+char) in bad_parts:
                    bad = True
            if count_voewls>=3 and consecutive and not bad:
                count+=1
    return count


# PART 2
def part2():
    count:int = 0
    with open("input.txt", "r") as f:
        for line in f:
            consecutive1 = False
            consecutive2 = False
            for index in range(len(line)):
                if not consecutive1:
                    for index2 in range(index+2,len(line)):
                        if line[index:index+2] == line[index2:index2+2]:
                            consecutive1=True
                            break
                if not consecutive2 and index<len(line)-2 and line[index] == line[index+2]:
                    consecutive2=True
                
            if consecutive1 and consecutive2:
                count+=1
    return count

print(part2())
