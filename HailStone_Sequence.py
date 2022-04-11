def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return (3 * num) + 1


def hailstone():
    try:
        num = int(input())
        next = collatz(num)
        while True:
            print(next, end=" ")
            if next == 1:
                break
            else:
                next = collatz(next)
    except ValueError:
        print("Enter a valid argument..")
        hailstone()


def main():
    hailstone()

if __name__ == '__main__':
    main()
