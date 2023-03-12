import re

# REMOVE DATE FROM STRING
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
def remove_date_from_string( string, regex_date ):
    # remove the extracted date from the string if there is a match
    try:
        string = re.sub( regex_date, '', string )
    except TypeError:
        pass

    return string