import os
import tempfile
import sys
from os.path import abspath, dirname, join

# зробити src/ видимим для імпорту
sys.path.insert(0, abspath(join(dirname(__file__), "..", "src")))

from goit_algo_hw_04.task1_total_salary import total_salary  # noqa: E402


def test_total_salary_basic():
    content = """Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
"""
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as f:
        f.write(content)
        path = f.name

    total, avg = total_salary(path)
    os.remove(path)

    assert total == 6000
    assert avg == 2000


def test_total_salary_empty_file():
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as f:
        path = f.name

    total, avg = total_salary(path)
    os.remove(path)

    assert total == 0
    assert avg == 0.0

