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
# Install Pandas and Matplotlib
import pandas as pd
import matplotlib.pyplot as plt

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
# Delete dupliates or unnecessary columns:
GDP_by_region_and_country_WB_merge_cl2= GDP_by_region_and_country_WB_merge_cl1.drop(['SpecialNotes', 'TableName',"Indicator Code","Unnamed: 5","Country Code_y","2020","Unnamed: 65"], axis=1)
print(GDP_by_region_and_country_WB_merge_cl2.info())
print(GDP_by_region_and_country_WB_merge_cl2.isna().any())
# Extract to csv and review:
GDP_by_region_and_country_WB_merge_cl2.to_csv("merged_WB_v2.csv")
# Rename column Country Code_x to Country Code:
GDP_by_region_and_country_WB_merge_cl3=GDP_by_region_and_country_WB_merge_cl2.rename({"Country Code_x":"Country Code"},axis=1)
print(GDP_by_region_and_country_WB_merge_cl3.info())
# Insert a column "Baseline_GDP" after Indicator Name with value 0 for all rows.
GDP_by_region_and_country_WB_merge_cl3["Baseline_GDP"]=0
print(GDP_by_region_and_country_WB_merge_cl3.head())
# Move "Baseline_GDP" column position to after "Indicator Name" and before GBP data
col_list = GDP_by_region_and_country_WB_merge_cl3.columns.tolist()
col_list.insert(5, col_list.pop(col_list.index('Baseline_GDP')))
print(col_list)
GDP_by_region_and_country_WB_merge_cl3 = GDP_by_region_and_country_WB_merge_cl3.reindex(columns=col_list)
# Forward fill by row across all columns
GDP_by_region_and_country_WB_merge_cl4=GDP_by_region_and_country_WB_merge_cl3.ffill(axis=1)
print(GDP_by_region_and_country_WB_merge_cl4.info())
print(GDP_by_region_and_country_WB_merge_cl4.head())
GDP_by_region_and_country_WB_merge_cl4.to_csv("merged_WB_v4.csv")
# Set the Indexs to Region and IncomeGroup
GDP_by_region_and_country_WB_merge_cl4=GDP_by_region_and_country_WB_merge_cl4.set_index("Region","IncomeGroup")
print(GDP_by_region_and_country_WB_merge_cl4.head())
# Groupby region and GDP 2019
GDP_by_region_2000v2019 = GDP_by_region_and_country_WB_merge_cl4.groupby("Region")[["2000","2019"]].sum()
print(GDP_by_region_2000v2019)
GDP_by_region_2000v2019.plot(kind="bar", title="GDP by Region 2000 V 2019")
plt.show()
GDP_Years=["1960","2000","2019"]
GDP_by_region = GDP_by_region_and_country_WB_merge_cl4.groupby("Region")[GDP_Years].sum()
GDP_by_region[GDP_Years].plot(kind="pie", subplots=True, title="GDP by Region 1960, 2000, 2019")
plt.show()
# Slice for sub saharan Africa
sub_saharan_africa_GDP = GDP_by_region_and_country_WB_merge_cl4[GDP_by_region_and_country_WB_merge_cl4["Sub-Saharan Africa"].isin("Region")]
print(sub_saharan_africa_GDP)