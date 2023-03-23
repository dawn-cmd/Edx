def main():
    weight = float(input("Please enter weight in kilograms: "))
    height = float(input("Please enter height in meters: "))
    print(f"BMI is: {weight / (height ** 2)}")

if __name__ == "__main__":
    main()