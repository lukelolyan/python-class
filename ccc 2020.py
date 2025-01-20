

def smallest_frame(drops):
    min_x = min(drop[0] for drop in drops)
    min_y = min(drop[1] for drop in drops)
    max_x = max(drop[0] for drop in drops)
    max_y = max(drop[1] for drop in drops)
    
    return (min_x - 1, min_y - 1), (max_x + 1, max_y + 1)


n = int(input())
drops = [tuple(map(int, input().split(','))) for _ in range(n)]


bottom_left, top_right = smallest_frame(drops)


print(f"{bottom_left[0]},{bottom_left[1]}")
print(f"{top_right[0]},{top_right[1]}")

text = input().strip()
string = input().strip()

def is_cyclic_shift(text, string):
    if len(string) > len(text):
        return "no"
    doubled_string = string + string
    for i in range(len(text) - len(string) + 1):
        if text[i:i + len(string)] in doubled_string:
            return "yes"
    return "no"

print(is_cyclic_shift(text, string))

def can_escape(grid, n, m):
    from collections import deque

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        if (x, y) == (n - 1, m - 1):
            return "yes"
        if (x, y) in visited:
            continue
        visited.add((x, y))
        jump_distance = grid[x][y]

        for dx, dy in directions:
            for jump in range(1, jump_distance + 1):
                nx, ny = x + dx * jump, y + dy * jump
                if 0 <= nx < n and 0 <= ny < m:
                    queue.append((nx, ny))
                else:
                    break

    return "no"

# Input reading
n = int(input())
m = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Output result
print(can_escape(grid, n, m))
