import json

from prepare_data import *

if __name__ == '__main__':
    create_quotes()
    create_authors()
    with open('quotes.json', 'w', encoding='utf-8') as q_file:
        json.dump(create_quotes(), q_file, ensure_ascii=False)
    with open('authors.json', 'w', encoding='utf-8') as au_file:
        json.dump(create_authors(), au_file, ensure_ascii=False)
