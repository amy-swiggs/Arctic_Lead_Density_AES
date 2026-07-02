# Arctic Lead Density AES
Code for reproducing the figures in the manuscript titled
'Regional and Temporal Variability in Arctic Lead Density from Multi-Mission Satellite Altimetry', submitted to Journal of Geophysical Research: Oceans on 30/06/2026.

All data used in the study are available from open sources listed below. The methods for generating lead density from CS2, IS2, and S3 is outlined in the manuscript.

## Raw Data
**ICESat-2**\
ATL07 along-track sea ice data, downloaded from Earthdata using Earthaccess\
[User Guide](https://nsidc.org/sites/default/files/documents/user-guide/atl07-v007-userguide.pdf) |
[ATBD](https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl07_10_20_21_atbd_v007.pdf) |
[Data Dictionary](https://nsidc.org/sites/default/files/documents/technical-reference/icesat2_atl07_data_dict_v007.pdf) |
[Earth Access Documentation](https://earthaccess.readthedocs.io/en/latest/) |\
Thanks to Earth Access for the very useful documentation for downloading and processing IS2 data

**CryoSat-2**\
ESA Level 1B sea ice data, processed according to the CPOM sea ice processing chain\
Thanks to Ben Palmer, Alan Muir, and Andy Ridout for their effort in making the CPOM sea ice processing chain open-access\
Data available for download from ESA via [ftp](https://earth.esa.int/eogateway/catalog/cryosat-products)\
[CPOM Processing Chain](https://github.com/CPOM-Altimetry) |
[Tilling et al. (2018)](https://www.sciencedirect.com/science/article/pii/S0273117717307901) |


**Sentinel-3**\
ESA Level 1B sea ice data, processed according to the CPOM sea ice processing chain\
The harmonisation of Sentinel-3 and CryoSat-2 was inspired by [Lawrence et al. (2019)](https://www.sciencedirect.com/science/article/abs/pii/S0273117719307458?via%3Dihub) \
Data available for download from ESA via [Copernicus](https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-3) \
[CPOM Processing Chain](https://github.com/CPOM-Altimetry) |
[Tilling et al. (2018)](https://www.sciencedirect.com/science/article/pii/S0273117717307901) |


## Evaluation Data
**MODIS**\
MODIS lead fractions are from [Willmes et al. (2023)](https://tc.copernicus.org/articles/17/3291/2023/tc-17-3291-2023.html)|\
Data available for download from [PANGAEA](https://doi.pangaea.de/10.1594/PANGAEA.955561) | 

**Landsat 8**\
Landsat 8 lead density was determined using methodology outlined in [Swiggs et al. (2024)](https://ieeexplore.ieee.org/document/10758740) |\
Landsat 8 imagery are available for download from [USGS Earth Explorer](https://earthexplorer.usgs.gov/) | 


