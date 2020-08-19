from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
username = driver.find_element_by_name('session_key')
# username = driver.find_element_by_class_name('input__message hidden')  # locate email form by_class_name
username.send_keys('email')  # send_keys() to simulate key strokes

password = driver.find_element_by_name('session_password')  # locate password form by_class_name
password.send_keys('password')  # send_keys() to simulate key strokes
time.sleep(0.5)
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()  # .click() to mimic button click
time.sleep(0.5)
driver.get("https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%224461%22%2C%2236006%22%5D")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
names = []
link = []
current_page = 1
number_of_pages = int(driver.find_element_by_class_name("artdeco-pagination__indicator artdeco-pagination__indicator--number "))
print(number_of_pages)

for a in soup.find_all('li', {'class': 'org-people-profiles-module__profile-item'}):
    p_name = a.find_all('div', attrs={'class': 'org-people-profile-card__profile-title t-black lt-line-clamp lt-line-clamp--single-line ember-view'})
    # names.append(p_name.text)
    p_link = a.find_all('a', attrs={'class': 'link-without-visited-state ember-view'})

    # link.append(p_link.get('href'))

print(p_name)
print(p_link)
