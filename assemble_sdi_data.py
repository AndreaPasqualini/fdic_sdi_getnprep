#!/usr/bin/python3

import sys
import os
import re
import json
from tqdm import tqdm
import pandas as pd
from zipfile import ZipFile


#%% Function definitions

def dict_reverse_lookup(e, d):
    """
    This function walks the contents of a dict and returns all keys of 'd'
    where element 'e' is found.
    """
    assert isinstance(d, dict)
    r = []
    for k, v in d.items():
        if e in v:
            r.append(k)
    return r


def extract_vars(var_names, csv_file, zip_file):
    zf = ZipFile(zip_file, mode='r')
    cf = zf.open(csv_file)
    var_names.insert(0, 'fed_rssd')
    col_filter = lambda x: x.lower() in var_names
    table = pd.read_csv(cf, index_col=False, usecols=col_filter, encoding='cp1252')
    table.columns = map(str.lower, table.columns)
    return table.set_index('fed_rssd', verify_integrity=True)


def extract_vars_period(var_csv_dict, zip_file, date):
    for i, (report_name, var_list) in enumerate(var_csv_dict.items()):
        csv_filename = 'All_Reports_' + date + '_' + report_name + '.csv'
        chunk = extract_vars(var_list, csv_filename, zip_file)
        if i == 0:
            table = chunk
        else:
            table = table.join(chunk, sort=False)
    return table


def join_variables(var_csv_dict, zip_files):
    date_pattern = re.compile(r'([0-9]{8})')
    for i, zfile in enumerate(tqdm(zip_files)):
        date = date_pattern.search(zfile).group()
        var_data = extract_vars_period(var_csv_dict, zfile, date)
        var_data.insert(0, 'period', date)
        var_data.set_index('period', inplace=True, append=True,
                           verify_integrity=True)
        if i == 0:
            res = var_data
        else:
            res = res.append(var_data, verify_integrity=True, sort=False)
    return res


#%% Parameter settings

if __name__ == '__main__':
    zip_files_dir = sys.argv[1]
    variables_conf_file = sys.argv[2]
    out_file = sys.argv[3]
    if zip_files_dir[-1] != '/':
        zip_files_dir += '/'

    with open(variables_conf_file, mode='r') as json_file:
        var_csv_list = json.load(json_file)

    all_zip_files = next(os.walk(zip_files_dir))[2]
    all_zip_files = [zip_files_dir + zfile for zfile in all_zip_files]

    master = join_variables(var_csv_list, all_zip_files)
    master.reset_index(inplace=True)
    print('Saving the file to disk. This will take a while...')
    master.to_csv(out_file, index=False)
    print('Done.')
