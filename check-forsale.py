# Check "for sale" portfolios against each other for duplicate accounts.

# Approach
# - grab all portfolios in the for-sale directory, store them as a list.
# - pull out the first portfolio and remove it from portfolios list.
# - run through all portfolios and check them against current check portfolio.
# - once completed, append to end of list, pop portfolios[0] to current check, repeat.

import pandas as pd
import os


fs_portfolios_directory = 'for-sale/'



# pull directory list
fs_portfolios = os.listdir(fs_portfolios_directory)

# set portfolio to start
current_check = fs_portfolios.pop(0)

def clean(current):

  for index, row in current.iterrows():

    print(index, row)

for i in range(len(fs_portfolios)):

  current_df = pd.read_excel(fs_portfolios_directory + fs_portfolios[i])
  
  clean(current_df)