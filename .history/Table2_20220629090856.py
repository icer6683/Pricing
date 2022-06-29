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

company = conn.get_table(library='comp', table='company', obs=10)
print(company)
