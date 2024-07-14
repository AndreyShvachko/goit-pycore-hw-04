def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_dict = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    cats_info.append(cat_dict)
                else:
                    print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"Error reading file '{path}': {e}")
    
    return cats_info

cats_info = get_cats_info(r"D:\Woolf\repositories\goit-pycore-hw-04\task_02\cats_file.txt")
print(cats_info)

        

