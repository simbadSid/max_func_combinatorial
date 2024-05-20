import pytest

from src.main.s_max import Smax
from src.utils.utils import FileParser


@pytest.fixture
def s_max() -> Smax:
    return Smax()

INPUT_TEST_FILE     = 'tests/input/non_regression/test{0}.in'
OUTPUT_TEST_FILE    = 'tests/output/non_regression/test{0}.out'

@pytest.mark.parametrize("input_file,output_file", [
    (INPUT_TEST_FILE.format(1), OUTPUT_TEST_FILE.format(1)),
    (INPUT_TEST_FILE.format(2), OUTPUT_TEST_FILE.format(2)),
    (INPUT_TEST_FILE.format(3), OUTPUT_TEST_FILE.format(3)),
    (INPUT_TEST_FILE.format(4), OUTPUT_TEST_FILE.format(4)),
    (INPUT_TEST_FILE.format(5), OUTPUT_TEST_FILE.format(5)),
    (INPUT_TEST_FILE.format(6), OUTPUT_TEST_FILE.format(6)),
    (INPUT_TEST_FILE.format(7), OUTPUT_TEST_FILE.format(7)),
    (INPUT_TEST_FILE.format(8), OUTPUT_TEST_FILE.format(8)),
    (INPUT_TEST_FILE.format(9), OUTPUT_TEST_FILE.format(9)),
    (INPUT_TEST_FILE.format(10), OUTPUT_TEST_FILE.format(10)),
    (INPUT_TEST_FILE.format(11), OUTPUT_TEST_FILE.format(11)),
    (INPUT_TEST_FILE.format(12), OUTPUT_TEST_FILE.format(12)),
    (INPUT_TEST_FILE.format(13), OUTPUT_TEST_FILE.format(13)),
    (INPUT_TEST_FILE.format(14), OUTPUT_TEST_FILE.format(14)),
    (INPUT_TEST_FILE.format(15), OUTPUT_TEST_FILE.format(15)),
    (INPUT_TEST_FILE.format(16), OUTPUT_TEST_FILE.format(16)),
    (INPUT_TEST_FILE.format(17), OUTPUT_TEST_FILE.format(17)),
])
def test_algo(s_max: Smax, input_file: str, output_file: str):
    s_max.parse_input(file_relative_path=input_file)
    result = s_max.find_max()
    expected_result = int(FileParser(file_relative_path=output_file).next_line())

    assert result == expected_result
