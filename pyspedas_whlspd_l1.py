import pyspedas
from pytplot import tplot, options, tplot_names, get_data
from os import environ

pyspedas.psp.fields(trange=['2022-05-15','2022-06-15'],
                    datatype='sc_hk_high',level = 'l1',
                    username = 'pulupa',  password=environ.get('PSP_STAGING_PW'),
                    get_support_data=True, time_clip=True, varnames = '*')

tplot_names()

data_whlspd0 = get_data('WHLSPD0')

print(data_whlspd0)

tplot(['WHLSPD0','WHLSPD1','WHLSPD2','WHLSPD3'])