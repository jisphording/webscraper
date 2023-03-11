from datetime import datetime
import re

# EXTRACT DATE FROM STRING
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
def extract_date( string ):
    # SETTINGS
    match_str = re.search( r'\d{1,2}\.\s\w+\s\d{4}', string )

    # METHODS
    def transform_date( string ):
        
        # split date into day, month and year
        date = string.split( ' ' )

        # convert the month to a number
        months = { 'Januar': 1, 'Februar': 2, 'März': 3, 'April': 4, 'Mai': 5, 'Juni': 6, 'Juli': 7, 'August': 8, 'September': 9, 'Oktober': 10, 'November': 11, 'Dezember': 12 }
        date[1] = months[ date[1] ]

        # convert the date to a datetime object
        date = datetime( int( date[2] ), int( date[1] ), int( date[0] ) )

        return date

    def regex_date( string ):
        # extract the date from the string
        try:
            res = match_str.group().replace( '.', '' )
        except AttributeError:
            res = None

        return res
    
    def date_found( string, regex_result ):
        # test if a date was actually found
        if match_str is not None:
            transformed_date = transform_date( regex_result )
        else:
            transformed_date = ''

        return transformed_date
            
    # MAIN PROGRAM
    regex_result = regex_date( string )
    extracted_date = date_found( string, regex_result )

    return extracted_date