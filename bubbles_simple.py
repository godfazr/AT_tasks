from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time
from expects import expect, equal

ff = webdriver.Firefox()
ff.get("https://task1-bvckdxdkxw.now.sh/")
try:
    element = WebDriverWait(ff, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "bubble")))
except TimeoutError:
    print("No bubbles.")
else:
    time.sleep(5)
    elem = ff.find_elements_by_class_name("bubble")
    exp = len(elem)
    for el in elem:
        el.click()
    try:
        expect(exp).to(equal(int(ff.find_element_by_id("score").text)))
    except AssertionError:
        print("Counter error")
    else:
        print("bubbles found", count)
finally:
    ff.close()

