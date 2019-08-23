from __future__ import division
from io import BytesIO
# import zipfile
import pandas as pd
import requests

var_defitions = """\
Variable name:	Variable definition

countrycode:	3-letter ISO country code
country:	Country name
year:		Year

cgdppc:		Real GDP per capita in 2011US$,
		multiple benchmarks (suitable for cross-country income comparisons)

rgdpnapc:	Real GDP per capita in 2011US$,
		2011 benchmark (suitable for cross-country growth comparisons)

pop:	Population, mid-year (thousands)

i_cig:	0/1/2:
	0: observation is extrapolated
	1: benchmark
	2: interpolated

i_bm:	For benchmark observations:
	1: ICP PPP estimates
	2: Historical income benchmarks
	3: Real wages and urbanization
	4: Multiple of subsistence
	5: Braithwaite (1968) PPPs

* Note: real GDP per capita figures are rounded to the nearest dollar, population figures are rounded to the nearest 1000.
* Note: Data for 'selected sub-national units with long time series' are NOT included."""



def _get_mpd_data(base_url, version):
    """Download the Maddison data."""
    tmp_url = base_url + '/mpd' + str(version) + '.dta'
    tmp_buffer = requests.get(url=tmp_url)
    with open('mpd' + str(version) + '.dta', "wb") as data:
        data.write(tmp_buffer.content)


def _download_mpd_data(base_url, version):
    """Download the Maddison data."""
    _get_mpd_data(base_url, version)


def load(base_url='http://www.rug.nl/ggdc/historicaldevelopment/maddison/data/',
                  version=2018, multi_index=False, description=False):
    """
    Load the Maddison data as a pandas DataFrame object.

    Parameters
    ----------
        base_url : str, optional(default='http://www.rug.nl/ggdc/historicaldevelopment/maddison/data/')
            Base url to use for the download.
        version : int, optional(default=2018)
            Version number for Maddison data.
        multi_index : boolean, optional (default=False)
            MultiIndex with countrycode and year as row labels
        description : boolean, optional (default=False)
            Shows variable definitions

    Returns
    -------
        pd.DataFrame containing the Maddison data.

    """
    try:
        mpd_data = pd.read_stata('mpd' + str(version) + '.dta')

    except IOError:
        _download_mpd_data(base_url, version)
        mpd_data = pd.read_stata('mpd' + str(version) + '.dta')

    # year as int
    mpd_data.year = mpd_data.year.astype('int')

    # MultiIndex
    mpd_data_multi = mpd_data.set_index(['countrycode', 'year'])

    # return value
    if description == True:
        print(var_defitions)
    elif (description == False) & (multi_index==False):
        return mpd_data
    elif (description == False) & (multi_index==True):
        return mpd_data_multi
