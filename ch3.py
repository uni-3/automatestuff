# config utf-8

def collatz(n):
    if n%2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def main():
    # 数値が入力されるまで無限ループ
    print('整数を入力してください')
    while True:
        try:
            n = int(input())
            break
        except:
            print('整数を...')

    i = 0
    while True:
        i = i + 1
        n = collatz(n)
        print(i, "回目の値は:", int(n))

        if n == 1:
            return

if __name__ == '__main__':
    main()