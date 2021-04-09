
installation required before executing the scripts. run below commands on command prompt
pip install selenium
pip install openpyxl
pip install Pillow


To execute the script from command line
1. Open the command prompt from PythonAssignment/test folder
2. enter the file name with extension and press enter key. Example-  "problem1.py"



folder structure:
Main directory - PythonAssignment
Test Scripts - test
All related images and screenshots - images
Test data excel - testData.xlsx
chrome driver - chromedriver.exe under PythonAssignment folder
firefox driver - geckodriver.exe under PythonAssignment folder

Note - there are few extra files under utilities folder, which are not in use for these 3 problems

Code details:

problem1 - to get screenshot for the user for defined article
            it is based on user input and will execute on headless browser
            provide correct article name to get the screenshot(just copy paste the article name from the list display)
            User can download as many article screenshot as present on the homepage
            to exit or terminate the execution, user has to provide 'quit' keyword

    things to remember -
        User has to provide exact article name to get the screenshot for the article
        User can get screenshot of an article only once, screenshot won't be replaced for the article if saved once

    There are 2 folders for article screenshot under images folder
        Articles - have screenshot of just article(cropped)
        fullScreenImage - have screenshot of full screen having article


problem2 - place order for first 3 popular items
            user can provide budget on start of execution on console
            on launch user account is created as per the data present in the testData.xlsx
            after successful account creation user is navigated to popular items screen and top 3 items are added to the cart
            after successful addition of products to the cart, user is navigated to checkout screen to verify the total
            if cart total is less or equal to budget present, then place order code is executed and screenshot is saved for order confirmation screen under success folder
            if cart total is greater than the budget mentioned by the user, then execution is stopped there and screenshot is saved under failure folder

    functions -
        take_screenshot - function to take screenshot for success anf failure
        excel_data - function to open excel
        modify_excel_data - function to modify the excel data
        tearDown - close all the browser instance for the execution

    Things to remember -
        User needs to provide column name and value to be added in the excel on command prompt once started the execution
        column name and value will be removed after the successful execution of the script
        if any of the top3 items are not added to the cart then next orderable product will be added to the cart
        for email, have added random number generation to have different email id everytime user execute the script

    There are 2 folders for article screenshot under images/problem2 folder
        Failure - have screenshot of Failed case when budget is less than the total price on checkout screen
        Success - have screenshot of order confirmation screen


problem 3 - download top 10 images of the latest trending topic on google trends
            trending topic is being searched from https://trends.google.com/ site
            after extracting the name of top trending topic of current time, name in searched on https://images.google.com/
            directory is created under images/trending topic folder with the current search time
            top 10 images are downloaded in the newly created folder

     Images are downloaded under images/trending topic folder
        Images are downloaded as per the date and time of the execution
        all images are renamed with the trending topic name as per the image number




Note - you might need to re-execute problem2.py as there are application issues
most of the time we are getting server hang up issues
have added extra sleep time as application response time is comparatively more