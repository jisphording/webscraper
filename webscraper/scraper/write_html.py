import os

# WRITE HTML TO DISK
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
def write_html( content, path ):
    file_name = 'index'
    # set filetype
    file_type = 'html'

    # to write html has to be a string
    content = content.prettify()

    # test if file already exists
    if os.path.exists( path + '/' + file_name + '.' + file_type ):
        print( "File already exists, skipping..." )
        return
        
    # else, create the file
    else:
        if not os.path.exists( path ):
            os.makedirs( path )
        print( "Writing '" + path + "/" + file_name + "." + file_type + "' to disk..." )
        # write the file
        with open( path + '/' + file_name + '.' + file_type , 'w', encoding="utf-8" ) as f:
            f.write( content )     