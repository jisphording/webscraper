# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# REWRTIE IMAGE PATHS
# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
# This script rewrites the image paths in the combined csv file.
#
# (C) 2023 - Johannes Isphording

# Import modules
import transform_data
import url_to_extract

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# SETTINGS
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

# URL of the web page to extract
path_to_csv = './data/combined_headlines.csv'

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# MAIN PROGRAM
# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

df_webflow = transform_data.load_webflow_csv( path_to_csv )
image_exchange_path = url_to_extract.image_exchange_path()

images = df_webflow[ 'Bildergalerie' ]

for image, path in enumerate( images ):
    if path != ' ' and not path.startswith( 'https' ):
        images[ image ] = image_exchange_path + path
    else:
        pass

# save the combined dataframe as a csv file
df_webflow.to_csv( 'data/combined_images.csv', index=False )