from numpy import *
from scipy import *
from numpy import *
from scipy import *
from xarray import *
from vtk import *
from PySide6 import *
from pyqtgraph import *
from requests import *
from netCDF4 import *
from fpdf import *             # this is fpdf2
from pdfrw import *
from rapidfuzz import *
from wavespectra import *
from waveresponse import *
from mafredo import *
from nooverlap import *
from PySide6QtAds import *
from PIL import *
from yaml import load, safe_dump, SafeLoader

all = dict(**locals())

for key, value in all.items():
    print(key, value)

print('all imported!')
