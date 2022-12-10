from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json
options = webdriver.ChromeOptions()

options.add_argument("user-data-dir=C:/Users/RYAN/AppData/Local/Google/Chrome/User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
options.add_argument('profile-directory=Profile 5')
driver = webdriver.Chrome(options=options)
driver.get("https://cmrls.lib.ms.us/digital-library/virtual-reference-collection/ddc-website-links/dewey-decimal-subject-list/?fbclid=IwAR3U6x3FjAmhDKIxDeVLxwBlWPMqNX9YoId_ClAWflSBsf0l4gUZ67g-P-g")

time.sleep(5)
elements  = driver.find_elements(By.CLASS_NAME, "vc_column-inner")
array = []
NEEDS_FIXING = []
for element in elements:
    print(element)
    paragraphs = element.find_elements(By.TAG_NAME, "p")
    for p in paragraphs:
        text = p.text
        separated = text.split(" – ")
        subject = {}
        try:
            subject = {
                "name": separated[0],
                "number": float(separated[1])
            }
        except:
            NEEDS_FIXING.append(separated)

        array.append(subject)

print(NEEDS_FIXING)
with open('./dewey_subjects/subjects.json', 'w') as fout:
    json.dump(array, fout)