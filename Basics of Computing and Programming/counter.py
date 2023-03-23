def main():
    print("Please enter the number of coins:")
    quarters = int(input("# of quarters: "))
    dimes = int(input("# of dimes: "))
    nickels = int(input("# of nickels: "))
    pennies = int(input("# of pennies: "))
    total = 25 * quarters + 10 * dimes + 5 * nickels + pennies
    print(f"The total is {total // 100} dollars and {total % 100} cents")

if __name__ == "__main__":
    main()