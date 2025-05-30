<div dir="rtl">

# پروژه کاوشگر مریخی آستروبات
این پروژه شامل پیاده‌سازی سه مسئله الگوریتمی برای کمک به کاوشگر مریخی آستروبات است. هدف این پروژه، حل مسائل مسیر‌یابی، بهینه‌سازی نوردهی پنل‌های خورشیدی و زمان‌بندی وظایف با استفاده از الگوریتم‌های مختلف است.

## مسائل حل‌شده
1. **مسئله 1: مسیر‌یابی با BFS**
- **هدف:** یافتن کوتاه‌ترین مسیر از `(0,0)` به `(4,4)` در یک شبکه 5x5 با استفاده از الگوریتم جستجوی اول سطح (BFS).
- **ورودی:** شبکه 5x5 شامل 0 (قابل پیمایش) و 1 (صخره).
- **خروجی:**  لیست مختصات مسیر یا پیام "مسیر یافت نشد".
- **فایل:** `AI_Project_Part_1.py`

2. **مسئله 2: بهینه‌سازی نوردهی با الگوریتم ژنتیک**
- **هدف:**  انتخاب 5 جایگاه از 10 جایگاه برای قرار دادن پنل‌های خورشیدی به‌گونه‌ای که مجموع نوردهی حداکثر شود.
- **ورودی:** لیست 10 مقدار نوردهی (0 تا 10).
- **خروجی:**  رشته باینری 10 بیتی با 5 عدد 1 و مجموع نوردهی.
- **فایل:** `AI_Project_Part_2.py`

3. **مسئله 3: زمان‌بندی وظایف با CSP و Backtracking**
- **هدف:**  تخصیص 5 وظیفه به 5 بازه زمانی با رعایت محدودیت‌های توان و عدم قرارگیری وظایف با زیرسیستم یکسان در بازه‌های مجاور.
- **ورودی:**  زیرسیستم‌ها و توان موردنیاز وظایف، توان بازه‌های زمانی.
- **خروجی:**  دیکشنری تخصیص وظایف به بازه‌ها یا پیام "راه‌حل یافت نشد".
- **فایل:** `AI_Project_Part_3.py`

## پیش‌نیازها
- Python 3.11
- کتابخانه‌های موردنیاز:
    - برای مسئله 1: `collections.deque`
    - برای مسئله 2: `random`
    - برای مسئله 3: هیچ کتابخانه اضافی لازم نیست

## نحوه اجرا
1. فایل‌های پروژه (`AI_Project_Part_1.py`, `AI_Project_Part_2.py`, `AI_Project_Part_3.py`) را در یک پوشه ذخیره کنید.
2. برای اجرای هر مسئله، دستور زیر را در ترمینال اجرا کنید:
    ```bash
    python AI_Project_Part_1.py
    python AI_Project_Part_2.py
    python AI_Project_Part_3.py
    ```
3. هر فایل نمونه ورودی‌های پیش‌فرض دارد. برای استفاده از ورودی‌های دلخواه، می‌توانید بخش `main` هر فایل را تغییر دهید.

**توسعه‌دهنده**

- **نام:** امیرعلی اسماعیلی  
- **ایمیل:** [amiraliesmaeli741@gmail.com](mailto:amiraliesmaeli741@gmail.com)  
- **گیت‌هاب:** [github.com/Amirali-Esmaeli](https://github.com/Amirali-Esmaeli?tab=repositories)
</div>

# AstroBot Martian Rover Project
This project implements three algorithmic solutions to assist the AstroBot Martian rover in performing tasks to prepare Mars for human habitation. The objectives include pathfinding, optimizing solar panel placement, and task scheduling using various AI algorithms.

## Solved Problems
1. **Problem 1: Pathfinding with BFS**
- **Objective:** Find the shortest path from `(0,0)` to `(4,4)` in a 5x5 grid using Breadth-First Search (BFS).
- **Input:** A 5x5 grid with 0 (traversable) and 1 (obstacle).
- **Output:**  List of coordinates for the shortest path or "No path found".
- **File:** `AI_Project_Part_1.py`

2. **Problem 2: Solar Panel Placement Optimization with Genetic Algorithm**
- **Objective:** Select 5 out of 10 positions to place solar panels to maximize total exposure.
- **Input:** List of 10 exposure values (0 to 10).
- **Output:** A 10-bit binary string with 5 ones and the total exposure value.
- **File:** `AI_Project_Part_2.py`

3. **Problem 3: Task Scheduling with CSP and Backtracking**
- **Objective:** Assign 5 tasks (T1–T5) to 5 time slots, respecting power constraints and ensuring tasks with the same subsystem are not in adjacent slots.
- **Input:** Subsystems and power requirements for tasks, power limits for time slots.
- **Output:** Dictionary mapping tasks to time slots or "No solution found".
- **File:** `AI_Project_Part_3.py`

## Prerequisites
- Python 3.11
- Required libraries:
    - For Problem 1: `collections.deque`
    - For Problem 2: `random`
    - For Problem 3: No additional libraries required

## How to Run
1. Save the project files (`AI_Project_Part_1.py`, `AI_Project_Part_2.py`, `AI_Project_Part_3.py`)  in a directory.
2. Run each problem using:
    ```bash
    python AI_Project_Part_1.py
    python AI_Project_Part_2.py
    python AI_Project_Part_3.py
    ```
3. Each file includes default test inputs. Modify the `main` function in each file to use custom inputs.

**Developer**

- **Name**: Amirali Esmaili
- **Email**: [amiraliesmaeli741@gmail.com](mailto:amiraliesmaeli741@gmail.com)
- **GitHub**: [https://github.com/Amirali-Esmaeli](https://github.com/Amirali-Esmaeli?tab=repositories)
