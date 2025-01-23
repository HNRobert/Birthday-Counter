from datetime import datetime, timedelta


# Function to calculate the day number since birth
def days_since_birth(birthday):
    today = datetime.today()
    birth_date = datetime.strptime(birthday, "%Y-%m-%d")
    delta = today - birth_date
    return delta.days


# Function to calculate the date after a certain number of days
def date_after_days(birthday, days):
    birth_date = datetime.strptime(birthday, "%Y-%m-%d")
    target_date = birth_date + timedelta(days=days)
    return target_date.strftime("%Y-%m-%d")


# Main Program
def main():
    print("Please enter your birth date in the format: yyyy-mm-dd (e.g., 1990-01-01)")
    birthday = input("Enter your birth date: ")

    while True:
        print("\nChoose an option:")
        print("1. Calculate how many days have passed since your birth.")
        print("2. Calculate the date after a certain number of days since your birth.")
        print("3. Exit program")
        choice = input("Enter 1, 2 or 3: ")

        if choice == "1":
            days = days_since_birth(birthday)
            print(f"You were born {days} days ago.")
        elif choice == "2":
            days_input = int(input("Enter the number of days to add: "))
            result_date = date_after_days(birthday, days_input)
            print(f"The date after {days_input} days is {result_date}.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
