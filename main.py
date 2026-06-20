print("===== WANDERLOG =====")
print("1. Create Trip")
print("2. Add Journal Entry")
print("3. Add Expense")
print("4. View Trip Summary")
print("5. Exit")

choice=input('Choose an option: ')

if choice=="1":
    desination=input("Destination: ")
    start_date=input("Start Date: ")
    days=input("Number of Days: ")
    budget=input("Budget: ")

    with open("trips.txt","w")as file:
        file.write("Destination: "+desination+ "\n")
        file.write("Start Date:"+start_date+ "\n")
        file.write("Days: "+days+ "\n")
        file.write("Budget: "+budget+ "\n")

    print("\nTrip created successfully!")
                   
                   
