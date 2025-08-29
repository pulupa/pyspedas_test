# Levels of RFS data

# We can load the data using pyspedas

import pyspedas.projects.psp as psp
from pyspedas import tplot_names, tplot, options, get_data
from os import environ

# Use USER and PSP_STAGING_PW environment variables to
# access non-public PSP data from the SSL server

psp.fields(trange=['2022-04-19','2022-04-20'],
                    datatype='rfs_rawspectra',level = 'l1',
                    username = environ.get('USER'),  
                    password=environ.get('PSP_STAGING_PW'),
                    get_support_data=True, time_clip=True, varnames = '*')

tplot_names()

data_rfs_rawspectra = get_data('ch0_re')

print(data_rfs_rawspectra)