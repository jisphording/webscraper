from .extract_date_from_string import extract_date
from .remove_date_from_string import remove_date_from_string
from .regex_date import regex_date

# EXTRACT DATES FROM JSON
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
def extract_dates_from_json( df_json ):
    # extract the dates from the json content
    #table_data = [ extract_date( x ) for x in df_json['Text'] ]
    #table_text = [ remove_date_from_string( y, regex_result= ) for y in df_json['Text'] ]
    
    # insert a new column at the beginning of the dataframe
    df_json.insert( 0, 'Datum', '' )

    for i in range( len( df_json['Text'] ) ):
        data_cell = df_json.loc[ i, 'Text' ]
        
        df_json.loc[ i, 'Datum' ] = extract_date( data_cell )
        df_json.loc[i, 'Text'] = remove_date_from_string( data_cell, regex_date( data_cell ) )

    return df_json