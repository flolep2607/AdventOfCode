from utils import AOCSolution

class Day07(AOCSolution):
    def part1(self) -> None:
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
            
        for line in self.lines:
            if line:
                operation,to = line.split(" -> ")
                cables[to.strip()] = operation.strip()
        print(worker("a"))

    def part2(self) -> None:
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
            
        for line in self.lines:
            if line:
                operation,to = line.split(" -> ")
                cables[to.strip()] = operation.strip()
        
        # We need to run worker("a") first, then reset values with 'b' overridden.
        
        # Original logic:
        # values={"b":worker("a")}
        # return worker("a")
        
        # The first worker("a") computes the signal for a.
        a_signal = worker("a")
        
        # Reset values for the second run
        values.clear() 
        # Actually original code did `values={"b":worker("a")}` which effectively clears other values because it creates a NEW dict.
        # But here `values` is in the scope of `part2`.
        # If I do `values = ...` inside `part2`, `worker` (which closes over `values`) will see the new object?
        
        # In Python:
        # def outer():
        #   x = {}
        #   def inner(): return x
        #   x = {'a':1}
        #   return inner()
        # Returns {'a':1}. Yes.
        
        values = {"b": a_signal} # Rebind values to a new dict
        
        # However, `worker` refers to `values`. The `worker` function defined above closes over the variable `values`.
        # But if I assign `values = ...`, does `worker` see it?
        # Yes, because `worker` looks up `values` in local scope of `part2` when executed.
        
        # BUT WAIT.
        # In `part2` defined above, I need `nonlocal values` if I were to assign to it inside `worker`, but I am only reading it or mutating it.
        # But assigning to `values` in `part2` itself is just changing the local variable `values`. `worker` will see the change.
        
        # To be absolutely safe and clear, I'll use `values.clear(); values['b'] = a_signal`.
        # But wait, the original code did `values={"b":worker("a")}`. And `worker` was modifying `values`.
        
        # Let's check original code `2015/07/main.py`:
        # def part2():
        #     values = {}
        #     def worker(...): ... uses values ...
        #     ... parsing ...
        #     values={"b":worker("a")}
        #     return worker("a")
        
        # This relies on `worker` using the `values` variable from the closure.
        # It works.
        
        # My implementation:
        # I just won't re-define `worker` if I don't have to, but here I am defining it inside `part2`.
        # I cannot easily reassign `values` without `nonlocal` keyword if `worker` was modifying it (it is modifying it).
        # Wait, `worker` does `values[target] = value`. This mutates the object.
        # If I do `values = ...`, I verify that `worker` sees the new object.
        
        # Actually, simpler approach to replicate "Take the signal you got on wire a, override wire b to that signal, and reset the other wires":
        
        first_a = worker("a")
        values.clear()
        values["b"] = first_a
        print(worker("a"))

if __name__ == "__main__":
    Day07().run()
