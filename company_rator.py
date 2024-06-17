#Python company rating App
import json

# Initialize an empty company database
companies = []

# Function to add a new company to the database
def add_company():
    name = input("Enter the company name: ")
    rating = int(input("Enter a rating (1-5): "))
    if 1 <= rating <= 5:
        company = {"name": name, "rating": rating}
        companies.append(company)
        print(f"{name} has been added with a rating of {rating}.")
    else:
        print("Invalid rating. Rating must be between 1 and 5.")

# Function to list all companies and their ratings
def list_companies():
    if not companies:
        print("No companies in the database.")
    else:
        print("Company Ratings:")
        for idx, company in enumerate(companies, 1):
            print(f"{idx}. {company['name']} - Rating: {company['rating']}")

# Main program loop
while True:
    print("\nCompany Rating App")
    print("1. Add a company")
    print("2. List all companies")
    print("3. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_company()
    elif choice == "2":
        list_companies()
    elif choice == "3":
        # Save the database to a JSON file before quitting
        with open("company_ratings.json", "w") as file:
            json.dump(companies, file)
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

#Xafiq
