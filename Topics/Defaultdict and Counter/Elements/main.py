from collections import Counter

counter = Counter(input().lower().split())
print(sorted(counter.elements()))
