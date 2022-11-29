"""
CP1404 | Liam Eime | Practical 10 | wiki
"""

import wikipedia


def main():
    """Program to get wikipedia summary of user entered phrase"""
    search_phrase = input("Enter title/search phrase: ")
    while search_phrase != "":
        try:
            wiki_abstraction = wikipedia.page(search_phrase, auto_suggest=False)
            print(f"Title: {wiki_abstraction.title}")
            print(f"Summary: {wiki_abstraction.summary}")
            print(f"URL: {wiki_abstraction.url}")
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        search_phrase = input("Enter title/search phrase: ")


main()
