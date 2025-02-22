def total_salary(path):
    total_salary = 0
    num_developers = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    salary = int(parts[1])  
                    total_salary += salary
                    num_developers += 1
                else:
                    print(f"Пропуск невірного рядка: {line}")
        
        if num_developers > 0:
            average_salary = total_salary // num_developers
        else:
            average_salary = 0  
        
        return total_salary, average_salary
    
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Error reading file '{path}': {e}")
    
    return 0, 0 
  

path_to_file = (r"D:\Woolf\repositories\goit-pycore-hw-04\task_01\salary.txt")
total, average = total_salary(path_to_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
