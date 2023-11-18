from wordcloud import WordCloud
from os.path import exists
import wikipedia
import nlp_rake
import argparse

""" This Python script generates a word cloud from a Wikipedia article, allowing customization through command-line arguments.
    It extracts keywords using NLP-Rake, displays top keywords, and saves the resulting word cloud image """


def main():
    # Parsing arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--page", type=str, required=True)
    parser.add_argument("-r", "--resolution", type=str, default="800x600")
    parser.add_argument("-c", "--color", type=str, default="white")
    parser.add_argument("-n", type=int, default=None)
    args = parser.parse_args()

    # Fetch the Wikipedia article content:
    args.page = args.page.replace(' ', '_')
    article_content = wikipedia.page(f"wiki/{args.page.capitalize()}").content

    # Use `nlp_rake` to extract keywords
    rake = nlp_rake.Rake(max_words=2, min_freq=3, min_chars=5)
    res = rake.apply(article_content)

    # Display top keywords:
    if args.n is not None:
        res = res[:args.n]
    for keyword, freq in res:
        print(f"Keyword: \x1b[32m{keyword.capitalize()!r}\x1b[0m")
        print(f"Frequency: \x1b[34m{freq:.2f}\x1b[0m\n")

    # Generate and save the word cloud:
    (width, height) = map(int, args.resolution.split("x"))
    file_path = args.page.lower() + "_wordcloud.png"
    wc = WordCloud(background_color=args.color, width=width, height=height)
    if not exists(file_path):
        print(f"\x1b[32mFile {file_path!r} was created..\x1b[0m")
    wc.generate_from_frequencies({k: v for k, v in res}).to_file(file_path)


if __name__ == "__main__":
    main()
