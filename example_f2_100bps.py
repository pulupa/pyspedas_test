import pyspedas.projects.psp as psp
from pyspedas import tnames, tplot, options, get_data, tplot_names, time_string
import numpy as np
import pandas as pd

# Load the F2 100bps data

psp.fields(trange=['2025-06-14/00:00','2025-06-25/00:00'],
                    datatype='f2_100bps', 
                    get_support_data=True)

# Print the list of variables

print(tnames())

# The DFB VDC variables are included in the list
# Before we plot, change the colors so we can tell them apart

options('PSP_FLD_L2_F2_100bps_DFB_VDC_V1', 'colors', 'red')
options('PSP_FLD_L2_F2_100bps_DFB_VDC_V2', 'colors', 'blue')
options('PSP_FLD_L2_F2_100bps_DFB_VDC_V3', 'colors', 'green')
options('PSP_FLD_L2_F2_100bps_DFB_VDC_V4', 'colors', 'orange')

# Make a plot

tplot(['PSP_FLD_L2_F2_100bps_DFB_VDC_V1',
       'PSP_FLD_L2_F2_100bps_DFB_VDC_V2',
       'PSP_FLD_L2_F2_100bps_DFB_VDC_V3',
       'PSP_FLD_L2_F2_100bps_DFB_VDC_V4'])

# Extract the V1 data

time, data = get_data('PSP_FLD_L2_F2_100bps_DFB_VDC_V1')

# Create a pandas DataFrame

df = pd.DataFrame(data)

# Add a datetime column (PySPEDAS internal times are nanosecond Unix timestamps)

df['Time'] = pd.to_datetime(time, unit='s')

# Set Time as the index for time-series operations

df.set_index('Time', inplace=True)

# see the first few values

print(df.head())
