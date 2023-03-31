import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver and go to Google Maps
driver = webdriver.Chrome()
driver.get("https://www.google.com/maps/")

# Find the search field and enter "Barrie" using ID selector
search_field = driver.find_element("id","searchboxinput")
search_field.send_keys("Barrie")
search_field.send_keys(Keys.RETURN)
time.sleep(5)

# Find the Photos link and click on it using XPath selector
photos_link = driver.find_element("xpath","/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[16]/div[1]/button/div[2]")
photos_link.click()
time.sleep(5)

# Find the Street View & 360 link and click on it using XPath selector
street_view_link = driver.find_element("xpath","/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div/button[2]/div[2]/div[2]")
street_view_link.click()
time.sleep(5)

# Find the Videos link and click on it using XPath selector
videos_link = driver.find_element("xpath","/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div/button[3]/div[2]/div[2]")
videos_link.click()
time.sleep(5)

video1_link = driver.find_element("xpath","/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[1]/div[4]/div/a/div[4]")
video1_link.click()
time.sleep(5)

play_link = driver.find_element("xpath","/html/body/div[3]/div[9]/div[16]/div/div[3]/button[1]")
play_link.click()
time.sleep(12)
# Close the browser window
driver.quit()
