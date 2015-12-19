import re
from typing import Iterable
from collections import defaultdict

regex = re.compile(r"(\w+) => (\w+)")

# PART 1
def part1():
    replacements: dict[str, str] = {}
    string = ""
    with open("input.txt") as f:
        modifiers,_,string = f.read().partition("\n\n")
        for match in regex.finditer(modifiers):
            if not replacements.get(match.group(1)):
                replacements[match.group(1)] = []
            replacements[match.group(1)].append(match.group(2))
    results = set()
    for old_value, new_values in replacements.items():
        splitted = string.split(old_value)
        for index in range(len(splitted) - 1):
            for new_value in new_values:
                results.add(
                    hash(
                        old_value.join(splitted[: index + 1])
                        + new_value
                        + old_value.join(splitted[index + 1 :])
                    )
                )
    return len(results)




# PART 2
def part2():
    with open("input.txt") as f:
        reactions, separator, element = f.read().partition("\n\n")

    reaction_dict = defaultdict(list)
    inverse_reaction_dict = {}
    for source, result in regex.findall(reactions):
        reaction_dict[source].append(result)
        inverse_reaction_dict[result] = source

    replacement_count = 0
    while element != "e":
        position_dict = {}
        for result, source in inverse_reaction_dict.items():
            length_difference = len(result) - len(source)
            if result in element:
                if source != "e" or len(element) - length_difference == 1:
                    position_dict[result] = (element.rfind(result) + len(result), length_difference)
        max_key = max(position_dict, key=position_dict.get)
        max_value = inverse_reaction_dict[max_key]
        # replace from right
        element = element[::-1].replace(max_key[::-1], max_value[::-1], 1)[::-1]
        replacement_count += 1
    return replacement_count

print(part2())