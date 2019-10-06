#!/usr/bin/python3

import sys
from bs4 import BeautifulSoup as bs
from requests import get
from urllib.request import urlretrieve
from tqdm import tqdm


#%% Obtain HTML source

website = 'https://www5.fdic.gov/sdi/'
webpage = get(website + 'download_large_list_outside.asp')
soup = bs(webpage.text, 'lxml')
tables = soup.find_all('table')
table = tables[1]
tablerows = table.find_all('tr', align='center')


#%% Parse HTML table into a list of tuples

table_parsed = []

for i, row in enumerate( tablerows ):
    if i == 0:
        th0 = row.find('th', id='filename').text
        th1 = row.find('th', id='filesize').text
        th2 = row.find('th', id='rptdate').text
        table_header = (th0, th1, th2)
    else:
        url_relative = row.find('a')['href']
        url_absolute = website + url_relative
        columns = row.find_all('td', align='center')
        row_parsed = tuple([col.text.strip() for col in columns])
        augmented_row_parsed = row_parsed + (url_absolute,)
        table_parsed.append(augmented_row_parsed)


#%% Download files and name them appropriately

if __name__ == '__main__':

    download_location = sys.argv[1]
    if download_location[-1] != '/':
        download_location += '/'

    for entry in tqdm( table_parsed ):
        if entry[0] != 'All_Reports_2007123.zip':
            """
            The reason for which I perform this check is that this file makes
            little sense. If you check the website, there is such file listed.
            If you look closer, you'll see that the file name is badly formed
            (only one digit for the day, right before the dot). If you check
            the contents of this file and compare them with the file
            'All_Reports_20071231.zip' (with the name correctly formed), you'll
            see that the badly named file has outdated data. Hence I discard
            it.
            """
            urlretrieve(entry[3], download_location + entry[0])
