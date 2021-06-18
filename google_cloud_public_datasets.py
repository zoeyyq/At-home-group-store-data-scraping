from google.cloud import bigquery
import geopandas
import numpy as np
import pandas as pd
import json
from shapely import wkt
from shapely import geometry
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
project_id = 'cloud-public-datasets-program'
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

client = bigquery.Client(project = project_id)