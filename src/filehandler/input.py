from pandas import read_excel, read_csv


def file_input(file: str):
    assert file.endswith(('.xlsx','.xls', '.csv')), "Filetype must be xlsx or csv"
    if file.endswith('.csv'):
        df_file = read_csv(file)
    else:
        df_file = read_excel(file, sheet_name=0)
    return df_file

# print(file_input("src/data/Bakery.csv "))