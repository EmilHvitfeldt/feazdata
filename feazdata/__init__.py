import pandas
from pkg_resources import resource_filename as _rf

ames = pandas.read_csv(_rf("feazdata", "data/ames.csv"))
