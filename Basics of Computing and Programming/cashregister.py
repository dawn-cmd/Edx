def main():
    price = []
    for i in range(2):
        times = "first" if not(i) else "second"
        price.append(float(input(f"Enter price of the {times} item: ")))
    price.sort()
    base_price = sum(price)
    price[0] /= 2
    discount_price = sum(price)
    if input("Does customer have a club card? (Y/N): ").lower() == 'y':
        discount_price *= 0.9
    tax_rate = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: ")) / 100
    print(f"Base price = {round(base_price, 2):.2f}")
    if discount_price != base_price:
        print(f"Price after discounts = {round(discount_price, 2):.2f}")
    print(f"Total price = {round(discount_price * (1 + tax_rate), 2):.2f}")

if __name__ == "__main__":
    main()