import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')
page_py = wiki_wiki.page('Category:People_from_Delhi')

print(page_py.summary)