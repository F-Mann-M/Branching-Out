import json

def load_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def filter_users_by_name():
    users = load_file("users.json")
    name = input("Enter a name to filter users: ").strip()
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)

def filter_users_by_age():
    users = load_file("users.json")
    age = int(input("Enter age to filter users: "))
    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email():
    users = load_file("users.json")
    email = input("Enter an email to filer users: ")
    filter_users = [user for user in users if user["email"] == email]

    for user in filter_users:
        print(user)


if __name__ == "__main__":

    user_choice = {
        "name": filter_users_by_name,
        "age": filter_users_by_age,
        "email": filter_users_by_email
    }

    filter_option = input("What would you like to filter by? (name, age, email): ").strip().lower()

    if filter_option in user_choice:
        user_choice[filter_option]()
    else:
        print("Filtering by that option is not yet supported.")
