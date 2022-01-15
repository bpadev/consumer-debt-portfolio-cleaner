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
forsale_portfolio_path = "test_new/forsale.xlsx"
purchased_portfolio_path = "test_purchased/purchased.xlsx"

# Read portfolios and load in as Data Frames
forsale_portfolio_df = pd.read_excel(forsale_portfolio_path)
purchased_portfolio_df = pd.read_excel(purchased_portfolio_path, usecols="A")


print(forsale_portfolio_df, purchased_portfolio_df)

# #
# for i in range(len(new_df)):
#     # this is the column value
#     val = new_df.iloc[i, 1]
#     # val = new_df.iloc[i, 0]
#
#     if val in purchased_df.iloc[:, 0].values:
#         print("duplicate", i)
#         dups.append(new_df.iloc[i])
#         mod_new = mod_new.drop(i)
#
# writer = pd.ExcelWriter('pulled/connect1-pulled12.xlsx', engine="xlsxwriter")
#
# mod_new.to_excel(writer, sheet_name="Sheet1")
#
# writer.save()
