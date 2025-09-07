stack = []
for _ in range(int(input())):
    q = list(map(int, input().split()))
    # check the query type
    # push the element
    if q[0] == 1:
        if stack:
            stack.append(max(stack[-1], q[1]))
        else:
            stack.append(q[1])
    # delete the element
    elif q[0] == 2:
        stack.pop()
    # print the element
    else:
        print(stack[-1])

