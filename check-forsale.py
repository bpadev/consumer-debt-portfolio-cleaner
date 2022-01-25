# Check "for sale" portfolios against each other for duplicate accounts.

# Approach
# - Make dataframes from directory

import pandas as pd
import os


# Grab portfolios to read
fs_directory_path = 'for-sale/'

fs_portfolios = os.listdir(fs_directory_path)

# Store amount of files for loop
files_to_clean = len(fs_portfolios)

duplicates = 0

def make_dataframes(directory):

  # get list of file names in given directory
  file_names = os.listdir(directory)

  # make empty list to hold dataframes
  dataframes = []

  # make files readable to pandas
  for file in file_names:
    
    # add directory prefix
    file = fs_directory_path + file

    # read as df
    df = pd.read_excel(file)
    
    # store as dataframes
    dataframes.append(df)

  return dataframes

def check_duplicates(row, dataframes, duplicates):

  # go over all files in temp dataframes
  for df in dataframes:

    for row_comp in df.itertuples():
      
      if row[1] == row_comp[1]:

        print('duplicate')


def main():

  # get dataframes
  dataframes = make_dataframes(fs_directory_path)

  # make copy
  dataframes_temp = dataframes.copy()

  # 
  for df in dataframes:

    # set current df
    current_df = dataframes_temp.pop(0)

    for row in current_df.itertuples():

      # run check against others in list
      check_duplicates(row, dataframes_temp, duplicates)  

    # return to dataframes_temp
    dataframes_temp.append(current_df)

  print(dataframes_temp)

main()