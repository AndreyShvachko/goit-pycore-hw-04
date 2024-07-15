import sys
from pathlib import Path
from colorama import init, Fore, Style


init(autoreset=True)

def print_directory_structure(path, prefix=''):
    try:
        
        if not path.is_dir():
            print(Fore.RED + "Зазначений шлях не є директорією.")
            return

        
        items = sorted(path.iterdir(), key=lambda x: x.is_file())

        for index, item in enumerate(items):
            connector = "└──" if index == len(items) - 1 else "├──"
            if item.is_dir():
                print(prefix + connector + Fore.BLUE + item.name)
                
                print_directory_structure(item, prefix + ("    " if index == len(items) - 1 else "│   "))
            else:
                print(prefix + connector + Fore.GREEN + item.name)
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python t_03.py d:/Woolf/repositories/goit-pycore-hw-04/task_03/venv/Include/t_03.py")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(Fore.RED + "Зазначений шлях не існує.")
        return

    print(Fore.YELLOW + directory_path.name)
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()
