# Check "for sale" portfolios against each other for duplicate accounts.

# Approach
# - grab all portfolios in the for-sale directory
# - set initial portfolio to the first portfolio in the directory.
# - 

import pandas as pd
import os

fs_portfolios_directory = 'for-sale/'


def get_portfolios(directory):

  # pull directory list
  fs_portfolios = os.listdir(directory)

  return fs_portfolios


def set_initial_portfolio(portfolios):
  
  # set current portfolio to initial portfolio, first .xlsx in directory
  current_fs_portfolio = portfolios[0]


def run_cleaner():

  # get portfolios
  fs_portfolios = get_portfolios(fs_portfolios_directory)

  # set initial portfolio for looping
  set_initial_portfolio(fs_portfolios)

  # 