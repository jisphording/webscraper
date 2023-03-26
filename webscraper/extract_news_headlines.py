# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# EXTRACT NEWS HEADLINES
# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
# This script is used to generate missing news/blog entry headlines from post content.
#
# (C) 2023 - Johannes Isphording

# Import modules
import transform_data
import re

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# SETTINGS
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

# URL of the web page to extract
path_to_csv = './data/combined.csv'

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# MAIN PROGRAM
# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

df_webflow = transform_data.load_webflow_csv( path_to_csv )

text = df_webflow[ 'Text' ]
name = df_webflow[ 'Name' ]
slug = df_webflow[ 'Slug' ]

for i, t in enumerate( text ):
    if t != ' ':
        # Create headline from text
        headline = transform_data.summarize_text( t )
        headline = headline.strip()
        headline = headline[:256] # max 256 characters
        name[ i ] = headline

        # Create slug from headline
        slug[ i ] = headline.lower().replace( ' ', '-' )
        # remove all non-alphanumeric characters except for dashes
        slug[ i ] = re.sub( r'[^a-zA-Z0-9-]', '', slug[ i ] )
    else:
        name[ i ] = 'EMPTY'
        slug[ i ] = 'EMPTY'

print( df_webflow )

# save the combined dataframe as a csv file
df_webflow.to_csv( 'data/combined_headlines.csv', index=False )