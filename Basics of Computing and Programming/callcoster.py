def main():
    h = {"Mon": 1, "Tue": 2, "Wed": 3, "Thr": 4, "Fri": 5, "Sat": 6, "Sun": 7}
    day = h[input("Enter the day the call started at: ")]
    time = input("Enter the time the call started at (hhmm): ")
    length = int(input("Enter the duration of the call (in minutes): "))
    if day == 6 or day == 7:
        print(f"This call will cost ${0.15 * length:.2f}")
        return
    if time >= "0800" and time <= "1800":
        print(f"This call will cost ${0.4 * length:.2f}")
    else:
        print(f"This call will cost ${0.25 * length:.2f}")
    
if __name__ == "__main__":
    main()