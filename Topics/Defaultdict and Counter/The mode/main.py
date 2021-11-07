from collections import Counter

common = Counter(input().split()).most_common(1)
print(common[0][0])
