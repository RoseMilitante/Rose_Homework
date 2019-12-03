# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import time

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    mars_complete_data = {}
    browser = init_browser()

    # NASA Mars News
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)

    html = browser.html
    mars_soup = BeautifulSoup(html, 'html.parser')

    articles = mars_soup.find_all('div', class_="list_text")

    for article in articles:
        news_titles = article.find('div', class_="content_title")
        mars_complete_data['title'] = news_titles.find('a').get_text()
        mars_complete_data['paragraph'] = article.find('div', class_="article_teaser_body").get_text()

    # JPL Mars Space Images
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    jpl_html = browser.html
    jpl_soup = BeautifulSoup(jpl_html, 'html.parser')
    featured_images = jpl_soup.find_all('a', class_='button fancybox')
    images = []
    for image in featured_images:
        photo_references = image['data-fancybox-href']
        images.append(photo_references)
        featured_image_url = "https://www.jpl.nasa.gov" + photo_references
        mars_complete_data['featured_image_url'] = featured_image_url
    
    # Mars Weather
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    weather_html = browser.html
    weather_soup = BeautifulSoup(weather_html, 'html.parser')
    
    tweets = weather_soup.find_all('div', class_='js-tweet-text-container')
    weather = []
    for tweet in tweets:
        description = tweet.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text.replace('\n', ',', 2)
        weather.append(description)
        mars_complete_data['mars_weather'] = weather[0]

    # Mars Facts
    mars_facts_url = 'https://space-facts.com/mars/'
    mars_table = pd.read_html(mars_facts_url)
    # only need the data in table 1
    table = mars_table[0]
    table.columns = ['Description', 'Facts']
    temp_table = table.set_index(['Description'])
    table_data_html = temp_table.to_html()
    table_data_html = table_data_html.replace("\n","")
    mars_complete_data['mars_facts'] = table_data_html

    # Mars Hemispheres
    # URLs for Mars hemisphers from of Astrogeology site
    cerberus_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    schiaparelli_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    syrtis_major_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    valles_marineris_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

    # Cerberus Hemisphere
    browser.visit(cerberus_url)
    html = browser.html
    cerberus_soup = BeautifulSoup(html, 'html.parser')
    cerberus_image = cerberus_soup.find_all('div', class_='wide-image-wrapper')
    for image in cerberus_image:
        cerb_photo = image.find('li')
        full_res_photo = cerb_photo.find('a')['href']
    cerberus_title = cerberus_soup.find('h2', class_='title').text.replace('Enhanced', '')
    cerberus_hemisphere = {"title": cerberus_title, "img_url": full_res_photo}

    # Schiaparelli Hemisphere
    browser.visit(schiaparelli_url)
    html = browser.html
    schiaparelli_soup = BeautifulSoup(html, 'html.parser')
    schiaparelli_image = schiaparelli_soup.find_all('div', class_='wide-image-wrapper')
    for image in schiaparelli_image:
        sch_photo = image.find('li')
        full_res_photo = sch_photo.find('a')['href']
    schiaparelli_title = schiaparelli_soup.find('h2', class_='title').text.replace('Enhanced', '')
    schiaparelli_hemisphere = {"title": schiaparelli_title, "img_url": full_res_photo}

    # Syrtis Major Hemisphere
    browser.visit(syrtis_major_url)
    html = browser.html
    syrtis_major_soup = BeautifulSoup(html, 'html.parser')
    syrtis_major_image = syrtis_major_soup.find_all('div', class_='wide-image-wrapper')
    for image in syrtis_major_image:
        sm_photo = image.find('li')
        full_res_photo = sm_photo.find('a')['href']
    syrtis_major_title = syrtis_major_soup.find('h2', class_='title').text.replace('Enhanced', '')
    syrtis_major_hemisphere = {"title": syrtis_major_title, "img_url": full_res_photo}

    # Valles Marineris Hemisphere
    browser.visit(valles_marineris_url)
    html = browser.html
    valles_marineris_soup = BeautifulSoup(html, 'html.parser')
    valles_marineris_image = valles_marineris_soup.find_all('div', class_='wide-image-wrapper')
    for image in valles_marineris_image:
        vm_photo = image.find('li')
        full_res_photo = vm_photo.find('a')['href']
    valles_marineris_title = valles_marineris_soup.find('h2', class_='title').text.replace('Enhanced', '')
    valles_marineris_hemisphere = {"title": valles_marineris_title, "img_url": full_res_photo}
    
    #appending all 4 dictionaries into 1 list
    mars_hemispheres = [cerberus_hemisphere, schiaparelli_hemisphere, syrtis_major_hemisphere, valles_marineris_hemisphere]

    mars_complete_data['mars_hemispheres'] = mars_hemispheres
 
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_complete_data

