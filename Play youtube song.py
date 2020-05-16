from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome('driver/chromedriver.exe')
options = webdriver.ChromeOptions();
options.add_argument('headless');

youtube = "https://www.youtube.com/"
browser.get(youtube)


while(1):
    song = input("Song you want to hear: ")

    searchBar = browser.find_element_by_id("search")
    searchBar.send_keys(song)
    search = browser.find_element_by_id("search-icon-legacy")
    search.submit()

    soup = BeautifulSoup(browser.page_source, features="html5lib")
    song = soup.findAll('a', {'class': 'yt-simple-endpoint inline-block style-scope ytd-thumbnail'})
    firstSong = song[0].get('href')

    songLink = "https://www.youtube.com/"+firstSong
    browser.get(songLink)

    print("1. Another song?\n2. Quit?")
    query = input("Answer(1/2): ")
    if query=='1' or  query.lower()=='song' or query.lower()=='another song' or query.lower()=='another':
        pass
    else:
        break

