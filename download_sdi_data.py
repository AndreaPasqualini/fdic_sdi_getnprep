#!/usr/bin/python3

import os, sys
import requests
from datetime import datetime
from functools import partial
from multiprocessing.pool import ThreadPool
from tqdm import tqdm


#%% Define functions

def build_year_urls(year):
    location = 'https://www7.fdic.gov/sdi/Resource/AllReps/'
    filename_q1 = f'All_Reports_{year}0331.zip'
    filename_q2 = f'All_Reports_{year}0630.zip'
    filename_q3 = f'All_Reports_{year}0930.zip'
    filename_q4 = f'All_Reports_{year}1231.zip'
    fnames = [filename_q1, filename_q2, filename_q3, filename_q4]
    return list(map(lambda x: location + x, fnames))


def build_all_year_urls(start, stop):
    urls = []
    for y in range(start, stop+1):
        urls.extend(build_year_urls(y))
    return urls


def compute_total_download_size(urls):
    total_length = 0
    for url in urls:
        with requests.get(url, stream=True) as resp:
            try:
                resp.raise_for_status()
                total_length += int(resp.headers.get('content-length', 0))
            except requests.HTTPError:
                continue
    return total_length


def download_remote_file(url, folder='./', log='./download.log'):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as resp:
        try:
            resp.raise_for_status()
        except requests.HTTPError:
            now = datetime.now()
            length = 0
            code = resp.status_code
            msg = f'Unable to get {url} due to HTTP status code {code}.'
            with open(log, mode='a') as logfile:
                logfile.write(f'[{now}]  ' + msg + '\n')
        else:
            length = int(resp.headers.get('content-length', 0))
            with open(folder + local_filename, mode='wb') as fl:
                for data in resp.iter_content(8192):
                    fl.write(data)
            now = datetime.now()
            size_mb = '{:.3f}'.format(length / 1024**2)
            msg = f'Successfully got {url} with size {size_mb} MB.'
            with open(log, mode='a') as logfile:
                logfile.write(f'[{now}]  ' + msg + '\n')
    return length


def main(urls, destination, logfile, concurrent_downloads):
    n = len(urls)
    dload = partial(download_remote_file, folder=destination, log=logfile)
    with ThreadPool(concurrent_downloads) as pool:
        for _ in tqdm(pool.imap_unordered(dload, urls), total=n):
            pass


#%% Main program

if __name__ == '__main__':
    destination = sys.argv[1]
    first_year = int(sys.argv[2])
    last_year = int(sys.argv[3])
    try:
        download_streams = int(sys.argv[4])
    except IndexError:
        download_streams = 4
    if destination[-1] != '/':
        destination += '/'
    logfile = destination + 'download.log'
    if os.path.exists(logfile):
        os.remove(logfile)
    dirlist = os.listdir(destination)
    for f in dirlist:
        if f.endswith('.zip'):
            os.remove(destination + f)
    urls = build_all_year_urls(first_year, last_year)
    main(urls, destination, logfile, download_streams)
