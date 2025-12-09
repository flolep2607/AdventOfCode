from utils import AOCSolution
import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return True
        return False

class Day08(AOCSolution):
    def parse_input(self):
        points = []
        for line in self.lines:
            line = line.strip()
            if line:
                parts = line.split(',')
                points.append(tuple(map(int, parts)))
        return points

    def dist_sq(self, p1, p2):
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2

    def part1(self) -> None:
        points = self.parse_input()
        n = len(points)
        
        # Generate all pairs and calculate squared distances
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                d = self.dist_sq(points[i], points[j])
                edges.append((d, i, j))
        
        # Sort edges by distance (smallest first)
        edges.sort(key=lambda x: x[0])
        
        uf = UnionFind(n)
        
        # Process the top 1000 pairs
        limit = 1000
        if len(edges) < limit:
            limit = len(edges)
            
        for k in range(limit):
            _, u, v = edges[k]
            uf.union(u, v)
            
        # Get sizes of all components
        root_sizes = []
        for i in range(n):
            if uf.parent[i] == i:
                root_sizes.append(uf.size[i])
                
        # Sort sizes descending
        root_sizes.sort(reverse=True)
        
        # Multiply the three largest
        if len(root_sizes) >= 3:
            ans = root_sizes[0] * root_sizes[1] * root_sizes[2]
            print(ans)
        else:
            print(f"Not enough circuits: {len(root_sizes)}")
            ans = 1
            for s in root_sizes:
                ans *= s
            print(ans)

    def part2(self) -> None:
        points = self.parse_input()
        n = len(points)
        
        # Generate all pairs and calculate squared distances
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                d = self.dist_sq(points[i], points[j])
                edges.append((d, i, j))
        
        # Sort edges by distance (smallest first)
        edges.sort(key=lambda x: x[0])
        
        uf = UnionFind(n)
        
        # Keep connecting until we have 1 circuit (n-1 unions needed)
        unions_made = 0
        last_pair = None
        
        for d, u, v in edges:
            if uf.union(u, v):
                unions_made += 1
                last_pair = (u, v)
                if unions_made == n - 1:
                    # All connected!
                    break
        
        if last_pair:
            u, v = last_pair
            x1 = points[u][0]
            x2 = points[v][0]
            print(f"Last connection: {points[u]} and {points[v]}")
            print(f"X coordinates: {x1} * {x2} = {x1 * x2}")
            print(x1 * x2)
        else:
            print("Error: Could not connect all boxes")

if __name__ == '__main__':
    Day08().run()
