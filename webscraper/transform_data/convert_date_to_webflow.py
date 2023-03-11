import pytz

# CONVERT DATE TO WEBFLOW 
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
def convert_date_to_webflow( df, column='Datum' ):
    # SETTINGS
    webflow_date_df = df

    # METHODS
    def convert_date( date ):
        # convert the date to the timezone of the webflow CMS
        local_tz = pytz.timezone( 'Europe/Berlin' )
        target_tz = pytz.timezone( 'UTC' )
        
        # normalize the date to the local timezone
        local_date = local_tz.localize( date )

        return local_date.astimezone( target_tz )

    # MAIN PROGRAM
    # iterate over the dataframe and convert the dates in the specified column to the webflow timezone format
    for i in range( len( df[ column ] ) ):
        try:
            # if a date was found, convert it to the webflow timezone
            date = df[ column ][ i ]
            df[ column ][ i ] = convert_date( date ).strftime( '%a %h %d %Y %H:%M:%S GMT+0000 (Coordinated Universal Time)' )
        except:
            # if no date was found, insert an empty string
            date = ''

    return webflow_date_df