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