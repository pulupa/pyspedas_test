import pyspedas.projects.psp as psp
from pyspedas import tnames, tplot, options, get_data

trange = ['2025-09-10','2025-09-21']

psp.fields(trange=trange,
           datatype='sqtn_rfs_V1V2',level = 'l3', 
           username = 'hello', password = 'world',
           get_support_data=True, time_clip=True, prefix='psp_fld_l3_sqtn_rfs_V1V2')

psp.fields(trange=trange,
           datatype='sqtn_rfs_V3V4',level = 'l3', 
           username = 'hello', password = 'world',
           get_support_data=True, time_clip=True, prefix='psp_fld_l3_sqtn_rfs_V3V4')

options('*electron_density', 'ylog', True)
options('*electron_core_temperature', 'ylog', True)

tplot(['*electron_density','*electron_core_temperature'])