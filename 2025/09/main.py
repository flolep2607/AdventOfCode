from utils import AOCSolution


class Day09(AOCSolution):
    def part1(self) -> None:
        # Parse red tile coordinates
        tiles = []
        for line in self.lines:
            x, y = map(int, line.split(","))
            tiles.append((x, y))

        # Find the largest rectangle using any two red tiles as opposite corners
        max_area = 0
        for i in range(len(tiles)):
            for j in range(i + 1, len(tiles)):
                x1, y1 = tiles[i]
                x2, y2 = tiles[j]
                # Area of rectangle with opposite corners at (x1,y1) and (x2,y2)
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                max_area = max(max_area, area)

        print(max_area)

    def part2(self) -> None:
        # Parse red tile coordinates
        tiles = []
        for line in self.lines:
            x, y = map(int, line.split(","))
            tiles.append((x, y))

        num_tiles = len(tiles)
        edges = []
        for k in range(num_tiles):
            p1 = tiles[k]
            p2 = tiles[(k + 1) % num_tiles]
            # Store edge as (x1, y1, x2, y2)
            edges.append((p1[0], p1[1], p2[0], p2[1]))

        # Pre-classify edges
        v_edges = []
        h_edges = []
        for e in edges:
            x1, y1, x2, y2 = e
            if x1 == x2:
                v_edges.append((x1, min(y1, y2), max(y1, y2)))
            else:
                h_edges.append((y1, min(x1, x2), max(x1, x2)))

        max_area = 0

        # Iterate all pairs
        for i in range(num_tiles):
            for j in range(i + 1, num_tiles):
                x1, y1 = tiles[i]
                x2, y2 = tiles[j]

                # Rectangle coordinates
                rx1, rx2 = min(x1, x2), max(x1, x2)
                ry1, ry2 = min(y1, y2), max(y1, y2)

                w = rx2 - rx1 + 1
                h = ry2 - ry1 + 1
                area = w * h

                if area <= max_area:
                    continue

                # Check 1: Does any edge cross the INTERIOR of the rectangle?
                valid_intersection = True
                for vx, vy1, vy2 in v_edges:
                    if rx1 < vx < rx2:
                        if max(ry1, vy1) < min(ry2, vy2):
                            valid_intersection = False
                            break
                if not valid_intersection:
                    continue

                for hy, hx1, hx2 in h_edges:
                    if ry1 < hy < ry2:
                        if max(rx1, hx1) < min(rx2, hx2):
                            valid_intersection = False
                            break
                if not valid_intersection:
                    continue

                # Check 2: Center Inclusion
                cx = (rx1 + rx2) / 2
                cy = (ry1 + ry2) / 2

                # Is center on boundary?
                on_boundary = False

                if (rx1 + rx2) % 2 == 0:  # cx is integer
                    for vx, vy1, vy2 in v_edges:
                        if vx == cx and vy1 <= cy <= vy2:
                            on_boundary = True
                            break

                if not on_boundary and (ry1 + ry2) % 2 == 0:  # cy is integer
                    for hy, hx1, hx2 in h_edges:
                        if hy == cy and hx1 <= cx <= hx2:
                            on_boundary = True
                            break

                if on_boundary:
                    max_area = area
                    continue

                # PIP Test (Ray casting to the right)
                count = 0
                for vx, vy1, vy2 in v_edges:
                    if vx <= cx:
                        continue
                    if vy1 <= cy < vy2:
                        count += 1

                if count % 2 == 1:
                    max_area = area

        print(max_area)


if __name__ == "__main__":
    Day09().run()
