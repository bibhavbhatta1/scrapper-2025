import requests
from bs4 import BeautifulSoup
import json

URL = "https://books.toscrape.com/"

# git config --global user.name "Ramesh Pradhan"
# git config --global user.email "pyrameshpradhan@gmail.com"

# git init
# git status => if you want to check what are the status of files
# git diff => if you want to check what are the changes
# git add .
# git commit -m "Your message"
# copy paste git code from github


def scrape_books():
    response = requests.get(URL)
    if response.status_code != 200:
        return
    #Set encoding explicitly to handle special character 
    response.encoding = response.apparent_encoding 

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
   
    all_books = []
    for book in books:
        title = book.h3.a['title']
        price_text = book.find("p", class_="price_color").text
        currency = price_text[0]
        price = price_text[1:]
        all_books.append(
            {
                "Title": title,
                "Price": price,
                "Currency": currency,
            }
        )
    return all_books

books = scrape_books()
with open("books.json","w", encoding="utf-8") as f:
    json.dump(books, f, indent = 2, ensure_ascii=False)


