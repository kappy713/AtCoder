n = int(input())
cards = []
for i in range(n):
    a,c = map(int, input().split())
    cards.append({'a': a, 'c': c, 'index': i})
    
cards.sort(key=lambda x: x['c'])

ans = []
v = 0
for i in range(n):
    if cards[i]['a'] > v:
        v = cards[i]['a']
        ans.append(cards[i]['index'])
    
ans.sort()

m = len(ans)
print(m)
for i in range(m):
    print(ans[i] + 1, end=' ')