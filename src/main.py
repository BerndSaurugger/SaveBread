from filehandler.load_input import load_file
from preprocessing.preprocessing import preprocess_datasets

sales = load_file("src/data/Bakery_Sales.csv")

# read in csv, needs separation by semicolon to read in
weather = load_file("src/data/Seoul_weather.csv", seperator=";")

# read in csv, needs separation by semicolon to read in
holidays = load_file("src/data/public_holidays.csv", seperator=";")

df = preprocess_datasets(sales, weather, holidays)
print(df)
