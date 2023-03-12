# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# SCRAPER
# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
# This is a custom scraping tool to pull content from websites that are transitioned
# to another CMS
#
# (C) 2023 - Johannes Isphording

# Import custom modules
import url_to_extract
import scraper

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# SETTINGS
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

# URL of the web page to extract
url = url_to_extract.url()

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
# MAIN PROGRAM
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

# Get HTML
html = scraper.get_html( url )

scraper.write_html( html, './data/' )