from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

# set the path to the chromedriver executable
chrome_driver_path = "path/to/chromedriver.exe"

# create a new Chrome browser instance
browser = webdriver.Chrome(ChromeDriverManager().install())

# navigate to the website containing the button
browser.get("https://ebook.waka.vn/cam-nang-quan-ly-hieu-qua-tu-duy-tich-cuc-susan-quilliam-bGyq8W.html")

time.sleep(10)

css_path2 = 'a[href="javascript:void(0)"]'


#------------------Method1
# WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_path1))).click()

#------------------Method2
button = browser.find_element(By.CSS_SELECTOR, css_path2)
button.click()
# button = browser.find_element(By.XPATH, xpath2)
# button.click()


#------------------Method3
# button = browser.find_element(By.CSS_SELECTOR, css_path2)
# action = ActionChains(browser)
# action.click(button)
# action.perform()

#-------------------Method4
# javaScript = "document.querySelector('a[href=\"javascript:void(0)\"]').click();"
# browser.execute_script(javaScript)


# wait for the page to load
time.sleep(10)

# get the current URL after clicking the button
after_url = browser.current_url
# print the current URL
print(after_url)

css_path3 = "#nav-bar > div:nth-child(1) > a"
button = browser.find_element(By.CSS_SELECTOR, css_path3)
button.click()
time.sleep(10)
after_url = browser.current_url
print(after_url)


# close the browser
browser.quit()



#https://ebook.waka.vn/mot-cuon-sach-ve-chu-nghia-toi-gian-by1nLW.html
#https://ebook.waka.vn/mot-cuon-sach-ve-chu-nghia-toi-gian-chi-nguyen-ry1nLW.html?type=1
#https://ebook.waka.vn/cam-nang-quan-ly-hieu-qua-tu-duy-tich-cuc-susan-quilliam-bGyq8W.html
#https://ebook.waka.vn/cam-nang-quan-ly-hieu-qua-tu-duy-tich-cuc-susan-quilliam-rGyq8W.html?type=1