# src/goit_algo_hw_04/task2_cats_info.py
from pathlib import Path
from typing import List, Dict

def get_cats_info(path: str | Path) -> List[Dict[str, str]]:
    """
    Прочитати файл у форматі:
        <id>,<name>,<age>
    Повернути список словників з ключами: id, name, age (рядки).
    Некоректні рядки пропускаються. Якщо файл не існує — FileNotFoundError.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")

    cats: List[Dict[str, str]] = []

    try:
        with p.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 3:
                    continue
                cat_id, name, age = (s.strip() for s in parts)
                cats.append({"id": cat_id, "name": name, "age": age})
    except OSError as e:
        raise OSError(f"Failed to read file {p}: {e}") from e

    return cats


if __name__ == "__main__":
    info = get_cats_info("cats_file.txt")
    print(info)
