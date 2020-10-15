#8. Qual é a letra com maior recorrência nos títulos dos livros?

import requests

def most_freq_char():
    r = requests.get("http://0.0.0.0:8000/books")
    l = r.json()

    #create list with titles

    titles = []
    for i in l:
        x = i['title']
        titles.append(x)
    
    #titles == list of all book titles
    #split book titles in a list of chars

    chars = []
    for i in titles:
        j = [char for char in i]
        chars.append(j)

    #char == list of lists with titles chars
    #merged == all chars from all titles

    merged = [item for let in chars for item in let]

    freq = max(set(merged), key = merged.count)

    print(f"The most recurrent letter in all titles is:\n {freq}")



most_freq_char()
