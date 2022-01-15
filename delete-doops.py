# Given two zip files, both containing multiple CSV files. 
# Using the file id of the CSV files in the DUPLICATES folder, 
# delete the accounts within the CSV files in the other folder that match said file id numbers.

# Approach
# - Combine purchased portfolios into 1 single .xlsx file to be able to compare against for sale portfolios.
# - Only read the accountid column for the purchased portfolio to increase speed.
# - Go through the whole for sale portfolio row by row and compare each account id against account ids in purchased portfolio.
# - If match, remove row. (improvement: if no match, add to new dataframe instead of needing to remove row and shift whole spreadsheet up by a row.)
# - Once done, write df to .xlsx in pulled/ directory

import pandas as pd
import os
import glob

# Script for concatenating multiple .xlsx into one .xlsx

# path = os.getcwd()
# csv_files = glob.glob(os.path.join(path, "purchased/*.xlsx"))
#
# df = pd.concat(
#     map(pd.read_excel, csv_files), ignore_index=True)
#
# writer = pd.ExcelWriter('test.xlsx', engine="xlsxwriter")
#
# df.to_excel(writer, sheet_name="Sheet1")
#
# writer.save()

# Portfolios to read
forsale_portfolio_path = "test_forsale/forsale.xlsx"
purchased_portfolio_path = "test_purchased/purchased.xlsx"

# Read portfolios and load in as Data Frames
forsale_portfolio_df = pd.read_excel(forsale_portfolio_path)
purchased_portfolio_df = pd.read_excel(purchased_portfolio_path, usecols="A")


# Create new empty data frame that will only contain fresh accounts, keep column headers
cleaned_portfolio_df = pd.DataFrame(data=forsale_portfolio_df.values, columns=forsale_portfolio_df.columns)

# Search through each row of forsale portfolio, compare each account id against purchased, if no match, push to new dataframe
forsale_portfolio_length = len(forsale_portfolio_df)

# for i in range(forsale_portfolio_length):
#     # this is the column value
#     val = forsale_portfolio_df.iloc[i, 0]

#     if val in purchased_portfolio_df.iloc[:, 0].values:
#         print("duplicate", i)
#     else:
#         print("unique", i)


writer = pd.ExcelWriter('test-headers.xlsx', engine="xlsxwriter")

cleaned_portfolio_df.to_excel(writer, sheet_name="Sheet1", index=False)

writer.save()