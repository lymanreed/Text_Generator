from nltk import regexp_tokenize

tokens = regexp_tokenize(input(), '[A-Za-z]+')
print(tokens[int(input())])
