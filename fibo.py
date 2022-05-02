def recursive_nth_fibo(n):
    if n <= 1:
        return n
    else:
        return (recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2))

def main():
    n = int(input())
    for i in range(n):
        print(recursive_nth_fibo(i))
    pass


if __name__ == "__main__":
    main()
