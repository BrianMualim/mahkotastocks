# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 13:59:36 2024

@author: brian
"""

import csv
import pandas as pd
import openpyxl
import math
import numpy as np
from datetime import datetime, timedelta

# Data from 2001 - 2022

# MIN RISK PORTFOLIO

start_date = datetime.strptime("20210601", "%Y%m%d")
end_date = datetime.strptime("20211230", "%Y%m%d")

# Will be dynamic, user input
stocks_chosen = ["Date", "BRPT", "ADRO", "PGAS", "BBCA", "MEDC"]

# "Date" column must be kept
stocks_prices_df = pd.read_csv(r"C:\Users\brian\Downloads\mahkotastocks\Pull " + str(start_date.year) + "\Pull 2021 PX.csv", 
                               usecols = stocks_chosen, index_col = ["Date"])

returns_df = stocks_prices_df.pct_change()
returns_df.index = pd.to_datetime(returns_df.index)

specific_returns_df = returns_df.loc[start_date:end_date]

# Converted to array
cov_matrix = specific_returns_df.cov().to_numpy()
ones_matrix = np.tile(1, cov_matrix.shape[1])

x_weights = (cov_matrix @ ones_matrix) / (np.transpose(ones_matrix) @ cov_matrix @ ones_matrix)



