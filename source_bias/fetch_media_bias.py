import requests
from bs4 import BeautifulSoup

def fetch_media_bias(source):
    '''request allsides.com to get the media bias.

    Parameters:
    source (str): the media source to search

    Return:
    side (str): the side of the media. Could be left, left-centered, centered, right-centered, right. Would choose the most frequently one if more than one of the media is searched.
    status (bool): Will return False if bad status code or could not find any media. Else, return side
    '''
    # allsides wedsite
    webpage = f"https://www.allsides.com/media-bias/ratings?field_featured_bias_rating_value=All&field_news_source_type_tid%5B%5D=1&field_news_source_type_tid%5B%5D=2&field_news_source_type_tid%5B%5D=3&field_news_source_type_tid%5B%5D=4&field_news_bias_nid_1%5B1%5D=1&field_news_bias_nid_1%5B2%5D=2&field_news_bias_nid_1%5B3%5D=3&title={source}"
    x = requests.get(webpage)
    # check status code
    if x.status_code != 200:
        return False
    else:
        soup = BeautifulSoup(x.text, 'html.parser')
        # find all media names in the table
        # names = [i.text for i in soup.findAll("td", {"class": "views-field views-field-title source-title"})]
        # names = [i.strip() for i in names] # strip 
        # find the corresponding bias
        bias = [i.find("a")['href'] for i in soup.findAll("td", {"class" :"views-field views-field-field-bias-image"})]
        bias = [i[i.rfind("/")+1:] for i in bias]
        
        if len(bias) == 0:
            return False
        else:
            # compute most frequent bias
            side = max(set(bias), key = bias.count)
            return side
