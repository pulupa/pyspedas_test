import pyspedas.projects.psp as psp
from pyspedas import tnames, tplot, options, get_data
from os import environ

trange=['2025-01-01/12:00:00','2025-01-01/13:00:00']

psp.fields(trange=trange,
           datatype='mag_RTN_4_Sa_per_Cyc',
           time_clip=True,
           username = 'none', 
           password = 'none')

print(tnames())

tplot('psp_fld_l2_mag_RTN_4_Sa_per_Cyc')