import pyspedas.projects.psp as psp
from pyspedas import tplot, options

# Load data during a rotation

trange = ['2020-08-05/12:00', '2020-08-05/20:00']
psp.fields(trange=trange, time_clip=True, datatype='rfs_hfr', level='l3')

# Set scale to show variation during rotation

options('psp_fld_l3_rfs_hfr_auto_averages_ch0_V1V2', 'zrange', [1e-17,5e-17])

# Filter out data during rotation

psp.filter_fields('psp_fld_l3_rfs_hfr_auto_averages_ch0_V1V2',[8]) 

# Plot data, filtered data, and attitude data showing rotation

tplot(['psp_fld_l3_rfs_hfr_auto_averages_ch0_V1V2',
       'psp_fld_l3_rfs_hfr_auto_averages_ch0_V1V2_008',
       'psp_fld_l3_rfs_hfr_ch0_V1V2_J2000'])