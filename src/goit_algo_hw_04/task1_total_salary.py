# src/goit_algo_hw_04/task1_total_salary.py
from pathlib import Path
from typing import Tuple

def total_salary(path: str | Path) -> Tuple[int, float]:
    """
    Прочитати файл із зарплатами у форматі:
        Name Surname,3000
        ...
    Повернути (total, average)

    Якщо файл не існує — підняти FileNotFoundError з ясним текстом.
    Порожні або некоректні рядки пропускаються.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")

    total = 0
    count = 0

    try:
        with p.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    _, salary_str = line.split(",", maxsplit=1)
                    salary = int(salary_str)
                except ValueError:
                    # некоректний рядок — пропускаємо
                    continue
                total += salary
                count += 1
    except OSError as e:
        raise OSError(f"Failed to read file {p}: {e}") from e

    average = total / count if count else 0.0
    return total, average


if __name__ == "__main__":
    t, a = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {t}, Середня заробітна плата: {a}")
