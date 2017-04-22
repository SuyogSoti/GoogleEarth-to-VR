import os
from selenium import webdriver
from pyvirtualdisplay import Display



def main():
    display = Display(visible=0, size=(1080, 1920))
    display.start()
    driver = webdriver.Chrome()
    driver.get("https://earth.google.com/web/@40.00122818,-105.26285119,1644.76720416a,73.34143392d,35y,89.6767488h,66.20806007t,-0r/data=CksaSRJDCiUweDg3NDAxNDc0OWIxODU2Yjc6MHhjNzU0ODMzMTQ5OTBhN2ZmGY1QB5lipkNAIYAWaIEWYFrAKghDT0xPUkFETxgBIAE")
    # print driver.page_source.encode('utf-8')
    driver.save_screenshot("google.png")
    driver.quit()
    display.stop()


if __name__ == "__main__":
    main()
