def main():
    s = input("Enter an odd length string: ")
    print(f"Middle character: {s[(len(s) - 1) // 2]}")
    print(f"First half: {s[:(len(s) - 1) // 2]}")
    print(f"Second half: {s[(len(s) - 1) // 2 + 1:]}")

if __name__ == "__main__":
    main()