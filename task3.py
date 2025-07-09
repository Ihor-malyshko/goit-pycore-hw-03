import sys
from pathlib import Path
from colorama import init, Fore

init()

def display_directory_structure(path, prefix=""):
    try:
        # список елементів
        items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
       
        for i, item in enumerate(items):
            space = "    "
            new_prefix = prefix + "    │"

            if item.is_dir():
                print(f"{prefix}{space}{Fore.BLUE}{item.name}/{Fore.RESET}")
                
                # pекурсія для піддиректорій
                item_path = Path(item)
                display_directory_structure(item_path, new_prefix)
            else:
                print(f"{prefix}{space}{Fore.GREEN}{item.name}{Fore.RESET}")
    
    except Exception as e:
        print(f"{prefix}{Fore.RED}Сталася помилка:{Fore.RESET} {e}")


# run task
directory_path = sys.argv[1]
path = Path(directory_path)
if not path.exists():
    print(f"{Fore.RED}Помилка:{Fore.RESET} '{directory_path}' не існує.")
    sys.exit(1)
    
print(f"{Fore.BLUE}{path.name}/{Fore.RESET}")
display_directory_structure(path)

