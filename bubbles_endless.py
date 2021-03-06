from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from expects import expect, equal

count = 0
ff = webdriver.Firefox()
ff.get("https://task1-bvckdxdkxw.now.sh/")
while True:
    try:
        elem = WebDriverWait(ff, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "bubble")))
    except TimeoutError:
        continue
    except KeyboardInterrupt:
        ff.quit()
        break
    else:
        elem.click()
        count += 1
        try:
            expect(count).to(equal(int(ff.find_element_by_id("score").text)))
        except AssertionError:
            print("Counter error")
        else:
            print("Ok")