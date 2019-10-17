# Explanations file for `pull_variables.json`

**Disclaimer:** the short description is inaccurate as it's just supposed to give a quick'n'dirty idea of the meaning of the variable.
Please check the [FDIC SDI Glossary](https://www5.fdic.gov/sdi/main.asp?formname=glossary) for precise information.


## Demographic variables

These variables are found in every CSV file.
For convenience and reliability, the Python program will get them from the Assets and Liabilities CSV file.


| Variable name     | Description |
|-------------------|-------------|
| `cert`            | FDIC Certificate no. |
| `docket`          | OTS docket no. |
| `fed_rssd`        | FED ID no. (RSSD) |
| `rssdhcr`         | RSSD of the top bank-holding company |
| `name`            | Institution name |
| `city`            | City |
| `stalp`           | State |
| `zip`             | ZIP code |
| `repdte`          | Report date |
| `rundate`         | Run date |
| `bkclass`         | Bank charter class |
| `address`         | Physical street address |
| `namehcr`         | Name of the top bank-holding company |
| `offdom`          | No. of domestic US offices |
| `offfor`          | No. of foreign offices |
| `stmult`          | Interstate branches |
| `specgrp`         | Asset concentration hierarchy |
| `subchaps`        | Subchapter S corporations |
| `county`          | County |
| `cbsa_metro`      | MSA no. based on 2000 census |
| `cbsa_metro_name` | MSA no. based on 2000 census |
| `estymd`          | Established date |
| `insdate`         | Date of deposit insurance |
| `effdate`         | Last structure change effective date |
| `mutual`          | Mutual ownership flag |
| `parcert`         | Directly owned by another bank (CERT) |
| `trust`           | Trust powers |
| `regagnt`         | Regulator |
| `insagnt1`        | Insurance fund membership |
| `fdicdbs`         | FDIC regions |
| `fdicsupv`        | FDIC supervisory region  |
| `fldoff`          | FDIC field office |
| `fed`             | FED district |
| `occdist`         | Office of the Comptroller district |
| `otsregnm`        | Office of Thrift supervision region (prior 21-Jul-2011) |
| `offoa`           | No. of offices in insured other areas |
| `cb`              | FDIC community banks |
| `webaddr`         | Primary internet web address |


## Financial variables

Variables related to balance sheet and income statement figures.
Each variable belongs to at least one CSV file.

| Source CSV table       | Variable name | Short description                                      |
|------------------------|---------------|--------------------------------------------------------|
| Assets and Liabilities | `numemp`      | FTE no. of workers                                     |
| Assets and Liabilities | `asset`       | Total assets (book value)                              |
| Assets and Liabilities | `sc`          | Securities                                             |
| Assets and Liabilities | `bkprem`      | Equipment and premises                                 |
| Assets and Liabilities | `ore`         | Other real estate                                      |
| Assets and Liabilities | `intan`       | Intangibles and goodwill                               |
| Assets and Liabilities | `liabeq`      | Total liabilities and equity (book value)              |
| Assets and Liabilities | `liab`        | Total liabilities                                      |
| Assets and Liabilities | `dep`         | Total deposits                                         |
| Assets and Liabilities | `eqtot`       | Total equity                                           |
| Assets and Liabilities | `frepo`       | Fedfunds and repos (assets)                            |
| Assets and Liabilities | `frepp`       | Fedfunds and repos (liabilities)                       |
| Assets and Liabilities | `rwajt`       | Risk-weighted assets                                   |
| Assets and Liabilities | `rbct1j`      | Tier 1 (core) capital                                  |
| Net Loans and Leases   | `lnlsnet`     | Loans and leases, net                                  |
| Net Loans and Leases   | `lnatres`     | Loans and leases loss allowances                       |
| Net Loans and Leases   | `lnlsgr`      | Loans and leases, gross                                |
| Total Interest Income  | `intinc`      | Total interest income                                  |
| Total Interest Income  | `ilndom`      | Interest income from domestic loans                    |
| Total Interest Income  | `ilnfor`      | Interest income from foreign loans                     |
| Total Interest Expense | `eintexp`     | Total interest expense                                 |
| Total Interest Expense | `edepdom`     | Interest expense from deposits                         |
| Total Interest Expense | `efrepp`      | Interest expense from fedfunds and repos (liabilities) |
| Income and Expense     | `nim`         | Net interest margin                                    |
| Income and Expense     | `nonii`       | Non-interest income                                    |
| Income and Expense     | `esal`        | Wages and salaries                                     |
| Income and Expense     | `epremagg`    | Expenses on premises and fixed assets                  |
| Income and Expense     | `ideoth`      | Non-interest, operating expenses                       |
| Income and Expense     | `idpretx`     | Net income before taxes                                |
| Income and Expense     | `eqcdiv`      | Cash dividends to equity holders                       |
| Income and Expense     | `noij`        | Net operating income                                   |
