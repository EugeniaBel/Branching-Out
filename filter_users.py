import json

def filter_users_by_name(data, name):
    filtered_users = [user for user in data if user['name'].lower() == name.lower()]
    return filtered_users

def filter_users_by_age(data, age):
    filtered_users = [user for user in data if user['age'] == int(age)]
    return filtered_users

if __name__ == "__main__":
    with open("users.json", "r") as file:
        user_data = json.load(file)

    filter_option = input("What would you like to filter by? ('name' or 'age'): ").strip().lower()

    filtered_results = []
    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filtered_results = filter_users_by_name(user_data, name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        try:
            filtered_results = filter_users_by_age(user_data, age_to_search)
        except ValueError:
            print("Invalid age entered. Please enter a number.")
    else:
        print("Filtering by that option is not supported.")

    if filtered_results:
        print("\nFiltered Users:")
        for user in filtered_results:
            print(f"- {user['name']} (ID: {user['id']}, Age: {user['age']}, Email: {user['email']})")
    else:
        if filter_option in ["name", "age"]:
            print("\nNo users found matching your criteria.")
