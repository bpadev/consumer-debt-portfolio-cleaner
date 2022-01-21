# Check "for sale" portfolios against each other for duplicate accounts.

# Approach
# - grab all portfolios in the for-sale directory
# - 

import pandas as pd
import os

fs_portfolios_directory = 'for-sale/'


def get_portfolios(directory):

  # pull directory list
  fs_portfolios = os.listdir(directory)

  return fs_portfolios


print(get_portfolios(fs_portfolios_directory))

