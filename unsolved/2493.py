n = int(input())

heights = map(int, input())
stack = list()

for i in range(len(heights)):
    tar = heights[i]
    if len(stack) == 0:
        stack.append(tar)
        ans = 0
    while stack[-1] <= tar:
        stack.pop()
    stack.append(tar)
    