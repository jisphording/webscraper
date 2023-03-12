from .extract_date_from_string import extract_date
from .remove_date_from_string import remove_date_from_string
from .regex_date import regex_date

# EXTRACT DATES FROM JSON
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
def extract_dates_from_json( df_json ):
    # extract the dates from the json content
    table_data = [ extract_date( x ) for x in df_json['Text'] ]

    # insert a new column at the beginning of the dataframe
    df_json.insert( 0, 'Datum', '' )

    # insert the extracted dates into the new column
    for i in range( len( table_data ) ):
        df_json.loc[i, 'Datum'] = table_data[ i ]

    return df_json