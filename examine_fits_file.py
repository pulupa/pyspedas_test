import astropy.io.fits as fits

import fitsio
import numpy as np

# Replace 'your_file.fits' with the name of your FITS file
#filename = '/Users/pulupa/Desktop/ulsamap_withsun.fits'
filename = '/Users/pulupa/Desktop/ulsamap_withsun_49.8_Mhz.fits'
#filename = '/Users/pulupa/Desktop/interpolated_ulsa_maps.fits'

try:
    # Open the FITS file as an HDUList
    with fits.open(filename) as hdul:
        print("--- FITS File Structure ---")
        # Use .info() on the HDUList to get a summary of all HDUs
        hdul.info()

        print("\n--- Examining Each HDU ---")
        # Loop through each HDU in the file
        for i, hdu in enumerate(hdul):
            print(f"\nHeader for HDU {i} ({hdu.name}):")

            # Print all header keys and their values
            print(repr(hdu.header))

            # Check if the HDU contains data
            if hdu.data is not None:
                print(f"Data found in HDU {i}.")
                print(f"  Data shape: {hdu.data.shape}")
                print(f"  Data type: {hdu.data.dtype}")
            else:
                print(f"No data found in HDU {i}.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")

print("Reading FITS file with fitsio...")

fname = filename
header      = fitsio.read_header(fname)
fits        = fitsio.FITS(fname,'r')
maps        = fits[0].read()
#self.maps   = maps
print(header)
fstart      = header['freq_start']
fend        = header['freq_end']
fstep       = header['freq_step']
freq   = np.arange(fstart, fend+1e-3*fstep, fstep)

print(freq)
print(maps.shape)

assert (len(freq) == maps.shape[0])
