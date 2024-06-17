shopping_list = []


while True:
    print("\nOptions to choose: \n1: Add to list\n2: Detele from list\n3: Show the list\n4: Empty the list\n5: Quit")
    choix = input("Your choice : ")

    if choix == '1': liste_courses.append(input("Entrer element to add : "))
    elif choix == '2':
        element_a_retirer = input("Entrer element to delete from list : ")
        if element_a_retirer in liste_courses:
            liste_courses.remove(element_a_retirer)
            print(f"'{element_a_retirer}' have beed delete from the list.")
        else:
            print("Element not in the list.")
    elif choix == '3':
        [print(f"{i}. {element}") for i, element in enumerate(liste_courses, 1)] if liste_courses else print("The list is empty.")
    elif choix == '4': liste_courses.clear(); print("List deleted.")
    elif choix == '5': 
        print("See ya!")
        break
    else: 
        print("Invalid choice.")

#Xafiq
