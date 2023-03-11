import csv

# IMPORT CSV FILE
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
# Import a csv file and return a list of dictionaries
def import_csv( path ):
    print( 'Importing csv file...' )
    
    # open the file
    with open( path, 'r', encoding='utf-8' ) as file:
        # read the file
        reader = csv.DictReader( file )
        # create a list of dictionaries
        data = list( reader )
        # return the list of dictionaries
        return data