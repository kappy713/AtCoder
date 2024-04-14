from collections import Counter

s=input()

counter = Counter(s)

counter_of_counts = Counter(counter.values())

for count in counter_of_counts.values():
    if count not in [0,2]:
        print("No")
        break
else:
    print("Yes")