# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 10:59:16 2023

@author: VShields
"""
import pandas as pd
import glob
import os
from pathlib import Path
import win32com.client


class MyFormatter:
    def __init__(self, data, workbook, worksheet):
        self.data = data
        self.workbook = workbook
        self.worksheet = worksheet

    def spacing(self):
        """
        Function to add spacing to Excel columns based on the maximum length of the
        data in each column.
        """
        if isinstance(self.data, pd.DataFrame):
            if self.data.index.nlevels > 1:
                self.data = self.data.reset_index()
        elif isinstance(self.data, pd.core.groupby.DataFrameGroupBy):
            self.data = self.data.apply(lambda x: x.reset_index(drop=True))
            self.data = self.data.reset_index()
        else:
            raise TypeError("The data must be a pd.DataFrame or a pd.core.groupby.DataFrameGroupBy.")

        for i, col in enumerate(self.data.columns):
            max_width = max(self.data[col].astype(str).str.len().max(), len(col))
            self.worksheet.set_column(i, i, max_width + 1)

    def color_columns(self, grey_bottom=False, color='#ffb3b3'):
        """
        Function to color columns in Excel worksheet.
        """
        if isinstance(self.data, pd.DataFrame):
            if self.data.index.nlevels > 1:
                self.data = self.data.reset_index()
        elif isinstance(self.data, pd.core.groupby.DataFrameGroupBy):
            self.data = self.data.apply(lambda x: x.reset_index(drop=True))
            self.data = self.data.reset_index()
        else:
            raise TypeError("The data must be a pd.DataFrame or a pd.core.groupby.DataFrameGroupBy.")

        if grey_bottom:
            last_row = self.data.shape[0]
            last_column = self.data.shape[1]
            last_row_format = self.workbook.add_format({'bg_color': '#d9d9d9', 'bold': True})
            self.worksheet.conditional_format(last_row, 0, last_row, last_column, {'type': 'no_blanks', 'format': last_row_format})

        column_format = self.workbook.add_format({'bg_color': color})
        self.worksheet.conditional_format(0, 0, 0, len(self.data.columns), {'type': 'no_blanks', 'format': column_format})

    def add_borders(self):
        """
        Function to add borders to cells in Excel worksheet.
        """
        if isinstance(self.data, pd.DataFrame):
            if self.data.index.nlevels > 1:
                self.data = self.data.reset_index()
        elif isinstance(self.data, pd.core.groupby.DataFrameGroupBy):
            self.data = self.data.apply(lambda x: x.reset_index(drop=True))
            self.data = self.data.reset_index()
        else:
            raise TypeError("The data must be a pd.DataFrame or a pd.core.groupby.DataFrameGroupBy.")

        border_format = self.workbook.add_format({'border': 1, 'border_color': 'black'})
        border_format.set_locked(False)
        self.worksheet.conditional_format(1, 0, len(self.data), self.data.shape[1]-1, {'type': 'no_errors', 'format': border_format})

    def panes(self):
        self.worksheet.freeze_panes(1,1)
