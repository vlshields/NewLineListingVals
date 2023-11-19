# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 18:02:47 2023

@author: VShields
"""

import pandas as pd
from datetime import date
from myformatter import MyFormatter
import argparse
from quickhelper import QuickHelper

def indicators(x):
    if x == "left_only":
        return "New"
    elif x == "right_only":
        return "Old"
    else:
        return "Both"

def find_new(filename: str) -> None:
    
    height_old = pd.read_csv(filename)
    
    # read most recent csv file from downloads folder and rename it. Make sure to
    # download the correct file first
    
    
    qh = QuickHelper("heightvals")
    height_new = qh.data
    print(height_new.columns)
    try:
        height_new = height_new[['Patient','CurrentHeight', "VisitDate","VisitNum"]]
        height_old = height_old[['Patient','CurrentHeight', "VisitDate","VisitNum"]]
    except KeyError as e:
        print("Did you remember to download the data grid?")
        
    
    height_new["VisitDate"] = pd.to_datetime(height_new["VisitDate"])
    height_new.sort_values(by=["Patient","VisitDate"],inplace=True)
    
    
    height_old["VisitDate"] = pd.to_datetime(height_old["VisitDate"])
    height_old.sort_values(by=["Patient","VisitDate"],inplace=True)
    
    
    test = pd.merge(height_new,height_old,how='outer',indicator=True)
    test.rename(columns={"_merge":"Indicator"},inplace=True)
    
    test["Indicator"] = test["Indicator"].apply(indicators)
    test["VisitDate"] = pd.to_datetime(test["VisitDate"])
    test["VisitDate"] = test["VisitDate"].dt.strftime("%d-%b-%Y")
    
    with pd.ExcelWriter("HeightNewVals{:%d_%b_%Y}.xlsx".format(date.today())) as writer:
        
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
    parser = argparse.ArgumentParser(description="Find new height values.")
    parser.add_argument("filename", type=str, help="Path to the csv file")
    args = parser.parse_args()
    find_new(args.filename)

if __name__ == "__main__":
    main()



