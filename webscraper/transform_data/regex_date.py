import re

# REGEX MATCH DATE
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
def regex_date( string ):
    # SETTINGS
    match_str = re.search( r'\d{1,2}\.\s\w+\s\d{4}', string )

    # extract the date from the string
    try:
        res = match_str.group()

    except AttributeError:
        res = ''

    return res