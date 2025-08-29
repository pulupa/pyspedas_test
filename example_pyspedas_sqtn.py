import pyspedas.projects.psp as psp
from pyspedas import tnames, tplot, options, get_data

psp.fields(trange=['2022-05-15','2022-06-15'],
                    datatype='sqtn_rfs_V1V2',level = 'l3', 
                    get_support_data=True, time_clip=True)

options('electron_density', 'ylog', True)
options('electron_core_temperature', 'ylog', True)

tplot(['electron_density','electron_core_temperature'])