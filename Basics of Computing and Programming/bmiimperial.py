def main():
    weight = float(input("Please enter weight in pounds: "))
    height = float(input("Please enter height in inches: "))
    print(f"BMI is: {(weight * 0.453592) / (height * 0.0254) ** 2}")

if __name__ == "__main__":
    main()