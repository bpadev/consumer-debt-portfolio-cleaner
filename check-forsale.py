# Check "for sale" portfolios against each other for duplicate accounts.

# Approach
# - grab all portfolios in the for-sale directory, store them as a list.
# - pull out the first portfolio and remove it from portfolios list.
# - run through all portfolios and check them against current check portfolio.
# - once completed, append to end of list, pop portfolios[0] to current check, repeat.

import pandas as pd
import os


fs_portfolios_directory = 'for-sale/'

def get_portfolios(directory):

  # pull directory list
  fs_portfolios = os.listdir(directory)

  return fs_portfolios


def run_cleaner():

  # get portfolios
  fs_portfolios = get_portfolios(fs_portfolios_directory)





print(get_portfolios(fs_portfolios_directory))