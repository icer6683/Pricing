##########################################
# Pricing/Mispricing Paper Table 2       #
# Andrew Lou                             #
# Date: June 28 2022                     #
##########################################

# package imports
from tkinter import Y
import pandas as pd
import numpy as np
import datetime as dt
import wrds
import matplotlib.pyplot as plt
from dateutil.relativedelta import *
from pandas.tseries.offsets import *
from scipy import stats

# connect to WRDS
conn = wrds.Connection()

company = conn.get_table(library='comp', table='company',
                         columns=['cik'], obs=10)

rando = conn.raw_sql("""select permno, date, prc, ret, shrout 
                        from crsp.msf 
                        where permno = 14593
                        and date>='01/01/2019'""",
                     date_cols=['date'])

apple_fund = conn.raw_sql("""select a.gvkey, a.iid, a.datadate, a.tic, a.conm,
                            a.at, b.prccm, b.cshoq 
                            
                            from comp.funda a 
                            inner join comp.secm b 
                            
                            on a.gvkey = b.gvkey
                            and a.iid = b.iid
                            and a.datadate = b.datadate 
                            
                            where a.tic = 'AAPL' 
                            and a.datadate>='01/01/2010'
                            and a.datafmt = 'STD' 
                            and a.consol = 'C' 
                            and a.indfmt = 'INDL'
                            """, date_cols=['datadate'])

print(apple_fund)
apple_fund.to_pickle("/Pricing/apple_fund.pkl")
apple_fund.to_csv('/Pricing/apple_fund.csv')
apple_fund.to_stata('/Pricing/apple_fund.dta')
