def add_record():
    name = input("Enter student name: ")
    
    while True:
        grade = input("Enter student grade: ")
        if grade.isdigit():
            break
        else:
            print("Invalid grade. Please enter a number.")

    try:
        with open("students.txt", "a") as file:
            file.write(name + "," + grade + "\n")
        print("Record saved successfully.")
    except Exception as e:
        print("Error saving record:", e)


def view_records():
    try:
        with open("students.txt", "r") as file:
            print("\nSaved Records:")
            for line in file:
                name, grade = line.strip().split(",")
                print(f"Name: {name} | Grade: {grade}")
    except FileNotFoundError:
        print("No records found yet.")


def main():
    while True:
        print("\n=== Student Record Menu ===")
        print("1 - Add Student Record")
        print("2 - View Saved Records")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

main()
