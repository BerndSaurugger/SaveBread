# import xlrd as xl
from src.filehandler import load_input
import pytest

"""
Using pytest as a testing framework.
To locally run the tests install the dependency pytest and run
pytest
in the console from the outermost folder
"""


def test_raises_exeption_on_the_empty_folder():
    with pytest.raises(FileNotFoundError):
        load_input.get_file_path("tests/test_data/folder_with_nan")


def test_raises_value_on_to_many_files():
    with pytest.raises(ValueError):
        load_input.get_file_path("tests/test_data/folder_with_1_xlsx_and_1_csv_file")


def test_returns_1_on_folder_with_1_file():
    assert load_input.count_input_files("tests/test_data/folder_with_1_xlsx_file") == 1


def test_first_name_of_file_empty():
    data_frame = load_input.load_file("tests/test_data/folder_with_files/feature_list_blanc_fist_row.xlsx")
    counter = 0
    for i in range(len(data_frame.columns)):
        if data_frame.columns[i] == "Unnamed: {}".format(i):
            counter += 1
    assert counter == len(data_frame.columns)


def test_first_name_of_file_not_empty():
    data_frame = load_input.load_file("tests/test_data/folder_with_files/feature_list_all_correct.xlsx")
    counter = 0
    for i in range(len(data_frame.columns)):
        if data_frame.columns[i] == "Unnamed: {}".format(i):
            counter += 1
    assert counter != len(data_frame.columns)


def test_empty_dataset():
    data_frame = load_input.load_file("tests/test_data/folder_with_files/empty_dataset.xlsx")
    assert len(data_frame) == 0


def test_filled_dataset():
    data_frame = load_input.load_file("tests/test_data/folder_with_files/feature_list_all_correct.xlsx")
    assert len(data_frame) != 0


def test_missing_values():
    data_frame = load_input.load_file("tests/test_data/folder_with_files/feature_list_all_nan.xlsx")
    assert data_frame.isna().any().any()


def test_no_missing_values():
    data_frame = load_input.load_file("tests/test_data/folder_with_files/feature_list_all_correct.xlsx")
    assert not data_frame.isna().any().any()


# XLRD has removed support to read xlsx files, that's why I removed those tests. 
# They just test two implementations of the same functionality from different libraries

# def test_all_columns_correctly_read():
#     data_frame = load_input.load_file("tests/test_data/folder_with_files/feature_list_all_correct.xlsx")
#     wb = xl.open_workbook("tests/test_data/folder_with_files/feature_list_all_correct.xlsx").sheet_by_index(0)
#     wb.cell_value(0, 0)
#     assert len(data_frame.columns) == wb.ncols  # "Error while reading the columns"


# def test_all_rows_correctly_read():
#     data_frame = load_input.load_file("tests/test_data/folder_with_files/feature_list_all_correct.xlsx")
#     wb = xl.open_workbook("tests/test_data/folder_with_files/feature_list_all_correct.xlsx").sheet_by_index(0)
#     wb.cell_value(0, 0)
#     assert len(data_frame) == wb.nrows-1  # "Error while reading the rows" #care: pd.DataFrame uses 1 Row as Featurename

