#Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# url for site to be scraped
url = 'https://mars.nasa.gov/news/'
browser.visit(url)



# Mars News

html = browser.html
soup = bs(html, 'html.parser')

#browser click link for first article
browser.links.find_by_partial_text("Join NASA")

html = browser.html
soup = bs(html, 'html.parser')

results = soup.find_all('div', class_="grid_layout")
# print(results)

for result in results:
    title = result.find('h1', class_="article_title")
#     print(title)
    title_text = title.text
    print(title_text)
    paragraph = result.find('p')
#     print(paragraph)
    p_text = paragraph.text
    print(p_text)
        




# JPL Mars Space Images - Featured Image

# url for site to be scraped
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

#browser click full image button
browser.click_link_by_text('FULL IMAGE')

html = browser.html
soup = bs(html, 'html.parser')

browser.click_link_by_text('more info')

results = soup.find('div', class_="grid_layout")
print(results)

full_image_url = soup.find('a', class_='main_image')
print(full_image_url)





# Mars Weather

# url to be scraped
url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')

# find the latest tweet
results = soup.find('div', class_="css-1dbjc4n")
print(results)

for result in results:
    latest_tweet = result.find('div', class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0")
    print(latest_tweet)

# print the text from the tweet
mars_weather = latest_tweet.text
print(mars_weather)





# Mars Facts

# url to be scraped
url = 'https://space-facts.com/mars/'
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')

# main = soup.find('table', id='tablepress-p-mars-no-2')
# main

mars_facts = pd.read_html(url)
mars_facts





# Mars Hemispheres

# url to be scraped
hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemispheres_url)

html = browser.html
soup = bs(html, 'html.parser')

# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image
results = soup.find('div', class_="collapsible results")
print(results)

# generate list of mars hemisphere image urls

url_list = []
for result in results.find_all('a', href=True): 
    if result.text: 
        full_image_url = (f"{hemispheres_url}result.text")
        url_list.append(full_image_url)
        image_title = results.find('h3')
        
print(url_list)

# Close the browser after scraping
browser.quit()

# Return results
#return mars_data

