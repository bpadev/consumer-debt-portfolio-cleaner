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

# Store amount of files for loop
files_to_clean = len(fs_portfolios)

for i in range(files_to_clean):

  print(fs_portfolios)

  # Current portfolio in loop
  current_portfolio = fs_directory_path + fs_portfolios[0]

  # read current portfolio as df
  # current_portfolio_df = pd.read_excel(current_portfolio)
  
  # remove current portfolio from list
  current_portfolio_name = fs_portfolios.pop(0)

  # clean

  # append back
  fs_portfolios.append(current_portfolio_name)

print(fs_portfolios)