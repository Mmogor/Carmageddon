import heapq
from typing import Tuple, List, Dict


def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Calculates the Manhattan distance between two points a and b."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(start: Tuple[int, int], goal: Tuple[int, int], grid: List[List[int]]) -> List[Tuple[int, int]]:
    """Implements the A* algorithm to find the shortest path from start to goal on a grid."""
    print("astar begin", start, goal)
    print(grid)
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}
    g_score: Dict[Tuple[int, int], int] = {start: 0}
    f_score: Dict[Tuple[int, int], int] = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        # Debug: Current node
        print(f"Current node: {current}")

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current, grid):
            print(neighbor)
            tentative_g_score = g_score[current] + 1

            # Debug: Neighbor and scores
            print(
                f"Checking neighbor: {neighbor}, g_score: {tentative_g_score}, f_score: {f_score.get(neighbor, float('inf'))}")

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

                    # Debug: Added to open set
                    print(f"Added to open set: {neighbor}, f_score: {f_score[neighbor]}")

    # Debug: No path found
    print("No path found.")
    return []  # Return an empty path if there is no path


def reconstruct_path(came_from: Dict[Tuple[int, int], Tuple[int, int]], current: Tuple[int, int]) -> List[
    Tuple[int, int]]:
    """Reconstructs the path from start to goal using the came_from dictionary."""
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)

        # Debug: Path reconstruction
        print(f"Reconstructing path: {current}")

    return total_path[::-1]


def get_neighbors(pos: Tuple[int, int], grid: List[List[int]]) -> List[Tuple[int, int]]:
    """Finds the valid neighbors of a given position on the grid."""
    neighbors = []
    x, y = pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right

    for dx, dy in directions:
        print(dx, dy)
        nx, ny = x + dx, y + dy
        print(0 <= ny < len(grid))
        print(0 <= nx < len(grid[0]))
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
            print(grid[ny][nx] != 1)
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] != 1:
                neighbors.append((nx, ny))

                # Debug: Neighbor added
                print(f"Valid neighbor: {nx, ny}")

    return neighbors
