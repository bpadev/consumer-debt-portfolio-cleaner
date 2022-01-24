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

  print(dataframes[0])




# for i in range(files_to_clean):

#   # get data frames, single current portfolio and then list of portfolios to compare
#   get_dataframes(fs_portfolios[0], fs_portfolios)
#   # current_portfolio_df = pd.read_excel(current_portfolio)
  
#   # remove current portfolio from list
#   current_portfolio_name = fs_portfolios.pop(0)

#   # append back
#   fs_portfolios.append(current_portfolio_name)

make_dataframes(fs_directory_path)