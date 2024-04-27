n = int(input())
a = list(map(int, input().split()))

stack = [a[0]]
for i in range(1, n):
    if a[i] == stack[-1]:
        stack.pop()
        stack.append(a[i] + 1)
        while True:
            if len(stack) == 1:
                break
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.append(stack.pop() + 1)
            else:
                break
    else:
        stack.append(a[i])
print(len(stack))