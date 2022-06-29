##########################################
# Pricing/Mispricing Paper Table 2       #
# Andrew Lou                             #
# Date: June 28 2022                     #
##########################################

# package imports
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

crsp_m = conn.raw_sql("""
                      select a.permno, a.permco, a.date, b.shrcd, b.exchcd,
                      a.ret, a.retx, a.shrout, a.prc
                      from crsp.msf as a
                      left join crsp.msenames as b
                      on a.permno=b.permno
                      and b.namedt<=a.date
                      and a.date<=b.nameendt
                      where a.date between '01/01/1968' and '12/31/2021'
                      and b.exchcd between 1 and 3
                      """, date_cols=['date'])

# change variable format to int
crsp_m[['permco', 'permno', 'shrcd', 'exchcd']] = crsp_m[[
    'permco', 'permno', 'shrcd', 'exchcd']].astype(int)

# Line up date to be end of month
crsp_m['jdate'] = crsp_m['date']+MonthEnd(0)

# add delisting return
dlret = conn.raw_sql("""
                     select permno, dlret, dlstdt 
                     from crsp.msedelist
                     """, date_cols=['dlstdt'])

dlret.permno = dlret.permno.astype(int)
# dlret['dlstdt']=pd.to_datetime(dlret['dlstdt'])
dlret['jdate'] = dlret['dlstdt']+MonthEnd(0)

crsp = pd.merge(crsp_m, dlret, how='left', on=['permno', 'jdate'])
crsp['dlret'] = crsp['dlret'].fillna(0)
crsp['ret'] = crsp['ret'].fillna(0)

# retadj factors in the delisting returns
crsp['retadj'] = (1+crsp['ret'])*(1+crsp['dlret'])-1

# calculate market equity
crsp['me'] = crsp['prc'].abs()*crsp['shrout']
crsp = crsp.drop(['dlret', 'dlstdt', 'prc', 'shrout'], axis=1)
crsp = crsp.sort_values(by=['jdate', 'permco', 'me'])

print(crsp)
