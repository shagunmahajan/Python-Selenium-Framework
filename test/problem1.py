import os
import re
from pathlib import Path, PurePosixPath
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# image directory
screenshot_dir = PurePosixPath(Path.cwd()).joinpath("../images/articles/")
user_input = None
listOfArticlesName = []


# get driver
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')

    # chrome driver options
    chrome_location = PurePosixPath(Path.cwd()).joinpath("../chromedriver.exe")
    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_location)

    # firefox driver options
    # firefox_location = PurePosixPath(Path.cwd()).joinpath("../geckodriver.exe")
    # driver = webdriver.Firefox(options=chrome_options, executable_path=firefox_location)

    return driver


# close all browser instances related to execution
def tearDown():
    driver.quit()


# if __name__ == "__main__":
url = "http://lifecharger.org/"
driver = get_driver()
driver.get(url)

# get list of articles from homepage
listOfArticles = driver.find_elements_by_tag_name('article')

# store list of articles
for article in listOfArticles:
    listOfArticlesName.append(article.find_element_by_tag_name('a').text)

# search for article as per user input
while user_input != 'quit':
    print("\nList of articles present on homepage: \n")

    # display list of articles present on the homepage for user
    for (i, item) in enumerate(listOfArticlesName, start=1):
        print(str(i)+".", item)

    # take user input without spaces in the beginning and at the end
    user_input = (input("\nEnter article name for screenshot or Enter 'quit': ")).strip()
    print("Please wait, while we process your request..!!")

    # execute until input is quit
    if user_input != 'quit':
        ''''verification for user input is in the article list. '' to verify if user press enter key without
        providing any input'''
        if user_input in listOfArticlesName and user_input != '':
            searchArticle = driver.find_element_by_partial_link_text(user_input)
            searchArticle.click()

            # find the article height to resize the window
            article = driver.find_element_by_tag_name('article')
            article_height = article.size["height"]

            # resize window size according to the article height
            driver.set_window_size(1920, article_height)

            # get article size, width, height , x , y axis for cropped image
            article_x_axis = article.location['x']
            article_y_axis = article.location['y']
            article_width = article_x_axis + article.size['width']
            height = article_y_axis + article.size['height']
            article_size = (int(article_x_axis), int(article_y_axis), int(article_width), int(height))
            # # remove special characters from file name except the spaces
            fileName = re.sub(r"[^a-zA/-Z0-9]+", ' ', user_input) + ".png"
            article_screenshot_dir = os.path.join(screenshot_dir, 'fullScreenImage', fileName)

            # code to take screenshot
            try:
                # take screenshot of the article in full screen
                driver.save_screenshot(article_screenshot_dir)
                print("Screenshot saved successfully for article: " + fileName)
                # open the saved screenshot
                im = Image.open(article_screenshot_dir)
                # crop the image as per the article location and size
                im = im.crop(article_size)
                cropped_fileName = re.sub(r"[^a-zA-Z0-9]+", ' ', user_input) + ".png"
                cropped_dir = os.path.join(screenshot_dir, cropped_fileName)

                # save cropped image
                im.save(cropped_dir)
                print("Cropped image saved successfully for article: " + fileName)
                # navigate back to home page
                driver.find_element_by_link_text('Home').click()
            except Exception as e:
                print("Screenshot not saved for article: " + fileName)
        else:
            print("Oh No..!! We couldn't find any article with the searched name. Please choose one from the list.")

# close browser
tearDown()
