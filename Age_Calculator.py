from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()

    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

def main():
    print("=" * 35)
    print("   AGE CALCULATOR")
    print("="  * 35)

    try:
        dob = input("Enter your Date of Birth (DD-MM-YYYY): ")

        birth_date = datetime.strptime(dob, "%d-%m-%Y")
        age = calculate_age(birth_date)

        print(f"\nYou are {age} years old.")

    except ValueError:
        print("Invlalid date! Please use DD-MM-YYYY format.")

if __name__ == "__main__":
    main()