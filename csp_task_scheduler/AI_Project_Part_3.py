# تعریف وظایف و محدودیت‌ها
tasks = {
    'T1': {'subsystem': 'Navigation', 'power': 5},
    'T2': {'subsystem': 'Sampling', 'power': 4},
    'T3': {'subsystem': 'Communication', 'power': 6},
    'T4': {'subsystem': 'Navigation', 'power': 7},
    'T5': {'subsystem': 'Sampling', 'power': 3}
}
time_slot_powers = [10, 8, 12, 6, 10]  # توان هر بازه زمانی

def is_valid_assignment(assignment, task, time_slot):
    # بررسی محدودیت توان
    if tasks[task]['power'] > time_slot_powers[time_slot - 1]:
        return False
    
    # بررسی محدودیت زیرسیستم در بازه‌های مجاور
    for t, slot in assignment.items():
        if abs(slot - time_slot) == 1:
            if tasks[t]['subsystem'] == tasks[task]['subsystem']:
                return False
    return True

def csp_backtracking(assignment, tasks_list):
    if len(assignment) == len(tasks_list):  # همه وظایف تخصیص داده شده‌اند
        return assignment
    
    task = tasks_list[len(assignment)]  # وظیفه بعدی
    for time_slot in range(1, 6):  # بازه‌های زمانی 1 تا 5
        if time_slot not in assignment.values():  # بازه استفاده‌نشده
            if is_valid_assignment(assignment, task, time_slot):
                assignment[task] = time_slot
                result = csp_backtracking(assignment.copy(), tasks_list)
                if result:
                    return result
    return None

def schedule_tasks():
    tasks_list = ['T1', 'T2', 'T3', 'T4', 'T5']
    assignment = csp_backtracking({}, tasks_list)
    if assignment:
        return assignment
    return "راه‌حل یافت نشد"

def main():
    result = schedule_tasks()
    print(result)

if __name__ == "__main__":
    main()

# خروجی
# {'T1': 1, 'T2': 2, 'T3': 3, 'T4': 5, 'T5': 4}