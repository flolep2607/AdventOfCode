from utils import AOCSolution

class Day06(AOCSolution):
    def part1(self) -> None:
        lines = self.lines
        
        # Parse each column position
        # Numbers are in lines 0-3, operators are in line 4
        num_lines = lines[:4]
        op_line = lines[4]
        
        # Find the maximum line length
        max_len = max(len(line) for line in num_lines + [op_line])
        
        # Pad all lines to the same length
        num_lines = [line.ljust(max_len) for line in num_lines]
        op_line = op_line.ljust(max_len)
        
        # Parse problems column by column
        problems = []
        current_problem_numbers = [[] for _ in range(4)]  # 4 rows of number strings
        current_op = None
        in_problem = False
        
        col = 0
        while col < max_len:
            # Check if this column has any content
            column_chars = [num_lines[i][col] for i in range(4)]
            op_char = op_line[col]
            
            is_space_column = all(c == ' ' for c in column_chars) and op_char == ' '
            
            if is_space_column:
                if in_problem:
                    # End of a problem - process the collected numbers
                    numbers = []
                    for row in range(4):
                        num_str = ''.join(current_problem_numbers[row]).strip()
                        if num_str:
                            numbers.append(int(num_str))
                    
                    if numbers and current_op:
                        problems.append((numbers, current_op))
                    
                    # Reset for next problem
                    current_problem_numbers = [[] for _ in range(4)]
                    current_op = None
                    in_problem = False
            else:
                in_problem = True
                # Collect characters for this column
                for row in range(4):
                    current_problem_numbers[row].append(column_chars[row])
                
                if op_char in ['+', '*']:
                    current_op = op_char
            
            col += 1
        
        # Process the last problem if any
        if in_problem:
            numbers = []
            for row in range(4):
                num_str = ''.join(current_problem_numbers[row]).strip()
                if num_str:
                    numbers.append(int(num_str))
            
            if numbers and current_op:
                problems.append((numbers, current_op))
        
        # Calculate the grand total
        grand_total = 0
        for numbers, op in problems:
            if op == '+':
                result = sum(numbers)
            elif op == '*':
                result = 1
                for n in numbers:
                    result *= n
            grand_total += result
        
        print(f"Part 1: {grand_total}")

    def part2(self) -> None:
        lines = self.lines
        
        # Numbers are in lines 0-3, operators are in line 4
        num_lines = lines[:4]
        op_line = lines[4]
        
        # Find the maximum line length
        max_len = max(len(line) for line in num_lines + [op_line])
        
        # Pad all lines to the same length
        num_lines = [line.ljust(max_len) for line in num_lines]
        op_line = op_line.ljust(max_len)
        
        # Parse problems column by column, RIGHT TO LEFT
        problems = []
        current_problem_numbers = []  # List of numbers for current problem
        current_op = None
        in_problem = False
        
        # Process from right to left
        col = max_len - 1
        while col >= 0:
            # Check if this column has any content
            column_chars = [num_lines[i][col] for i in range(4)]
            op_char = op_line[col]
            
            is_space_column = all(c == ' ' for c in column_chars) and op_char == ' '
            
            if is_space_column:
                if in_problem:
                    # End of a problem - we have collected all numbers
                    if current_problem_numbers and current_op:
                        problems.append((current_problem_numbers, current_op))
                    
                    # Reset for next problem
                    current_problem_numbers = []
                    current_op = None
                    in_problem = False
            else:
                in_problem = True
                
                # Read the number vertically from this column
                # Top to bottom = most significant to least significant
                num_str = ''
                for row in range(4):
                    c = column_chars[row]
                    if c.isdigit():
                        num_str += c
                
                if num_str:
                    current_problem_numbers.append(int(num_str))
                
                if op_char in ['+', '*']:
                    current_op = op_char
            
            col -= 1
        
        # Process the last problem if any
        if in_problem:
            if current_problem_numbers and current_op:
                problems.append((current_problem_numbers, current_op))
        
        # Calculate the grand total
        grand_total = 0
        for numbers, op in problems:
            if op == '+':
                result = sum(numbers)
            elif op == '*':
                result = 1
                for n in numbers:
                    result *= n
            grand_total += result
        
        print(f"Part 2: {grand_total}")

if __name__ == '__main__':
    Day06().run()
