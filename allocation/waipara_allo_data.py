# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:47:54 2018

@author: MichaelEK
"""
import os
import pandas as pd
from pdsql import mssql
from allotools import AlloUsage
from datetime import datetime

pd.options.display.max_columns = 10


############################################
### Parameters

server = 'edwprod01'
database = 'hydro'
sites_table = 'ExternalSite'

#catch_group = ['Ashburton River']
gwaz = ['Waipara']
summ_col = 'GwazName'

#crc_filter = {'use_type': ['stockwater', 'irrigation']}

datasets = ['allo']

freq = 'M'

from_date = '2010-10-01'
to_date = '2010-10-31'

py_path = os.path.realpath(os.path.dirname(__file__))

plot_dir = 'plots'
export2 = 'Waipara_allo.csv'
export3 = 'Waipara_allo_pivot.csv'

now1 = str(datetime.now().date())

plot_path = os.path.join(py_path, plot_dir)

if not os.path.exists(plot_path):
    os.makedirs(plot_path)

############################################
### Extract data

#sites1 = mssql.rd_sql(server, database, sites_table, ['ExtSiteID', summ_col], where_in={summ_col: gwaz})

#site_filter = {'SwazName': sites1.SwazName.unique().tolist()}

a1 = AlloUsage(from_date, to_date, site_filter={summ_col: gwaz}, crc_filter={'take_type': ['Take Groundwater']})

combo_ts = a1.get_ts(datasets, freq, [summ_col, 'date'])

combo_ts.to_csv(os.path.join(py_path, export2))


allo1 = a1.allo.copy()


#########################################
### Plotting

### Grouped
## Lumped
a1.plot_group('A-JUN', group=summ_col, export_path=plot_path)


### Stacked
## lumped
a1.plot_stacked('A-JUN', group=summ_col, export_path=plot_path)



