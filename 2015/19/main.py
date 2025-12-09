from utils import AOCSolution
import re
from collections import defaultdict

class Day19(AOCSolution):
    def part1(self) -> None:
        regex = re.compile(r"(\w+) => (\w+)")
        replacements: dict[str, str] = {}
        
        modifiers,_,string = self.input.partition("\n\n")
        # self.input contains the full text
        
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
        print(len(results))

    def part2(self) -> None:
        regex = re.compile(r"(\w+) => (\w+)")
        reactions, separator, element = self.input.partition("\n\n")
        # Note: 'element' here is the target molecule from input
        
        # Original code used `regex.findall(reactions)`.
        
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
        print(replacement_count)

if __name__ == "__main__":
    Day19().run()