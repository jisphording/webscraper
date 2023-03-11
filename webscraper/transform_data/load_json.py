import pandas as pd

# LOAD JSON
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
def load_json( json ):
    # load json into pandas dataframe
    df_json = pd.read_json( json )

    # create the name 'content' for the first row
    df_json.rename( columns={ df_json.columns[0]: 'Text' }, inplace=True )
    df_json.drop( 'date', axis=1, inplace=True )
    df_json.rename( columns={ df_json.columns[1]: 'Bildergalerie' }, inplace=True )

    return df_json