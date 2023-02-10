from collections import Counter


data = input().split(',')

for i in sorted(set(data)):
    print('{}: {}'.format(i, Counter(data)[i]))
