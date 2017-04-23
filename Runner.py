import webbrowser
import pyscreenshot as ImageGrab
import time
import math
from selenium import webdriver


# def open_coordinates(long, latd, lat):
#     return "https://earth.google.com/web/@40.00122199,-105.26285016,1650.67707633a,54.79800433d,35y,88.6646013h,68.36048567t,-0r/data=CksaSRJDCiUweDg3NDAxNDc0OWIxODU2Yjc6MHhjNzU0ODMzMTQ5OTBhN2ZmGY1QB5lipkNAIYAWaIEWYFrAKghDT0xPUkFETxgBIAE"


x_init = 100
x_final = 1500
y_init = 200
y_final = 1000
# https://earth.google.com/web/@40.00976984,-105.26680447,1624.6141859a,732.04732435d,9.66183613y,-1.70467733h,71.44598343t,0r


def take_pictures(lat, long, radius, number):
    # webbrowser.open_new("http://www.google.com")
    # radius = radius/111
    # t = 70
    t = 55
    if number == 30:
        t = 70
    for i in range(number):
        num = i *9
        # webbrowser.open("https://earth.google.com/web/@"+str(lat + (radius/111)*math.cos(math.radians(num)))+","
        #                                                 +str(long + (radius/111)*math.sin(math.radians(num)))+","
        #                                                 +str(1700 + radius*math.sin(math.radians(t)))+"a,0d,35y,"
        #                                                 +str(num-180)+"h,"
        #                                                 +str(t)+"t,0r")
        webbrowser.open(
            "https://earth.google.com/web/@" + str(lat + 0.0006181318* math.cos(math.radians(num))) + ","
            + str(long + 0.0006181318* math.sin(math.radians(num))) + ","
            + str(1700 + 0.0006181318 * math.sin(math.radians(t))) + "a,0d,35y,"
            + str(num-180) + "h,"
            + str(t) + "t,0r")
        time.sleep(10)
        im = ImageGrab.grab(bbox=(x_init, y_init, x_final, y_final))
        im.save("images/screenshot"+str(i)+".png")

if __name__ == "__main__":
    take_pictures(40.00743167,-105.26844697, 60, 40)
    driver = webdriver.Chrome()
    driver.get("https://recap360.autodesk.com/")
    driver.find_element_by_id("userName").send_keys("jsky.johnson@gmail.com")
    driver.find_element_by_id("password").send_keys("InsecurePassword3\n")
    time.sleep(120)
    # driver.find_element_by_class_name("modal-backdrop").click()
    # driver.find_element_by_class_name("btn-new").click()
    # driver.find_element_by_class_name("360-browser-link").click()
