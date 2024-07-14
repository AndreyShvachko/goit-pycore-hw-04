def total_salary(path):
    try:
        with open (path, 'r', encoding= 'utf-8') as file:
            salaries = []
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    salaries.append(float(salary))
                except ValueError:
                    print(f"Incorrect format in line: {line}")
                    continue
                total = sum(salaries)
                average = total / len(salaries) if salaries else 0
                return total, average
   
    except FileNotFoundError:
        print(f"The file at path {path} does not exist.")
        return 0, 0
    except Exception as e:
        print(f"An error occured: {e}")
        return 0, 0

path_to_file = ("D:/Woolf/repositories/goit-pycore-hw-04/task_01/salary.txt")
total, average = total_salary(path_to_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата:{average}")
