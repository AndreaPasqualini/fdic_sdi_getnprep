#!/usr/bin/python3

import os, sys
from datetime import datetime
import aiohttp, asyncio
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
        q1, q2, q3, q4 = build_year_urls(y)
        urls.extend([q1, q2, q3, q4])
    return urls


async def get(url, destination):
    fname = url.split('/')[-1]
    log = 'download.log'
    try:
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.get(url=url) as response:
                resp = await response.read()
    except Exception as e:
        now = f'[{datetime.now()}]  '
        with open(destination + log, mode='a') as f:
            f.write(now + f"Unable to get {url}. Reason: {e.__class__}.\n")
    else:
        now = f'[{datetime.now()}]  '
        size_mb = '{:.3f}'.format(len(resp) / 1024**2)
        with open(destination + fname, mode='wb') as zipfile:
            zipfile.write(resp)
        with open(destination + log, mode='a') as f:
            f.write(now + f"Got {url} with size {size_mb} MB.\n")


async def main(urls, folder, amount):
    url_loop = tqdm(urls)
    for u in url_loop:
        await get(u, folder)
    # await asyncio.gather(*[await get(u, folder) for u in tqdm(asyncio.as_completed(urls), total=len(urls))])
    print("Download job finished.\n")


#%% Main program

if __name__ == '__main__':
    first_year = int(sys.argv[1])
    last_year = int(sys.argv[2])
    destination = sys.argv[3]
    if destination[-1] != '/':
        destination += '/'
    if os.path.exists(destination + 'download.log'):
        os.remove(destination + 'download.log')
    dirlist = os.listdir(destination)
    for f in dirlist:
        if f.endswith('.zip'):
            os.remove(destination + f)
    urls = build_all_year_urls(first_year, last_year)
    asyncio.run(main(urls, destination, len(urls)))
