from collections import deque

def validate_grid(grid):
    # بررسی اندازه شبکه
    if not grid or len(grid) != 5 or any(len(row) != 5 for row in grid):
        return False
    # بررسی مقادیر 0 و 1
    for row in grid:
        for cell in row:
            if cell not in (0,1):
                return False
    # بررسی قابل پیمایش بودن نقاط شروع و پایان
    if grid[0][0] != 0 or grid[4][4] != 0:
        return False
    return True

def bfs_shortest_path(grid):
    if not validate_grid(grid):
        return "مسیر یافت نشد"
    
    # جهت‌های حرکت: بالا، پایین، چپ، راست
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start, end = (0, 0), (4, 4)

    # صف برای BFS
    queue = deque([start])
    # دیکشنری برای ذخیره والدین هر نقطه
    parent = {start: None}
    # مجموعه نقاط بازدیدشده
    visited = {start}

    while queue:
        current = queue.popleft()
        if current == end:
            return reconstruct_path(parent, end)
        
        # بررسی همسایه‌ها
        for dx, dy in directions:
            next_pos = (current[0] + dx, current[1] + dy)
            # بررسی معتبر بودن مختصات
            if (0 <= next_pos[0] < 5 and 0 <= next_pos[1] < 5 and
                next_pos not in visited and grid[next_pos[0]][next_pos[1]] == 0):
                queue.append(next_pos)
                visited.add(next_pos)
                parent[next_pos] = current
    
    return "مسیر یافت نشد"

def reconstruct_path(parent, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    return path[::-1]  # مسیر را از ابتدا به انتها برمی‌گردانیم

def main():
    # شبکه نمونه
    grid = [
        [0, 0, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
        [1, 1, 0, 0, 0]
    ]
    
    result = bfs_shortest_path(grid)
    print(result)

if __name__ == "__main__":
    main()

# خروجی
[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]