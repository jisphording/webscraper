import pandas as pd
from .import_csv import import_csv

# LOAD WEBFLOW CSV
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
def load_webflow_csv( path ):
    # load the Webflow export csv data into a pandas dataframe
    data_table = import_csv( path )
    df = pd.DataFrame( data_table )
    
    return df