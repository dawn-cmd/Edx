def main():
    weight = float(input("Please enter weight in kilograms: "))
    height = float(input("Please enter height in meters: "))
    bmi = round(weight / (height ** 2), 2)
    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"
    print(f"BMI is: {bmi}, Status is {status}")

if __name__ == "__main__":
    main()


