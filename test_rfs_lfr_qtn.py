import pyspedas.projects.psp as psp
from pyspedas import tnames, tplot, options, get_data

psp.fields(trange=['2022-05-15','2022-06-15'],
           datatype='rfs_lfr_qtn',level = 'l3', 
           get_support_data=True, time_clip=True)

options('N_elec', 'ylog', True)

tplot(['N_elec'])