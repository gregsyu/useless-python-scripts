from operator import itemgetter
from bs4 import BeautifulSoup
import nlp_rake
import requests

""" This script extracts love-themed quotes from a website, ranks them by keyword count using NLP-Rake,
    and prints the quotes, emphasizing the top quotes and their corresponding keyword counts. """


def main():
    url = "https://quotes.toscrape.com/tag/love/"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'html.parser')
    rake = nlp_rake.Rake(max_words=1, min_freq=2, min_chars=5)
    quotes_dict = dict()

    for quote, author in zip(soup.find_all("span", class_="text"), soup.find_all("small", class_="author")):
        res = rake.apply(quote.text)
        quotes_dict[author.text] = (len(res), quote.text)
    ranking = sorted(quotes_dict.items(), key=itemgetter(1), reverse=True)

    for v in ranking:
        print(v[1][1])  # prints quote
        splitted = v[0].split()
        print(f" ~ {splitted[1]}, {splitted[0]}\n")  # Inverts name
    print("-" * 32)
    print([v[1][0] for v in ranking])


if __name__ == "__main__":
    main()
