from cgi import print_environ_usage
from curses import A_VERTICAL
import os

import numpy as np
import pandas as pd

import earthpy as et
def main():
    os.chdir(os.path.join(os.path.expanduser('~'), 
                            'earth-analytics-parent', 
                            'earth-analytics'))

    fname = os.path.join('data', 'earthpy-downloads', 
                     'avg-precip-months-seasons.csv')

    avg_monthly_precip = pd.read_csv(fname)

    print(avg_monthly_precip)

    high_precip: pd.DataFrame = avg_monthly_precip[avg_monthly_precip['precip'] >= 1]
    print(high_precip)
    print()
    print(high_precip.loc[2:4])


if __name__ == '__main__':
    main()