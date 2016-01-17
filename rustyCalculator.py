
def answer(str):
    ans=''
    stack = []
    for char in str:
        if char == '+':
            while stack and stack[len(stack)-1] == '*':
                ans += stack.pop()
            stack.append(char)
        elif char == '*':
            stack.append(char)
        else:
            ans += char
    while stack:
        ans += stack.pop()
    return ans