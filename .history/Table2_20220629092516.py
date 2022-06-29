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
print(company)

rando = conn.raw_sql("""select permno, date, prc, ret, shrout 
                        from crsp.msf 
                        where permno = 14593
                        and date>='01/01/2019'""",
                     date_cols=['date'])
print(rando)
