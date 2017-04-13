# -*- coding:utf-8 -*-
import nltk
from nltk.tokenize import WordPunctTokenizer
# import requests
# url = 'http://127.0.0.1'
# r = requests.get(url)
# print r.text
# nltk.download()
words = []
sent = 'hh  hhahshah sajsjajs sashahsh saksjkasj'
words = WordPunctTokenizer().tokenize(sent)
print words
