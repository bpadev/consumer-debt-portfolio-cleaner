# Given two zip files, both containing multiple CSV files. 
# Using the file id of the CSV files in the DUPLICATES folder, 
# delete the accounts within the CSV files in the other folder that match said file id numbers.

# Approach
# -

import pandas as pd
import os
import glob

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

# for f in csv_files:
#
#     df = pd.read_excel(f, usecols="A", ignore_index=True)
#
#     print(df)

# real
new_path = "newnew/Connect 1 Inventory 4.xlsx"
purchased_path = "test.xlsx"

# test
# new_path = "test_new/new.xlsx"
# purchased_path = "test_purchased/purchased.xlsx"

# def logic(val):

    # if val in purchased_df.values:
    #     # purchased_df.drop([val.index])
    #     print(val.index)
    # else:
    #     print(True)
# new_df = pd.read_excel(new_path, usecols="A", skiprows=lambda x: logic(x))


# purchased_df = pd.read_excel(purchased_path, usecols="A")
new_df = pd.read_excel(new_path, usecols="A")

# Working piece for comparing purchased values with new and dropping duplicates.
mod_new = new_df

dups = []
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


print(mod_new)

