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
