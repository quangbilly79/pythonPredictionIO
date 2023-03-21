from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

# set the path to the chromedriver executable
chrome_driver_path = "path/to/chromedriver.exe"

# create a new Chrome browser instance
browser = webdriver.Chrome(ChromeDriverManager().install())

# navigate to the website containing the button
browser.get("https://ebook.waka.vn/cam-nang-quan-ly-hieu-qua-tu-duy-tich-cuc-susan-quilliam-bGyq8W.html")
browser.implicitly_wait(30)
css_path = """
#best-seller-w > div > div > div > div:nth-child(1) > div.card-body.card-body-book > div.book-title > a
"""


#WebDriverWait(browser, 20).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, css_path1)))

# find the button element by its CSS selector
button = browser.find_element(By.CSS_SELECTOR, css_path)

# browser.execute_script("arguments[0].click();", button)
# print("browser.execute_script(arguments[0].click();, button): ", browser)
# browser.execute_script("openReaderPage(42263,1,0,1,1);")
# print("browser.execute_script(openReaderPage(42263,1,0,1,1);): ", browser)
#browser.execute_script("arguments[0].scrollIntoView(true);", button)
# simulate a click on the button
button.click()

# wait for the page to load
browser.implicitly_wait(10)

# get the current URL after clicking the button
after_url = browser.current_url

# print the current URL
print("Current URL:", after_url)

#https://ebook.waka.vn/mot-cuon-sach-ve-chu-nghia-toi-gian-by1nLW.html
#https://ebook.waka.vn/mot-cuon-sach-ve-chu-nghia-toi-gian-chi-nguyen-ry1nLW.html?type=1
#https://ebook.waka.vn/cam-nang-quan-ly-hieu-qua-tu-duy-tich-cuc-susan-quilliam-bGyq8W.html
#https://ebook.waka.vn/cam-nang-quan-ly-hieu-qua-tu-duy-tich-cuc-susan-quilliam-rGyq8W.html?type=1

# close the browser
browser.quit()