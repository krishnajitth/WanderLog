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
    category = input("Expense Category: ")
    while True:
        amount = input("Amount: ")
        try:
            int(amount)
            break
        except ValueError:
            print("Please enter a valid number!")
    with open("expenses.txt", "a") as file:
        file.write(f"{category}: {amount}\n")

    print("\nExpense saved successfully")

def view_summary():
    print("\n" + "=" * 35)
    print("          TRIP SUMMARY")
    print("=" * 35)

    print("\n TRIP DETAILS")
    print("-" * 35)
    with open("trips.txt", "r") as file:
        print(file.read())

    print("\n JOURNAL")
    print("-" * 35)
    with open("journal.txt", "r") as file:
        print(file.read())

    print("\n EXPENSES")
    print("-" * 35)

    total_spent = 0

    with open("expenses.txt", "r") as file:
        for line in file:
            print(line, end="")
            category, amount = line.strip().split(": ")
            total_spent += int(amount)

    with open("trips.txt", "r") as file:
        lines = file.readlines()

    budget = int(lines[3].split(":")[1])
    remaining = budget - total_spent

    print("-" * 35)
    print(f"TOTAL SPENT : ₹{total_spent}")
    print(f"REMAINING   : ₹{remaining}")
    print("=" * 35)

def search_journal():
    keyword=input("Enter keyword: ")

    print("\nMATCHING ENTRIES")
    print("-"*35)
    with open("journal.txt","r") as file:
        content=file.read()
    
    entries=content.split("Day ")
    found=False
    for entry in entries:
        if keyword.lower() in entry.lower():
            print("Day "+entry)
            print()
            found=True
    if not found:
        print("No matching entries found.")
    
def view_statistics():
    total_spent=0
    biggest_expense=0
    biggest_category=""

    with open("expenses.txt","r") as file:
        expense_lines=file.readlines()
    
    for line in expense_lines:
        category,amount=line.strip().split(": ")
        amount=int(amount)

        total_spent+=amount

        if amount>biggest_expense:
            biggest_expense=amount
            biggest_category=category
    
    with open("trips.txt","r")as file:
        trip_lines=file.readlines()
    
    budget=int(trip_lines[3].split(":")[1])
    remaining=budget-total_spent
    percentage_used=(total_spent/budget)*100

    with open("journal.txt","r") as file:
        journal_content=file.read()

    journal_entries=journal_content.count("Day ")

    print("\n"+"="*40)
    print("            STATISTICS")
    print("="*40)
    print(f"Budget           : ₹{budget}")
    print(f"Total Spent      : ₹{total_spent}")
    print(f"Remaining Budget : ₹{remaining}")
    print(f"Budget Used      : {percentage_used:.1f}%")
    print(f"Biggest Expense  : {biggest_category}(₹{biggest_expense})")
    print(f"Expense Entries  : {len(expense_lines)}")
    print(f"Journal Entries  : {journal_entries}")
    print("="*40)
            

            




while True:    
    print("========== WANDERLOG ==========")
    print("1. Create Trip")
    print("2. Add Journal Entry")
    print("3. Add Expense")
    print("4. View Trip Summary")
    print("5. Search Journal Entries")
    print("6. View Statistics")
    print("7. Exit")

    choice=input('Choose an option: ')

    if choice=="1":
       create_trip()
                    
                    
    elif choice=="2":
        add_journal()

    elif choice=="3":
        add_expense()

    elif choice=="4":
        view_summary()

    elif choice=="5":
        search_journal()

    elif choice=="6":
        view_statistics()

    elif choice=="7":
        print("\nThank you for using WanderLog!")
        break




        