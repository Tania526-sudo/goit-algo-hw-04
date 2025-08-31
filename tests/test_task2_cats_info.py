import os
import tempfile
import sys
import pytest
from os.path import abspath, dirname, join


sys.path.insert(0, abspath(join(dirname(__file__), "..", "src")))

from goit_algo_hw_04.task2_cats_info import get_cats_info  


def test_get_cats_info_basic():
    content = """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
"""
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as f:
        f.write(content)
        path = f.name

    cats = get_cats_info(path)
    os.remove(path)

    assert cats == [
        {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
        {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
        {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    ]


def test_get_cats_info_with_invalid_line():
    content = """60b90c1c13067a15887e1ae1,Tayson,3
INVALID_LINE
60b90c2e13067a15887e1ae3,Barsik,2
"""
    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as f:
        f.write(content)
        path = f.name

    cats = get_cats_info(path)
    os.remove(path)

    
    assert cats == [
        {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
        {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    ]


def test_get_cats_info_file_not_found():
    with pytest.raises(FileNotFoundError):
        get_cats_info("definitely_missing_file.txt")

