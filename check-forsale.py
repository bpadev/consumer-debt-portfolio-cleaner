# Check "for sale" portfolios against each other for duplicate accounts.

# Approach
# - grab all portfolios in the for-sale directory, store them as a list.
# - pull out the first portfolio and remove it from portfolios list.
# - run through all portfolios and check them against current check portfolio.
# - once completed, append to end of list, pop portfolios[0] to current check, repeat.

import pandas as pd
import os


# Grab portfolios to read
fs_directory_path = 'for-sale/'

fs_portfolios = os.listdir(fs_directory_path)

def get_current_portfolio(p):

  # make path to current portfolio
  path = fs_portfolios_directory + p[i]
  
  # read and store as dataframe
  df = pd.read_excel(path)

  return df


for i in range(len(fs_portfolios)):

  # gets current portfolio as df
  get_current_portfolio(fs_portfolios)