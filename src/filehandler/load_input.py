from pandas import read_excel, read_csv
import os


def count_input_files(directory="src/data"):
    """
    Name the directory where you want to read the file as input
    """
    list_of_files = os.listdir(directory)
    counter = 0
    for file in list_of_files:
        if file.endswith(('.xlsx', '.xls', '.csv')) and file != "savebread_output.xlsx":
            counter += 1
    return counter


def get_file_path(directory="src/data"):
    """
    Automatically generates the filepath of the saved file
    """
    file_amount = count_input_files(directory)
    if file_amount == 0:
        raise FileNotFoundError("File not correctly uploaded!")
    if file_amount > 1:
        raise ValueError("You have provided {} files, but there is only one alowed".format(file_amount))

    list_of_data = os.listdir(directory)
    for i in range(len(list_of_data)):
        if list_of_data[i].endswith(('.xlsx', '.xls', '.csv')) and list_of_data[i] != "savebread_output.xlsx":
            file_name = list_of_data[i]
    file_path = "src/data/" + str(file_name)
    return file_path


def load_file(file_path: str = get_file_path, seperator=","):
    """
    Please provide a dataset from type xlsx, xls or csv and make sure the first row name your colomns
    """
    # assert file type and load data
    assert file_path.endswith(('.xlsx', '.xls', '.csv')), "Filetype must be xlsx or csv"
    if file_path.endswith('.csv'):
        df_file = read_csv(file_path, sep=seperator)
    else:
        df_file = read_excel(file_path, sheet_name=0)

    return df_file


# if df_file.columns[i] == "Unnamed: {}".format(i):
def count_columns_in_df(data_frame=load_file):
    """
    Name the directory where you want to read the file as input
    """
    col_counter = 0
    for columnname in data_frame.columns:
        col_counter += 1
    return col_counter
