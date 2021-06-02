import bs4
import requests

base_path = 'http://quotes.toscrape.com/page/{}/'

authors = set()
quotes = []
tags = set()

page = 1
while True:
    try:
        print(f'current page is {page}')
        response = requests.get(base_path.format(page))
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        quotes_box = soup.select('.quote')
        top_tags = soup.select('.tag-item')

        # break the loop if page not contains quotes
        if len(quotes_box) == 0:
            break

        for top_tag in top_tags:
            tags.add(top_tag.text)

        for quote_box in quotes_box:
            texts = quote_box.select('.text')
            for text in texts:
                quotes.append(text.text)
            author = quote_box.select('.author')[0].text
            authors.add(author)

        page = page + 1
        continue
    except:
        print('No data available for this page', page)
        break


print(quotes)
print(authors)
print(tags)