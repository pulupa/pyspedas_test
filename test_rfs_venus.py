import pyspedas.projects.psp as psp
from pyspedas import tnames, tplot, options, get_data
from os import environ

trange=['2024-11-06/17:30:00','2024-11-06/19:30:00']

psp.fields(trange=trange,
           datatype='rfs_lfr',
           varnames = 'psp_fld_l2_rfs_lfr_auto_averages_ch0_V1V2',
           time_clip=True,
           username = environ.get('USER'),  
           password = environ.get('PSP_STAGING_PW'))


psp.fields(trange=trange,
           datatype='sc_pse',
           varnames = '*',
           time_clip=True,
           username = environ.get('USER'), 
           password = environ.get('PSP_STAGING_PW'))


tplot(['psp_fld_l2_rfs_lfr_auto_averages_ch0_V1V2',
       'psp_fld_sc_pse_5hz_POSY_PRI_CURR_A'])