import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')
page_py = wiki_wiki.page('Delhi')

print(page_py.summary)