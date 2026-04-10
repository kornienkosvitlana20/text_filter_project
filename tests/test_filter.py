import pytest
from src.filter import read_file, filter_lines, write_file


@pytest.fixture
def sample_lines():
    return [
        "hello world\n",
        "python is cool\n",
        "hello python\n"
    ]


@pytest.mark.parametrize("keyword, expected", [
    ("hello", ["hello world\n", "hello python\n"]),
    ("python", ["python is cool\n", "hello python\n"]),
    ("none", [])
])
def test_filter_lines(sample_lines, keyword, expected):
    assert filter_lines(sample_lines, keyword) == expected


def test_write_and_read(tmp_path):
    file = tmp_path / "test.txt"
    data = ["a\n", "b\n"]

    write_file(file, data)
    assert read_file(file) == data