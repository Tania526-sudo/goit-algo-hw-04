# src/goit_algo_hw_04/task3_tree_view.py
import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_tree(root: Path, prefix: str = "") -> None:
    """
    Рекурсивно друкує дерево директорій.
    Папки — синім, файли — звичайним кольором.
    """
    try:
        entries = sorted(root.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    except PermissionError:
        print(prefix + Fore.RED + "[permission denied]" + Style.RESET_ALL)
        return

    last_index = len(entries) - 1
    for i, entry in enumerate(entries):
        connector = "└── " if i == last_index else "├── "
        if entry.is_dir():
            print(prefix + connector + Fore.BLUE + entry.name + "/" + Style.RESET_ALL)
            next_prefix = prefix + ("    " if i == last_index else "│   ")
            print_tree(entry, next_prefix)
        else:
            print(prefix + connector + entry.name)

def main() -> None:
    init(autoreset=True)
    if len(sys.argv) < 2:
        print("Usage: python -m goit_algo_hw_04.task3_tree_view <path>")
        sys.exit(1)

    target = Path(sys.argv[1])
    if not target.exists():
        print(f"Error: path does not exist: {target}")
        sys.exit(1)
    if not target.is_dir():
        print(f"Error: not a directory: {target}")
        sys.exit(1)

    print(Fore.CYAN + f"Tree for: {target.resolve()}" + Style.RESET_ALL)
    print(Fore.BLUE + target.name + "/" + Style.RESET_ALL)
    print_tree(target)

if __name__ == "__main__":
    main()
