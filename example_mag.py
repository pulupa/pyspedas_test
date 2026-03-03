import pyspedas.projects.psp as psp
from pyspedas import tnames, tplot, options, get_data, tplot_names, time_string
import numpy as np

psp.fields(trange=['2024-09-30/14:20','2024-09-30/14:30'],
                    datatype='mag_RTN', 
                    get_support_data=True, time_clip=True)

print(tplot_names())

mag_rtn = get_data('psp_fld_l2_mag_RTN')

print(mag_rtn)

# from the array mag_rtn.y, find a time when the magnetic field value is
# NaN, then print several samples around that time

y_data = mag_rtn.y
time_data = mag_rtn.times

# Find indices where y_data is NaN
nan_indices = np.where(np.isnan(y_data[:, 0]))[0]

if len(nan_indices) > 0:
    # Print several samples around the first NaN value
    start_idx = max(0, nan_indices[0] - 5)
    end_idx = min(len(y_data), nan_indices[0] + 5)
    
    print(f"Found NaN at index {nan_indices[0]}")
    print("Samples around the NaN value:")
    for i in range(start_idx, end_idx):
        print(f"Time: {time_string(time_data[i])}, Magnetic field values: {y_data[i]}")
else:
    print("No NaN values found in the magnetic field data.")

tplot('psp_fld_l2_mag_RTN')
