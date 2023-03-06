import requests
from bs4 import BeautifulSoup as bs

# GET HTML
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
#
def get_html( url, wait= 1 ):
    # initialize a session
    session = requests.Session()
    # set the User-agent as a regular browser
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

    # get the HTML content
    html = session.get( url, timeout= wait ).content

    # parse HTML using beautiful soup
    soup = bs( html, "html.parser" )

    return soup