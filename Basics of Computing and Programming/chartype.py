def main():
    c = input("Enter a character: ")
    if 'a' <= c <= 'z':
        print(f"{c} is a lower case letter.")
    elif 'A' <= c <= 'Z':
        print(f"{c} is an upper case letter.")
    elif '0' <= c <= '9':
        print(f"{c} is a digit.")
    else:
        print(f"{c} is a non-alphanumeric character.")
    
if __name__ == "__main__":
    main()