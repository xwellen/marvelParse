from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import csv

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url="https://www.marvel.com/characters")
with open("./page.html", "w") as file:
    file.write(driver.page_source)
with open("./page.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
cards_divs = soup.find_all("div", class_="mvl-card mvl-card--explore")

with open("./heroes.csv", "w") as file:
    fieldnames = ["hero_name", "hero_link"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for card in cards_divs:
        hero_name = card.find("p", class_="card-body__headline").text
        hero_link = card.find("a", class_="explore__link")['href']
        writer.writerow({
            "hero_name": str(hero_name),
            "hero_link": str(hero_link)
        })
