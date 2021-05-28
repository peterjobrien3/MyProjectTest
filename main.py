# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pandas as pd
# Read population_by_country.csv
population_by_country=pd.read_csv("population_by_country_2020.csv")
print(population_by_country.head())
print(population_by_country.info())
GDP_by_country_WB=pd.read_csv("API_NY.GDP.MKTP.CD_DS2_en_csv_v2_2445719.csv",skiprows=4)
print(GDP_by_country_WB.head())
print(GDP_by_country_WB.info())
Country_by_region_WB=pd.read_csv("Metadata_Country_API_NY.GDP.MKTP.CD_DS2_en_csv_v2_2445719.csv")
print(Country_by_region_WB.head())
print(Country_by_region_WB.info())