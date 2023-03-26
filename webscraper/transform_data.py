# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# TRANSFORM DATA
# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
# This tool transforms the data from the web scraper into a format that can be ingested 
# into the Webflow CMS.
#
# (C) 2023 - Johannes Isphording

# Import custom modules
import url_to_extract
import transform_data

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# SETTINGS
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

# URL of the web page to extract
path = url_to_extract.path()
json = url_to_extract.json()

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# MAIN PROGRAM
# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
df_webflow = transform_data.load_webflow_csv( path )
df_json = transform_data.load_json( json )

extracted_dates = transform_data.extract_dates_from_json( df_json )
transform_data.convert_date_to_webflow( extracted_dates )

df_combined = df_webflow.append( extracted_dates, ignore_index=True )

print( df_combined )

# save the combined dataframe as a csv file
df_combined.to_csv( 'data/combined.csv', index=False )
