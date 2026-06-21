import os
for filename in["trips.txt","journal.txt","expenses.txt","report.txt"]:
    with open(filename,"a"):
        pass

def pause():
    input("\nPress Enter to continue...")

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

    with open("journal.txt","w"):
        pass
    with open("expenses.txt","w"):
        pass
    with open("report.txt","w"):
        pass
    
    print("\nTrip created successfully!")
    pause()

def add_journal():
    day=input("Day Number: ")
    entry=input("Write your experience: ")

    with open("journal.txt","a")as file:
        file.write("Day "+day+ "\n")
        file.write(entry+ "\n\n")
    
    print("\nJournal entry saved!")
    pause()

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
    pause()

def view_summary():
    print_header("TRIP SUMMARY")

    print_section("TRIP DETAILS")

    with open("trips.txt", "r") as file:
        lines=file.readlines()

    if len(lines)<4:
        print("\nNo trip created yet!")
        pause()
        return
    
    for line in lines:
        key,value=line.strip().split(": ")
        print(f"{key:<12} : {value}")

    print_section("JOURNAL")

    with open("journal.txt", "r") as file:
        journal=file.read()
    
    if journal.strip()=="":
        print("No journal entries yet.")
    else:
        print(journal)

    print_section("EXPENSES")

    total_spent = 0

    with open("expenses.txt", "r") as file:
        expense_lines=file.readlines()

    if len(expense_lines)==0:
        print("No expenses recorded.")

    else:
        for line in expense_lines:
            category,amount=line.strip().split(": ")
            print(f"{category:<15} : ₹{amount}")
            total_spent+=int(amount)

    budget = int(lines[3].split(":")[1])
    remaining = budget - total_spent

    print("=" * 35)
    print(f"TOTAL SPENT : ₹{total_spent}")
    print(f"REMAINING   : ₹{remaining}")
    
    print("="*35)
    pause()

def search_journal():
    keyword=input("Enter keyword: ")

    print("\nMATCHING ENTRIES")
    print("-"*35)
    with open("journal.txt","r") as file:
        content=file.read()
    
    if content.strip()=="":
        print("\nNo journal entries found!")
        pause()
        return
    
    entries=content.split("Day ")
    found=False
    for entry in entries:
        if keyword.lower() in entry.lower():
            print("-"*40)
            print("Day "+entry)
            print()
            found=True
    if not found:
        print("No matching entries found.")

    pause()
    
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

    if len(trip_lines)<4:
        print("\nNo trip created yet!")
        pause()
        return
    
    budget=int(trip_lines[3].split(":")[1])
    remaining=budget-total_spent
    
    if budget==0:
        percentage_used=0
    else:
        percentage_used=(total_spent/budget)*100

    with open("journal.txt","r") as file:
        journal_content=file.read()

    journal_entries=journal_content.count("Day ")

    print_header("STATISTICS")

    print(f"Budget           : ₹{budget}")
    print(f"Total Spent      : ₹{total_spent}")
    print(f"Remaining Budget : ₹{remaining}")

    print("-" * 40)
    print(f"Budget Used      : {percentage_used:.1f}%")

    filled=int(percentage_used//5)
    bar="█"*filled+"-"*(20-filled)
    print(f"[{bar}]")
    print("-" * 40)

    if biggest_expense==0:
        print("Biggest Expense  : None")
    else:
        print(f"Biggest Expense  : {biggest_category} (₹{biggest_expense})")

    print(f"Expense Entries  : {len(expense_lines)}")
    print(f"Journal Entries  : {journal_entries}")
    print("="*40)

    pause()
            
def export_report():
    total_spent=0
    biggest_expense=0
    biggest_category=""

    with open("expenses.txt","r")as file:
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

    if len(trip_lines)<4:
        print("\nNo trip created yet!")  
        pause()
        return   
    
    budget=int(trip_lines[3].split(":")[1])
    remaining=budget-total_spent
    
    if budget==0:
        percentage_used=0
    else:
        percentage_used=(total_spent/budget)*100

    with open("journal.txt","r")as file:
        journal_content=file.read()

    with open("report.txt","w",encoding="utf-8")as report:
        report.write("="*40+"\n")
        report.write("         WANDERLOG REPORT\n")
        report.write("="*40+"\n\n")

        report.write("TRIP DETAILS\n")
        report.write("-"*40+"\n")
        report.writelines(trip_lines)
        report.write("\n")

        report.write("JOURNAL\n")
        report.write("-"*40+"\n")

        if journal_content.strip()=="":
            report.write("No journal entries yet.\n")
        else:
            report.write(journal_content)
        
        report.write("\n")

        report.write("EXPENSES\n")
        report.write("-"*40+"\n")
        
        if len(expense_lines)==0:
            report.write("No expenses recorded.\n")
        else:
            report.writelines(expense_lines)

        report.write("\n")

        report.write("STATISTICS\n")
        report.write("-"*40+"\n")
        report.write(f"Total Spent      : ₹{total_spent}\n")
        report.write(f"Remaining Budget : ₹{remaining}\n")

        report.write(f"Budget Used      : {percentage_used:.1f}%\n")
        filled=int(percentage_used//5)
        bar="█"*filled+"-"*(20-filled)
        report.write(f"[{bar}]\n")
        report.write("-"*40+"\n")

        if biggest_expense==0:
            report.write("Biggest Expense  : None\n")
        else:
             report.write(f"Biggest Expense  : {biggest_category} (₹{biggest_expense})\n")
        report.write(f"Expense Entries  : {len(expense_lines)}\n")
        report.write(f"Journal Entries  : {journal_content.count('Day ')}\n")

        report.write("\n")
        report.write("="*40+"\n")
        report.write("Generated by WanderLog\n")
        report.write("="*40+"\n")

    print("\nTrip report exported successfully!")

    with open("report.txt","r",encoding="utf-8")as report:
        print(report.read())
        pause()

def delete_expense():
    with open("expenses.txt","r")as file:
        expense_lines=file.readlines()
    
    if len(expense_lines)==0:
        print("\nNo expenses found!")
        pause()
        return

    print_section("EXPENSES")

    for i,line in enumerate(expense_lines,start=1):
        category,amount=line.strip().split(": ")
        print(f"{i}. {category:<15} : ₹{amount}")
    
    
    while True:
        try:
            number=int(input("\nEnter expense number to delete: "))
            
            if 1<=number<=len(expense_lines):
                break
            else:
                print("Invalid expense number!")
        except ValueError:
            print("Please enter a valid number!")
    expense_lines.pop(number-1)

    with open("expenses.txt","w")as file:
        file.writelines(expense_lines)

    print("\nExpense deleted successfully!")
    pause()

def print_header(title):
    print("\n"+"="*40)
    print(title.center(40))
    print("="*40)

def print_section(title):
    print("\n"+title)
    print("-"*40)

def clear_screen():
    os.system("cls")


while True:   
    clear_screen() 
    print_header("WANDERLOG")

    print("1. Create Trip")
    print("2. Add Journal Entry")
    print("3. Add Expense")
    print("4. View Trip Summary")
    print("5. Search Journal Entries")
    print("6. View Statistics")
    print("7. Export Trip Report")
    print("8. Delete Expense")
    print("9. Exit")

    print("=" * 40)

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
        export_report()

    elif choice=="8":
        delete_expense()

    elif choice=="9":
        print("\nThank you for using WanderLog!")
        break

    else:
        print("\nInvalid choice! Please choose from 1-9.")




        