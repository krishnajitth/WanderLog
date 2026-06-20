def create_trip():
    destination=input("Destination: ")
    start_date=input("Start Date: ")
    days=input("Number of Days: ")
    budget=input("Budget: ")

    with open("trips.txt","w")as file:
        file.write(f"Destination: {destination}\n")
        file.write(f"Start Date: {start_date}\n")
        file.write(f"Days: {days}\n")
        file.write(f"Budget: {budget}\n")
    
    print("\nTrip created successfully!")

def add_journal():
    day=input("Day Number: ")
    entry=input("Write your experience: ")

    with open("journal.txt","a")as file:
        file.write("Day "+day+ "\n")
        file.write(entry+ "\n\n")
    
    print("\nJournal entry saved!")

def add_expense():
    category=input("Expense Category: ")
    amount=input("Amount: ")

    with open("expenses.txt","a")as file:
        file.write(f"{category}: {amount}\n")

    print("\nExpense saved successfully")

def view_summary():
    print("\n" + "=" * 35)
    print("          TRIP SUMMARY")
    print("=" * 35)

    print("\n TRIP DETAILS")
    print("-" * 35)
    with open("trips.txt","r")as file:
        print(file.read())

    print("\n JOURNAL")
    print("-" * 35)
    with open("journal.txt","r")as file:
        print(file.read())

    print("\n EXPENSES")
    print("-" * 35)
    with open("expenses.txt","r")as file:
        print(file.read())


while True:    
    print("========== WANDERLOG ==========")
    print("1. Create Trip")
    print("2. Add Journal Entry")
    print("3. Add Expense")
    print("4. View Trip Summary")
    print("5. Exit")

    choice=input('Choose an option: ')

    if choice=="1":
       create_trip()
                    
                    
    elif choice=="2":
        add_journal()

    elif choice=="3":
        add_expense()

    elif choice=="4":
        view_summary()




        