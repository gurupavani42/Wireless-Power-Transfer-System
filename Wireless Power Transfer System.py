# Wireless-Power-Transfer-System
# Wireless Power Transfer System

power = 0
max_power = 100

while True:
    print("\n--- WIRELESS POWER TRANSFER ---")
    print("1. Start Power Transfer")
    print("2. Stop Power Transfer")
    print("3. Check Power")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        if power < max_power:
            power += 20
            print("Wireless power transfer started.")
            print("Transferred Power:", power, "%")
        else:
            print("Maximum power transferred!")

    elif choice == "2":
        power = 0
        print("Wireless power transfer stopped.")

    elif choice == "3":
        print("Current Transferred Power:", power, "%")

    elif choice == "4":
        print("System stopped.")
        break

    else:
        print("Invalid choice!")
