from nltk import sent_tokenize, regexp_tokenize

sentence = sent_tokenize(input())
i = int(input())
print(regexp_tokenize(sentence[i], "[A-z']+"))
