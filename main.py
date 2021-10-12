from selenium import webdriver
import time

with open('url.txt') as file:
    URL = file.readline()
    cookies_button_id = file.readline()
    notification_button_id = file.readline()
    elem_css = file.readline()


if __name__ == '__main__':
    while True:
        try:
            firefox_profile = webdriver.FirefoxProfile()
            firefox_profile.set_preference(URL, True)
            driver = webdriver.Firefox(firefox_profile=firefox_profile)
            driver.get(URL)

            time.sleep(3)

            cookies_button = driver.find_element_by_id(cookies_button_id)
            cookies_button.click()

            notification_button = driver.find_element_by_id(notification_button_id)
            notification_button.click()

            frame = driver.find_element_by_css_selector(elem_css)
            driver.switch_to.frame(frame)

            elems = driver.find_elements_by_css_selector(elem_css)
            elems[1].click()

            time.sleep(3)
            driver.close()
            print('\nClosed')

        except KeyboardInterrupt:
            print('\nInterrupted')
