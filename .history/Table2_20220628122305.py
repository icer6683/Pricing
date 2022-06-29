##########################################
# Pricing/Mispricing Paper Table 2       #
# Andrew Lou                             #
# Date: June 28 2022                     #
##########################################
import pandas as pd
import numpy as np
import datetime as dt
import wrds
import matplotlib.pyplot as plt
from dateutil.relativedelta import *
from pandas.tseries.offsets import *
from scipy import stats

conn = wrds.Connection()
