from pandas import read_csv
from sklearn.pipeline import Pipeline

# from preprocessing.preprocessing import preprocess_datasets
from preprocessing.pipeline_functions import Preprocess_Sales
from preprocessing.pipeline_functions import Preprocess_Merge_Weather
from preprocessing.pipeline_functions import Preprocess_Merge_Holidays
# from preprocessing.pipeline_functions import export_df_to_csv

sales = read_csv("src/data/Bakery_Sales.csv")
weather = read_csv("src/data/Seoul_weather.csv", sep=";")
holidays = read_csv("src/data/public_holidays.csv", sep=";")


def get_preprocessing_pipeline():
    preprocessing_pipeline = Pipeline(steps=[("preprocess_Maindataset", Preprocess_Sales()),
                                             ("preprocess+merge_Weatherdataset", Preprocess_Merge_Weather()),
                                             ("preprocess+merge_Holidaydataset", Preprocess_Merge_Holidays())])
    return preprocessing_pipeline


# print(sales)
print(get_preprocessing_pipeline().transform([sales, weather, holidays]))


# union_pipeline

# model_pipeline
