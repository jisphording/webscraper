from datetime import datetime
import re

from .regex_date import regex_date

# EXTRACT DATE FROM STRING
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
def extract_date( string ):
    # METHODS
    def transform_date( string ):
        
        try:
            # remove the dots from the date before splitting it
            string = string.replace( '.', '' )
            # split date into day, month and year
            date = string.split( ' ' )

            # convert the month to a number
            months = { 'Januar': 1, 'Februar': 2, 'März': 3, 'April': 4, 'Mai': 5, 'Juni': 6, 'Juli': 7, 'August': 8, 'September': 9, 'Oktober': 10, 'November': 11, 'Dezember': 12 }
            date[1] = months[ date[1] ]

            # convert the date to a datetime object
            date = datetime( int( date[2] ), int( date[1] ), int( date[0] ) )

        except AttributeError:
            date = None

        return date
    
    def date_found( match_str, regex_result ):
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