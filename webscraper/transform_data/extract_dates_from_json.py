from .extract_date_from_string import extract_date

# EXTRACT DATES FROM JSON
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
def extract_dates_from_json( df_json ):
    # extract the dates from the json data
    table_data = df_json['Text'].to_list()
    for i in range( len( table_data ) ):
        table_data[ i ] = extract_date( table_data[ i ] )

    return table_data