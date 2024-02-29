while True:
    print("Press-1:To convert in lowercase\nPress-2:To convert in uppercase")
    choice = int (input("Enter your choice: "))
    str=input("Enter a string: ")

    if choice==1:
        sl = str.lower()
        print("String in lowercase is: ",sl)

    elif choice==2:
        sl=str.upper()
        print("String in uppercase is: ",sl)

    else:
        print("Invalid choice entered")

    choice= input("Do you want to continue?(y/n):")
    if choice=='n' or choice=='N':
        break
 
