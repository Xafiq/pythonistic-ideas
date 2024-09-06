shopping_list = []


while True:
    print("\nOptions to choose: \n1: Add to list\n2: Detele from list\n3: Show the list\n4: Empty the list\n5: Quit")
    choice = input("Your choice : ")

    if choice == '1': liste_courses.append(input("Entrer element to add : "))
    elif choice == '2':
        element_to_delete = input("Entrer element to delete from list : ")
        if element_to_delete in liste_courses:
            liste_courses.remove(element_to_delete)
            print(f"'{element_to_delete}' have beed delete from the list.")
        else:
            print("Element not in the list.")
    elif choice == '3':
        [print(f"{i}. {element}") for i, element in enumerate(liste_courses, 1)] if liste_courses else print("The list is empty.")
    elif choice == '4': liste_courses.clear(); print("List deleted.")
    elif choice == '5': 
        print("See ya!")
        break
    else: 
        print("Invalid choice.")

#Xafiq
