import time
from pathlib import Path, PurePosixPath
def takeScreenshot(driver):
    fileName = time.strftime("%Y%m%d-%H%M%S") + ".png"
    screenshotDir = PurePosixPath(Path.cwd()).joinpath("..\screenshots\\")
    # screens = screenshotDir.joinpath(fileName)

    try:
        driver.save_screenshot(fileName)
        print("Screenshot saved successfully")
    except:
        print("Screenshot not saved")

