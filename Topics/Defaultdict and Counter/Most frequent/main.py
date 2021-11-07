from collections import Counter

text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")

freq_dict = Counter(text.split())

n = int(input())
for e in freq_dict.most_common(n):
    print(e[0], e[1])
