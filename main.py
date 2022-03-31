from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org/")
events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul').text


data = events.split("\n")
times = []
things = []
for i in data:
    listing = 0
    index = data.index(i)
    if index % 2 == 0:
        times.append(i)
    elif index % 2 != 0:
        things.append(i)
event = {}
for n in range(len(times)):
    event[n] = {
        "time": times[n],
        "event": things[n]
    }

print(event)