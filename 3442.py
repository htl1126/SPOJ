def main():
    n = int(raw_input())
    tbl = [[-1] for i in xrange(10)]
    for _ in xrange(n):
        a, b = raw_input().split(' ')
        a, b = int(a) % 10, int(b)
        if b == 0:
            print '1'
        else:
            if tbl[a][0] == -1:
                tbl[a][0] = a
                while tbl[a][-1] * a % 10 != tbl[a][0]:
                    tbl[a].append(tbl[a][-1] * a % 10)
            print tbl[a][b % len(tbl[a]) - 1]

if __name__ == '__main__':
    main()
