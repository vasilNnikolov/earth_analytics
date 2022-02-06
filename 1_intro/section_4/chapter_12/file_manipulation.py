import os
from glob import glob
import earthpy as et
def get_data():
    file_url = "https://ndownloader.figshare.com/files/21894528"
    et.data.get_data(url = file_url)

def main():
    # set working directory
    os.chdir(os.path.join(os.path.expanduser('~'), 'earth-analytics-parent', 'earth-analytics'))
    # run once
    # get_data()
    data_folder = os.path.join('data', 'earthpy-downloads', 'avg-monthly-temp-fahr')
    print(len(glob(os.path.join(data_folder,'San-Diego', '*'))))

if __name__ == "__main__":
    main()