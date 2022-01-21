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


def set_loop_settings(portfolios):

  # grab number of portfolios in directory
  number_of_portfolios = len(portfolios)


def run_cleaner():

  # get portfolios
  fs_portfolios = get_portfolios(fs_portfolios_directory)

  # set initial portfolio for looping
  current_fs_portfolio = set_initial_portfolio(fs_portfolios)

  # set current loop settings
  set_loop_settings(fs_portfolios)



run_cleaner()