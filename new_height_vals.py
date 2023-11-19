# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 18:02:47 2023

@author: VShields
"""

import pandas as pd
from datetime import date
from myformatter import MyFormatter
import argparse


def indicators(x):
    if x == "left_only":
        return "New"
    elif x == "right_only":
        return "Old"
    else:
        return "Both"

def find_new(listing_1: str,listing_2: str,columns: list) -> None:

    listing_1 = pd.read_csv(listing_1)
    listing_2 = pd.read_csv(listing_2)
    # read most recent csv file from downloads folder and rename it. Make sure to
    # download the correct file first



    try:
        listing_2 = listing_2[columns]
        listing_1 = listing_1[columns]
    except KeyError as e:
        print("Are your column names matching")


    # listing_2["VisitDate"] = pd.to_datetime(height_new["VisitDate"])
    # listing_2.sort_values(by=["Patient","VisitDate"],inplace=True)
    #
    #
    # listing_1["VisitDate"] = pd.to_datetime(height_old["VisitDate"])
    # listing_1.sort_values(by=["Patient","VisitDate"],inplace=True)
    #

    test = pd.merge(listing_2,listing_1,how='outer',indicator=True)
    test.rename(columns={"_merge":"Indicator"},inplace=True)

    test["Indicator"] = test["Indicator"].apply(indicators)
    # test["VisitDate"] = pd.to_datetime(test["VisitDate"])
    # test["VisitDate"] = test["VisitDate"].dt.strftime("%d-%b-%Y")

    with pd.ExcelWriter("NewVals{:%d_%b_%Y}.xlsx".format(date.today())) as writer:

        workbook  = writer.book

        test.to_excel(writer, sheet_name="Height",index=False)
        worksheet = writer.sheets["Height"]
        formatter = MyFormatter(test,workbook,worksheet)
        formatter.spacing()
        formatter.color_columns()
        formatter.add_borders()
        worksheet.freeze_panes(1,1)
        worksheet.autofilter(0, 0, len(test), len(test.columns)-1)
        worksheet.filter_column('E',"indicator == New or indicator == Old")

def main():
    listing_1 = input("Enter the old line listing: ")
    listing_2 = input("Enter the new line listing: ")
    columns = input("Enter the columns to match: ")
    columns=columns.split(' ')
    # parser = argparse.ArgumentParser(description="Find new height values.")
    # parser.add_argument("filename", type=str, help="Path to the csv file")
    # args = parser.parse_args()
    find_new(listing_1,listing_2,columns)

if __name__ == "__main__":
    main()
