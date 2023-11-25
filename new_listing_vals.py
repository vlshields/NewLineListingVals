"""
Created on Mon Jun  5 18:02:47 2023

@author: VShields
"""

import pandas as pd
from datetime import date
from myformatter import MyFormatter



def indicators(x):
    if x == "left_only":
        return "New"
    elif x == "right_only":
        return "Old"
    else:
        return "Both"

def find_new(listing_1: str,listing_2: str,columns: str, color: str) -> None:
      """
    Compare two CSV files containing data to identify new and old entries based on selected columns.

    Parameters:
    - listing_1 (str): File path of the first CSV file.
    - listing_2 (str): File path of the second CSV file.
    - columns (str): Space-separated columns to be used for comparison.

    The function reads the CSV files into pandas DataFrames, selects specified columns,
    and merges them using an outer join. An indicator column is created to label entries
    as 'New,' 'Old,' or 'Both.' The resulting DataFrame is saved to an Excel file named
    "NewVals{current_date}.xlsx" with formatted styling. The user is prompted to input
    the file names and columns to be matched during script execution.
    """

    listing_1 = pd.read_csv(listing_1)
    listing_2 = pd.read_csv(listing_2)

    letter_dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G',
    8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N',
    15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
     21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}


    try:
        listing_2 = listing_2[columns.split()]
        listing_1 = listing_1[columns.split()]
    except KeyError as e:
        print(e)



    test = pd.merge(listing_2,listing_1,how='outer',indicator=True)
    test.rename(columns={"_merge":"Indicator"},inplace=True)

    test["Indicator"] = test["Indicator"].apply(indicators)

    with pd.ExcelWriter("NewVals{:%d_%b_%Y}.xlsx".format(date.today())) as writer:

        workbook  = writer.book

        test.to_excel(writer, sheet_name="Height",index=False)
        worksheet = writer.sheets["Height"]
        formatter = MyFormatter(test,workbook,worksheet)
        formatter.spacing()
        formatter.color_columns(color = color)
        formatter.add_borders()
        worksheet.freeze_panes(1,1)
        worksheet.autofilter(0, 0, len(test), len(test.columns)-1)
        key = len(test.columns)
        worksheet.filter_column(letter_dict[key],"indicator == New or indicator == Old")

def main():

    listing_1 = input("Enter the new line listing: ")
    listing_2 = input("Enter the new line listing: ")
    columns = input("Enter the columns to match: ")
    color = input("Please enter the desired column color (HEX): ")
    find_new(listing_1,listing_2,columns)
