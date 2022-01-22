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


def set_loop_arguments(initial_amount_portfolios, portfolios, current_check):


  # check if first iteration
  if len(portfolios) == initial_amount_portfolios:

    # no append
    current_check = portfolios.pop(0)
  
  else:

    # put portfolio back at end of array
    portfolios.append(current_check)

    # pop new current
    current_check = portfolios.pop(0)






def run_cleaner():

  # get portfolios
  fs_portfolios = get_portfolios(fs_portfolios_directory)

  # keep initial amount of portfolios

  # needed for if/else statement
  current_check = fs_portfolios[0]

  initial_amount_portfolios = len(fs_portfolios)

  # set loop arguments
  set_loop_arguments(initial_amount_portfolios, fs_portfolios, current_check)
