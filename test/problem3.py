import os
import time
import urllib.request

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from pathlib import Path, PurePosixPath


# directory path for saving trending topic images
download_Img_Dir = PurePosixPath(Path.cwd()).joinpath("../images/trending topic/").joinpath(
    "Trending Topic on " + time.strftime("%d %b, %Y_%H_%M_%S"))


# get driver details
def get_driver():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    # chrome driver options
    chrome_location = PurePosixPath(Path.cwd()).joinpath("../chromedriver.exe")
    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_location)

    # firefox driver options
    # firefox_location = PurePosixPath(Path.cwd()).joinpath("../geckodriver.exe")
    # driver = webdriver.Firefox(options=chrome_options, executable_path=firefox_location)

    return driver


# function to scroll and find images for searched topic
def scroll_and_find_images():
    value = 0
    # range can be adjusted as per the number of images need to be downloaded
    for i in range(1):
        driver.execute_script("scrollBy(" + str(value) + ",+1000);")
        value += 1000
        time.sleep(1)
        # main div element having all the images as per search result
        main_element = driver.find_element_by_id('islmp')
        # element to find images using img tag
        image_elements = main_element.find_elements_by_tag_name('img')
        return image_elements


# create new directory as mentioned in the directory path
def create_directory():
    try:
        os.mkdir(download_Img_Dir)
        print("Created Directory successfully")
    except FileExistsError:
        print("Directory already Exists")
        pass


# function to search for image src attribute and download the images
def download_image(image_elements, trending_topic):
    count = 1
    for image in image_elements:
        # get src attribute for each image
        image_src = image.get_attribute('src')
        try:
            # number of images need to be downloaded
            if count > 10:
                print("Downloaded Images successfully")
                break
            else:
                if image_src is not None:
                    print('Downloading Image ' + str(count))

                    # download the image using the src attribute value
                    urllib.request.urlretrieve(image_src, os.path.join(download_Img_Dir, trending_topic + "_" + str(count) + '.jpg'))
                    count += 1
                else:
                    print("Image src attribute is not available")
                    raise TypeError
        except TypeError:
            print('Not able to download image ' + count)


# close browser instances related to execution
def tearDown():
    driver.quit()


# main function
if __name__ == "__main__":
    url = "https://trends.google.com/"
    driver = get_driver()

    driver.get(url)
    # get trending topic from google trends
    trendingTopic = driver.find_element_by_class_name('list-item-title').text
    print("Trending Topic: " + trendingTopic)

    # navigate to google image search site
    driver.get("https://images.google.com/")

    # provide trending topic in search field and hit search button
    driver.find_element_by_xpath("//*[@title='Search']").send_keys(trendingTopic)
    driver.find_element_by_xpath("//button[@aria-label='Google Search']").click()
    print("Searching for " + trendingTopic + " images")

    scroll_and_find_images()
    create_directory()
    download_image(scroll_and_find_images(), trendingTopic)
    tearDown()
