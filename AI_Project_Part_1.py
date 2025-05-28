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
