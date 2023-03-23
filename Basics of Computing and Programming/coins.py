def main():
    print("Please enter the amount of money to convert:")
    dollars = int(input("# of dollars: "))
    cents = int(input("# of cents: "))
    total = dollars * 100 + cents
    print(f"The coins are {total // 25} quarters, {total % 25 // 10} dimes, {total % 25 % 10 // 5} nickels and {total % 25 % 10 % 5} pennies")

if __name__ == "__main__":
    main()