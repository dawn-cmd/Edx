def main():
    n = int(input("Please enter a positive integer greater than 1: "))
    a = 0
    b = 1
    for i in range(n):
        print(b)
        a, b = b, a + b

if __name__ == "__main__":
    main()