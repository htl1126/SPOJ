def convert(s):
    stack = []
    for c in s:
        if c.isalpha():
            stack.append([c])
        elif c in '+-*/^':
            stack[-1].append(c)
        elif c == ')':
            t = stack.pop()
            stack[-1] = stack[-1][:-1] + t + [stack[-1][-1]]
    return ''.join(stack[0])


def main():
    n = int(raw_input())
    for _ in xrange(n):
        s = raw_input()
        print convert(s)

if __name__ == '__main__':
    main()
