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
GDP_by_region_and_country_WB_merge = pd.merge(Country_by_region_WB,GDP_by_country_WB, left_on='TableName', right_on='Country Name')
print(GDP_by_region_and_country_WB_merge.shape)
GDP_by_region_and_country_WB_merge.to_csv("merged_WB.csv")
# Check individual values for missing values
print((GDP_by_region_and_country_WB_merge.isna))
print((GDP_by_region_and_country_WB_merge.isna().any))
print(GDP_by_region_and_country_WB_merge.isna().sum())
# Delete rows on IncomeGroup & Region with NaN values (Aggregate Columns)
GDP_by_region_and_country_WB_merge_cl1=GDP_by_region_and_country_WB_merge.dropna(subset=["Region"])
print(GDP_by_region_and_country_WB_merge_cl1.isna().sum())
# Delete dupliate or unnecessary columns
GDP_by_region_and_country_WB_merge_cl2= GDP_by_region_and_country_WB_merge_cl1.drop(['SpecialNotes', 'TableName',"Indicator Code","2020"], axis=1)
print(GDP_by_region_and_country_WB_merge_cl2.info())