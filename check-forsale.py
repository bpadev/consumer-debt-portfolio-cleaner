# Check "for sale" portfolios against each other for duplicate accounts.

# Approach
# - Make dataframes from directory

import glob
import re
import subprocess
import pandas as pd
import os

from multiprocessing.dummy import Pool

# Convert .xlsx to .csv for speed improvement
xlsx_path = 'for-sale/'
csv_path = 'csv-forsale/'
list_of_xlsx = glob.glob(xlsx_path+'*.xlsx')

# for xlsx in list_of_xlsx:
#   # Extract File Name on group 2
#   filename = re.search(r'(.+[\\|\/])(.+)(\.(xlsx))', xlsx).group(2)
#   # Setup the call for subprocess.call()
#   call = ["python", "venv/bin/xlsx2csv", xlsx, csv_path+filename+'.csv']
#   try:
#       subprocess.call(call) # On Windows use shell=True
#   except:
#       print('Failed with {}'.format(filepath))

commands = []
for filepath in glob.glob(xlsx_path+'*.xlsx'):
    filename = re.search(r'(.+[\\|\/])(.+)(\.(csv|xlsx|xlx))', filepath) #Extract File Name on group 2 "(.+)"

    call = ["python", "venv/bin/xlsx2csv", filepath, csv_path+'{}.csv'.format(filename.group(2))]
    commands.append(call)

pool = Pool(2) # Specify How many concurrent threads

# Use functools.partial(subprocess.call, shell=True) in place of subprocess.call if you're on windows
for i, return_code in enumerate(pool.imap(subprocess.call, commands)):
    if return_code != 0:
        print("Command # {} failed with return code {}.".format(i, return_code))

# # Grab portfolios to read
# fs_directory_path = 'for-sale/'

# fs_portfolios = os.listdir(fs_directory_path)

# # Store amount of files for loop
# files_to_clean = len(fs_portfolios)

# duplicates = 0

# def make_dataframes(directory):

#   # get list of file names in given directory
#   file_names = os.listdir(directory)

#   # make empty list to hold dataframes
#   dataframes = []

#   # make files readable to pandas
#   for file in file_names:
    
#     # add directory prefix
#     file = fs_directory_path + file

#     # read as df
#     df = pd.read_excel(file)
    
#     # store as dataframes
#     dataframes.append(df)

#   return dataframes


# def check_duplicates(row, dataframes, duplicates):

#   # go over each df and compare each row against the supplied row argument from the current_df
#   for df in dataframes:

#     # iterate over each row of dataframe to be compared
#     for row_comp in df.itertuples():
      
#       # these grab values in their desired column, make sure every df has the same column setup for account ids
#       if row[1] == row_comp[1]:

#         duplicates += 1

#         # remove duplicate from only one portfolio! remove it from the portfolio in the list, not the current_df!
#         df.drop(row_comp[0], inplace=True)

#         print(duplicates)


# def write_dataframes_excel(dataframes):

#   # get list of file names in given directory
#   file_names = os.listdir(fs_directory_path)

#   options = {}

#   options['strings_to_formulas'] = False

#   options['strings_to_urls'] = False 

#   i = 0

#   for file in file_names:

#     writer = pd.ExcelWriter('pulled/pulled-' + file, engine="xlsxwriter", options=options)

#     dataframes[i].to_excel(writer, sheet_name="Sheet1", index=False)

#     writer.save()

#     # don't need conditional to stop loop because file_names are same size as dataframes?
#     i += 1


# def main():

#   # get dataframes
#   dataframes = make_dataframes(fs_directory_path)

#   # make copy
#   dataframes_temp = dataframes.copy()

#   # gurantees each df is ran through, regardless of indexing technique that modifies temp df list
#   for df in dataframes:

#     # set current df, this is always supposed to be index 0, the list items get modified
#     current_df = dataframes_temp.pop(0)

#     # iterate over every row in the current df
#     for row in current_df.itertuples():

#       # run the duplicate check against all other dataframes in the temp list
#       check_duplicates(row, dataframes_temp, duplicates)  

#     # return to dataframes_temp, loop on next dataframe
#     dataframes_temp.append(current_df)

#   # write modified dataframes to sheets
#   write_dataframes_excel(dataframes)

# main()