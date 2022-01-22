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

  fs_portfolios.append('hello')

  return fs_portfolios


def set_loop_settings(portfolios):

  # number of portfolios in directory that need to be cleaned, indices would be from 0 through number_of_portfolios - 1
  number_of_portfolios = len(portfolios)

  # set initial portfolio for looping
  current_portfolio = portfolios[0]

  # build array of files



def run_cleaner():

  # get portfolios
  fs_portfolios = get_portfolios(fs_portfolios_directory)

  # set initial portfolio for looping
  current_fs_portfolio = set_initial_portfolio(fs_portfolios)

  # set current loop settings
  set_loop_settings(fs_portfolios)



print(get_portfolios(fs_portfolios_directory))