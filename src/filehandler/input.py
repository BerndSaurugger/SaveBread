from pandas import read_excel


def file_input(file: str):
    assert file.endswith(('.xlsx','.xls')), "Filetype must be xlsx"
    df_file = read_excel(file, sheet_name=0)
    return df_file

print(file_input("src/data/feature_list.xlsx"))