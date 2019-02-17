#import all depencencies

from bs4 import BeautifulSoup as bs
import time
import requests

def scrape():

    #this is all a placeholer for now...


#-----------------------------------------------------------------------------------------------------------------#
#Set up URLS 
#-----------------------------------------------------------------------------------------------------------------#

    url_latest_news = "https://mars.nasa.gov/news/"  
    url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"   
    url_twitter = "https://twitter.com/marswxreport?lang=en"   
    url_mars_facts = "http://space-facts.com/mars/"
    url_hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

#-----------------------------------------------------------------------------------------------------------------#      
#-----------------------------------------------------------------------------------------------------------------#   



#-----------------------------------------------------------------------------------------------------------------#
#Set up requests and responses
#-----------------------------------------------------------------------------------------------------------------#

    response_latest_news = requests.get(url_latest_news)
    response_image = requests.get(url_image)
    response_twitter = requests.get(url_twitter)
    response_mars_facts = requests.get(url_mars_facts)
    response_hemisphere = requests.get(url_hemispheres)

#-----------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------#




#-----------------------------------------------------------------------------------------------------------------#
# Set up all the soups
#-----------------------------------------------------------------------------------------------------------------#

    soup_latest_news = bs(response_latest_news.text, "html.parser")
    soup_image = bs(response_image.text, "html.parser")
    soup_twitter = bs(response_twitter.text, "html.parser")
    soup_mars_facts = bs(response_mars_facts.text, "html.parser")
    soup_hemisphere = bs(response_hemisphere.text, "html.parser")

#-----------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------#





#-----------------------------------------------------------------------------------------------------------------#
#Get web scrapings for latest news
#-----------------------------------------------------------------------------------------------------------------#

    #news_title = soup_latest_news.body.find('ul', class_='item_list')
    news_title = 'Some Title'
    latest_news_text = 'Some Text Here. Lots of news.'

#-----------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------#






#-----------------------------------------------------------------------------------------------------------------#
#Get web scrapings for latest image
#-----------------------------------------------------------------------------------------------------------------#

    #soup_image.find_all('div', class_ = 'carousel_items')
    a = soup_image.find_all('div', class_ = 'carousel_items')[0]
    b = a.find('article').attrs['style'].strip()
    url = b.split("'")[1]
    base_url = 'https://www.jpl.nasa.gov'
    latest_image = base_url + url
    latest_image

#-----------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------#






#-----------------------------------------------------------------------------------------------------------------#
#Get web scrapings for latest weather
#-----------------------------------------------------------------------------------------------------------------#

    #soup_twitter.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")

    latest_weather = soup_twitter.find_all('div', class_='js-tweet-text-container')

    for tweet_html in latest_weather:
        tweet = tweet_html.text.strip()
        if tweet.startswith('Sol'): 
            weather = tweet
            break


#-----------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------#





#-----------------------------------------------------------------------------------------------------------------#
#Get web scrapings for mars facts
#-----------------------------------------------------------------------------------------------------------------#

    #mars_facts = soup_mars_facts.find('div', id = 'facts').find_all('strong')
    mars_facts_soup = soup_mars_facts.find('div', id = 'facts').find_all('strong')

    mars_facts = []
    for strong in mars_facts_soup:
        mars_facts.append(strong.text)


#-----------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------#




#-----------------------------------------------------------------------------------------------------------------#
# Images for Hemispheres go here
#-----------------------------------------------------------------------------------------------------------------#


    hemisphere_image_urls = []
    hemis = soup_hemisphere.find_all("img")

    for alt in hemis:
        if alt['alt'].find('Hemi') != -1:
            hemisphere_image_urls.append({'title':alt['alt'][:-19],'img_url':alt['src']})
    hemisphere_image_urls


#-----------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------------------#
# Store all data for Mongo Export
#-----------------------------------------------------------------------------------------------------------------#

    mars_data = {
        'Title' : news_title,
        'News' : latest_news_text,
        'Featured_Image' : latest_image,
        'Current_Weather' : weather,
        'Facts' : mars_facts,
        'Hemispheres' : hemisphere_image_urls

    }



    return mars_data


if __name__ == '__main__':
    print(scrape())

