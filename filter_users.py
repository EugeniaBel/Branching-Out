import json

def filter_users_by_name(data, name_prefix):
    filtered_users = [user for user in data if user['name'].startswith(name_prefix)]
    return filtered_users

if __name__ == "__main__":
    with open("users.json", "r") as f:
        user_data = json.load(f)

    prefix = input("Enter the name prefix to filter by: ")
    filtered_results = filter_users_by_name(user_data, prefix)

    print("\nUsers with names starting with '{}':".format(prefix))
    for user in filtered_results:
        print(f"- {user['name']} (ID: {user['id']}, Age: {user['age']}, Email: {user['email']})")
