import pyspedas.projects.psp as psp
from pyspedas import tnames, tplot, options, get_data
from os import environ

trange=['2020-07-11/03:03:00','2020-07-11/03:43:00']
# trange=['2024-11-06/17:30:00','2024-11-06/19:30:00']


psp.fields(trange=trange, level = 'l3',
           datatype='rfs_hfr',
           time_clip=True)

psp.fields(trange=trange, level = 'l3',
           datatype='rfs_lfr',
           time_clip=True)

psp.fields(trange=trange,
           datatype='sc_pse',
           time_clip=True,
           username = environ.get('USER'), 
           password = environ.get('PSP_STAGING_PW'))

psp.fields(trange=trange, level = 'l1',
           datatype='ephem_spp_VSO',
           time_clip=True,
           username = environ.get('USER'), 
           password = environ.get('PSP_STAGING_PW'))

tplot(['psp_fld_l3_rfs_hfr_auto_averages_ch0_V1V2',
       'psp_fld_l3_rfs_lfr_auto_averages_ch0_V1V2',
       'psp_fld_sc_pse_5hz_POSY_PRI_CURR_A',
       'position'])

p = get_data('position')

print(p)