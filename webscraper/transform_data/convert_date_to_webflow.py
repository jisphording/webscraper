import pytz

# CONVERT DATE TO WEBFLOW 
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
def convert_date_to_webflow( date ):
    # METHODS
    def convert_date( date ):
        # convert the date to the timezone of the webflow CMS
        local_tz = pytz.timezone( 'Europe/Berlin' )
        target_tz = pytz.timezone( 'UTC' )
        
        # normalize the date to the local timezone
        local_date = local_tz.localize( date )

        return local_date.astimezone( target_tz )

    webflow_date_format = convert_date( date ).strftime( '%a %h %d %Y %H:%M:%S GMT+0000 (Coordinated Universal Time)' )

    return webflow_date_format